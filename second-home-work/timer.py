from time import time


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


class catchtime(object):
    def __init__(self, units='s'):
        self.units = units


    def __enter__(self):
        self.t = time()

        return self


    def __exit__(self, type, value, traceback):
        self.t = time() - self.t


    def elapsed_time(self):
        if self.units == 's': return str(toFixed(self.t, 5)) + ' seconds'
        if self.units == 'm': return str(toFixed(self.t / 60, 5)) + ' minutes'
        if self.units == 'h': return str(toFixed(self.t / 3600, 5)) + ' hours'
