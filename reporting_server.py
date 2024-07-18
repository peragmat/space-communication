import enum
import random
from concurrent.futures import ThreadPoolExecutor

import grpc

import interaction_pb2
import interaction_pb2_grpc


class Alignment(enum.Enum):
    ALLY = 0
    ENEMY = 1


class ClassShip(enum.Enum):
    CORVETTE = 0
    FRIGATE = 1
    CRUISER = 2
    DESTROYER = 3
    CARRIER = 4
    DREADNOUGHT = 5


def generate_sapceship():
    def generate_officer():
        first_names = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "Unknown"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia"]
        ranks = ["Ensign", "Lieutenant", "Commander", "Captain"]

        return {
            "first_name": random.choice(first_names),
            "last_name": random.choice(last_names),
            "rank": random.choice(ranks),
        }

    alignment = random.choice(list(Alignment))
    officers = [generate_officer() for _ in range(random.randint(0, 2))]

    # spaceship = interaction_pb2.Spaceship(
    #     alignment=alignment.name,
    #     name=f"Spaceship-{random.randint(1, 1000)}",
    #     ship_class=random.choice(list(ClassShip)).name,
    #     length=round(random.uniform(80, 20000), 2),
    #     crew_size=random.randint(4, 500),
    #     armed=random.choice([True, False]),
    #     officers=officers,
    # )
    spaceship = interaction_pb2.Spaceship(
        alignment=Alignment.ENEMY.name,
        name=f"Spaceship-{random.randint(1, 1000)}",
        ship_class=ClassShip.CARRIER.name,
        length=1200,
        crew_size=200,
        armed=False,
        officers=officers,
    )
    return spaceship


class RouteReportingService(interaction_pb2_grpc.ReportingService):
    def GetSpaceshipEntries(self, request, context):
        ships = [generate_sapceship() for _ in range(random.randint(1, 10))]
        yield from ships


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    interaction_pb2_grpc.add_ReportingServiceServicer_to_server(
        RouteReportingService(), server
    )
    server.add_insecure_port("localhost:8888")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
