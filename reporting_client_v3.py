import random
import sys

import grpc

import interaction_pb2
import interaction_pb2_grpc
from model import create_tables, get_session, list_traitors, save_spaceship
from spaceship import Officer, Spaceship


def get_coordinate() -> interaction_pb2.Coordinates:
    coordinates = interaction_pb2.Coordinates(
        right_ascension_h=random.randint(-30, 30),
        right_ascension_m=random.randint(0, 20),
        right_ascension_s=round(random.uniform(0, 20), 5),
        declination_h=random.randint(-30, 30),
        declination_m=random.randint(0, 20),
        declination_s=round(random.uniform(0, 20), 5),
    )
    return coordinates


def validate_and_print_ship(ship: interaction_pb2.Spaceship):
    try:
        spaceship = Spaceship(
            alignment=ship.alignment,
            name=ship.name,
            ship_class=ship.ship_class,
            length=ship.length,
            crew_size=ship.crew_size,
            armed=ship.armed,
            officers=[
                Officer(first_name=o.first_name, last_name=o.last_name, rank=o.rank)
                for o in ship.officers
            ],
        )
        print(spaceship.model_dump_json(indent=4))
        return spaceship
    except ValueError as e:
        print(f"Invalid spaceship data: {e}")


def scan_coordinates(coordinate: tuple):
    with grpc.insecure_channel("localhost:8888") as channel:
        stub = interaction_pb2_grpc.ReportingServiceStub(channel)

        request = interaction_pb2.Coordinates(
            right_ascension=coordinate[0],
            declination=coordinate[1],
        )
        feature = stub.GetSpaceshipEntries(request)

        session = get_session()
        for msg in feature:
            spaceship = validate_and_print_ship(msg)
            if spaceship is not None:
                save_spaceship(session, spaceship)


if __name__ == "__main__":
    # create_tables()

    # python reporting_client_v3.py scan 17 45 40.0409 −29 00 28.118
    # python reporting_client_v3.py list_traitors

    if len(sys.argv) < 2:
        print("Error parse args")
        sys.exit(1)
    command = sys.argv[1]

    if command == "scan":
        if len(sys.argv) != 4:
            print("Usage: reporting_client_v3.py scan <right_ascension> <declination>")
            sys.exit(1)
        coordinates = (sys.argv[2], sys.argv[3])
        scan_coordinates(coordinates)
    elif command == "list_traitors":
        session = get_session()
        list_traitors(session)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
