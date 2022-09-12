'''
@author: firat.atas
'''
import threading
import time

class Task():
    '''
    Thread
    '''
    def __init__(self, interval, function, *args, **kwargs):
        '''
        Constructor
        '''
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.run_status = False
        self.__task = None

    def __dummy_thread(self):
        '''
        __dummy_thread
        '''
        while self.run_status == True:
            start_time = time.time()
            self.function(*self.args, **self.kwargs)
            ellapsed_time = time.time() - start_time
            if(ellapsed_time < self.interval):
                time.sleep(self.interval - ellapsed_time)

    def start(self):
        '''
        start
        '''
        self.__task = threading.Thread(target = self.__dummy_thread)
        self.run_status = True
        self.__task.start()
        
    def join(self):
        '''
        stop
        '''
        self.run_status = False
        self.__task.join()
        