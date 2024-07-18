from reporting_server import Alignment, ClassShip
import json
from sqlalchemy.orm import (
    DeclarativeBase,
    declared_attr,
    Mapped,
    joinedload,
    mapped_column,
    relationship,
    sessionmaker,
    MappedAsDataclass,
)
import interaction_pb2
from sqlalchemy import UniqueConstraint, create_engine, Enum, ForeignKey, and_, select


class Base(MappedAsDataclass, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """Автогенирация имени таблицы в БД на основе названия класса"""
        return f"{cls.__name__.lower()}s"


class Officer(Base):
    __table_args__ = (
        UniqueConstraint("first_name", "last_name", "rank", name="uq_officer"),
    )
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        init=False,
    )
    first_name: Mapped[str]
    last_name: Mapped[str]
    rank: Mapped[str]

    spaceships: Mapped[list["Spaceship"]] = relationship(
        secondary="assignments",
        back_populates="officers",
        init=False,
    )


class Spaceship(Base):
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, init=False, default=None
    )
    alignment: Mapped[str]
    name: Mapped[str]
    ship_class: Mapped[str]
    length: Mapped[float]
    crew_size: Mapped[int]
    armed: Mapped[bool]
    speed: Mapped[float | None] = mapped_column(nullable=True, default=None, init=False)

    officers: Mapped[list["Officer"]] = relationship(
        secondary="assignments",
        back_populates="spaceships",
    )


class Assignment(Base):
    spaceship_id: Mapped[int] = mapped_column(
        ForeignKey("spaceships.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
    officer_id: Mapped[int] = mapped_column(
        ForeignKey("officers.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )


def get_engine():
    return create_engine("postgresql://postgres:root@localhost:5435/spaceship_reports")


def create_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)


def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine, autoflush=True)
    return Session()


def save_spaceship(session, ship: interaction_pb2.Spaceship):
    officers = []
    for o in ship.officers:
        stmt = select(Officer).filter_by(
            first_name=o.first_name, last_name=o.last_name, rank=o.rank
        )
        result = session.execute(stmt).scalars().first()
        officer = (
            result
            if result
            else Officer(first_name=o.first_name, last_name=o.last_name, rank=o.rank)
        )
        officers.append(officer)

    spaceship = Spaceship(
        alignment=ship.alignment.name,
        name=ship.name,
        ship_class=ship.ship_class.name,
        length=ship.length,
        crew_size=ship.crew_size,
        armed=ship.armed,
        officers=[],
    )

    session.add(spaceship)
    session.commit()

    spaceship.officers = officers
    session.merge(spaceship)
    session.commit()


def list_traitors(session):
    stmt_enemy = (
        select(Officer)
        .join(Assignment)
        .join(Spaceship)
        .filter(Spaceship.alignment.in_(["ENEMY"]))
        .distinct()
    )
    stmt_ally = (
        select(Officer)
        .join(Assignment)
        .join(Spaceship)
        .filter(Spaceship.alignment.in_(["ALLY"]))
        .distinct()
    )

    enemy_officers = session.execute(stmt_enemy).scalars().all()
    ally_officers = session.execute(stmt_ally).scalars().all()
    enemy_officers_set = {
        (officer.first_name, officer.last_name, officer.rank)
        for officer in enemy_officers
    }
    ally_officers_set = {
        (officer.first_name, officer.last_name, officer.rank)
        for officer in ally_officers
    }

    traitors_set = enemy_officers_set.intersection(ally_officers_set)
    traitors_list = [
        {"first_name": first_name, "last_name": last_name, "rank": rank}
        for first_name, last_name, rank in traitors_set
    ]

    for traitor in traitors_list:
        print(json.dumps(traitor))
