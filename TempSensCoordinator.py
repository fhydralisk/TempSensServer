from TempSensServer import TempSensServer
from TempAlarmServer import TempAlarmServer
from TsLog import ts_log


class TempSensCoordinator(object):
    """
    Coordinator of Server
    """
    def __init__(self):
        self.sensServer = TempSensServer(coordinator=self)
        self.alarmServer = TempAlarmServer(coordinator=self)

    def start_server(self):
        try:
            if not self.sensServer.is_running():
                self.sensServer.run_deamon()
            if not self.alarmServer.is_running():
                self.alarmServer.run_deamon()
        except:
            ts_log("Error when starting server.")
            exit(1)

    def shall_alarm(self, devid):
        try:
            return self.sensServer.shall_alarm(devid)
        except KeyError:
            pass
        except:
            ts_log("Unexpected error happen in shall_alarm", debug_trace=True)
            pass


