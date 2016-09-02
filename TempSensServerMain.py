import time
from TempSensCoordinator import TempSensCoordinator


def run_server():
    coordinator = TempSensCoordinator()
    coordinator.start_server()
    while True:
        time.sleep(10)

run_server()
