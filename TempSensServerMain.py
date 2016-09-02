import time
import sys
import os
from TempSensCoordinator import TempSensCoordinator


def run_server():
    coordinator = TempSensCoordinator()
    coordinator.start_server()
    while True:
        time.sleep(10)


def deamon():
    if os.fork() > 0:
        sys.exit(0)

    os.setsid()
    os.chdir("/")
    os.umask(0)

    if os.fork() > 0:
        sys.exit(0)

    sys.stdout.flush()
    sys.stderr.flush()

    si = file('/dev/null', 'r')
    so = file('/dev/null', 'a+')
    serr = file('/dev/null', 'a+')
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(serr.fileno(), sys.stderr.fileno())

if len(sys.argv) == 2:
    if sys.argv[1].upper() in ["YES", "TRUE"]:
        deamon()


run_server()
