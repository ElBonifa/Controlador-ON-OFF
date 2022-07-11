from PyQt5.QtCore import *
from pyModbusTCP.client import ModbusClient
import time
import json

thread_pool = QThreadPool()
SERVERHOST = "localhost"
PORTHOST = 502


class ModBus_client():
    def __init__(self, args, kwargs):
        pass


class WorkerSignals(QObject):
    measurements_signals = pyqtSignal(list)
    data = pyqtSignal(dict)
    target_points = pyqtSignal(list)
    connection_error = pyqtSignal(str)
    running = pyqtSignal(str)
    stopped = pyqtSignal(str)
    sample = pyqtSignal(dict)


class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        '''
        worker here
        '''
        self.func = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        '''
        code here
        '''
        self.func()
datalist = []

if __name__ == "__main__":

    client = ModbusClient(host=SERVERHOST, port=PORTHOST, debug=False)

    while True:
        if not client.is_open():
            if not client.open():
                print("unnable to connect to " + SERVERHOST + " : " + str(PORTHOST))
        if client.is_open():
            print(client.last_error())
            data = client.read_holding_registers(0, 10)
            print("data", data)
            datalist.append(data)
            datalist2 = [datalist[-1]]
            with open('Medida.json', 'w') as file:
                json.dump(datalist2, file)

        time.sleep(0.5)


