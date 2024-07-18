from pydantic import BaseModel, field_serializer, model_validator
from typing import Any
from reporting_server import Alignment, ClassShip


class Officer(BaseModel):
    first_name: str
    last_name: str
    rank: str


class Spaceship(BaseModel):
    alignment: Alignment
    name: str
    ship_class: ClassShip
    length: float
    crew_size: int
    armed: bool
    officers: list[Officer]

    @field_serializer("alignment", "ship_class", when_used="json")
    def serialize_enum(value):
        return value.name.capitalize()

    @model_validator(mode="before")
    def validate_spaceship(cls, values: Any) -> Any:
        alignment = values.get("alignment", None)
        if alignment is None:
            raise ValueError("Unknown spaceship alignment")
        alignment = Alignment(alignment).name
        name = values.get("name")
        ship_class = ClassShip(values.get("ship_class"))
        length = values.get("length")
        crew_size = values.get("crew_size")
        armed = values.get("armed")

        # Constraints based on ship class
        constraints = {
            ClassShip.CORVETTE: {
                "length": (80, 250),
                "crew_size": (4, 10),
                "can_be_armed": True,
                "can_be_hostile": True,
            },
            ClassShip.FRIGATE: {
                "length": (300, 600),
                "crew_size": (10, 15),
                "can_be_armed": True,
                "can_be_hostile": False,
            },
            ClassShip.CRUISER: {
                "length": (500, 1000),
                "crew_size": (15, 30),
                "can_be_armed": True,
                "can_be_hostile": True,
            },
            ClassShip.DESTROYER: {
                "length": (800, 2000),
                "crew_size": (50, 80),
                "can_be_armed": True,
                "can_be_hostile": False,
            },
            ClassShip.CARRIER: {
                "length": (1000, 4000),
                "crew_size": (120, 250),
                "can_be_armed": False,
                "can_be_hostile": True,
            },
            ClassShip.DREADNOUGHT: {
                "length": (5000, 20000),
                "crew_size": (300, 500),
                "can_be_armed": True,
                "can_be_hostile": True,
            },
        }

        class_constraints = constraints.get(ship_class, None)

        if class_constraints is None:
            raise ValueError(f"Unspecified spaceship class {ship_class}")
        if not (
            class_constraints["length"][0] <= length <= class_constraints["length"][1]
        ):
            raise ValueError(f"Invalid length for {ship_class.name}")
        if not (
            class_constraints["crew_size"][0]
            <= crew_size
            <= class_constraints["crew_size"][1]
        ):
            raise ValueError(f"Invalid crew size for {ship_class.name}")
        if armed and not class_constraints["can_be_armed"]:
            raise ValueError(f"{ship_class.name} cannot be armed")
        if alignment == Alignment.ENEMY and name != "Unknown":
            raise ValueError("Enemy ships must have name 'Unknown'")
        if alignment != Alignment.ENEMY and name == "Unknown":
            raise ValueError("Non-enemy ships cannot have name 'Unknown'")
        if alignment == Alignment.ENEMY and not class_constraints["can_be_hostile"]:
            raise ValueError(
                f"Enemy ships of class {ship_class.name} can't be a hostile"
            )

        return values
