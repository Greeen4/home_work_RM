from time import time


class catchtime(object):
    def __enter__(self):
        self.t = time()
        return self

    def __exit__(self, type, value, traceback):
        self.t = time() - self.t

    def timer(self):
        print('test')

with catchtime() as t:
    print('lk')
