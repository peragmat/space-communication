from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Spaceship(_message.Message):
    __slots__ = ("alignment", "name", "ship_class", "length", "crew_size", "armed", "officers")
    class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALLY: _ClassVar[Spaceship.Alignment]
        ENEMY: _ClassVar[Spaceship.Alignment]
    ALLY: Spaceship.Alignment
    ENEMY: Spaceship.Alignment
    class ShipClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CORVETTE: _ClassVar[Spaceship.ShipClass]
        FRIGATE: _ClassVar[Spaceship.ShipClass]
        CRUISER: _ClassVar[Spaceship.ShipClass]
        DESTROYER: _ClassVar[Spaceship.ShipClass]
        CARRIER: _ClassVar[Spaceship.ShipClass]
        DREADNOUGHT: _ClassVar[Spaceship.ShipClass]
    CORVETTE: Spaceship.ShipClass
    FRIGATE: Spaceship.ShipClass
    CRUISER: Spaceship.ShipClass
    DESTROYER: Spaceship.ShipClass
    CARRIER: Spaceship.ShipClass
    DREADNOUGHT: Spaceship.ShipClass
    class Officer(_message.Message):
        __slots__ = ("first_name", "last_name", "rank")
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        RANK_FIELD_NUMBER: _ClassVar[int]
        first_name: str
        last_name: str
        rank: str
        def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., rank: _Optional[str] = ...) -> None: ...
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHIP_CLASS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    CREW_SIZE_FIELD_NUMBER: _ClassVar[int]
    ARMED_FIELD_NUMBER: _ClassVar[int]
    OFFICERS_FIELD_NUMBER: _ClassVar[int]
    alignment: Spaceship.Alignment
    name: str
    ship_class: Spaceship.ShipClass
    length: float
    crew_size: int
    armed: bool
    officers: _containers.RepeatedCompositeFieldContainer[Spaceship.Officer]
    def __init__(self, alignment: _Optional[_Union[Spaceship.Alignment, str]] = ..., name: _Optional[str] = ..., ship_class: _Optional[_Union[Spaceship.ShipClass, str]] = ..., length: _Optional[float] = ..., crew_size: _Optional[int] = ..., armed: bool = ..., officers: _Optional[_Iterable[_Union[Spaceship.Officer, _Mapping]]] = ...) -> None: ...

class Coordinates(_message.Message):
    __slots__ = ("right_ascension", "declination")
    RIGHT_ASCENSION_FIELD_NUMBER: _ClassVar[int]
    DECLINATION_FIELD_NUMBER: _ClassVar[int]
    right_ascension: str
    declination: str
    def __init__(self, right_ascension: _Optional[str] = ..., declination: _Optional[str] = ...) -> None: ...
