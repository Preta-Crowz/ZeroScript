class zstr:
    def __init__(self,value):
        self.value = str(value)
        self._pyObject = str(value)
        self._class = zstr
        self.raw = "\""+str(value)+"\""

class zbyte:
    def __init__(self,value):
        self.value = value
        self._pyObject = value
        self._class = zbyte
        self.raw = "\'"+str(value)+"\'"

class zint:
    def __init__(self,value):
        self.value = value
        self._pyObject = value
        self._class = zint
        self.raw = str(value)

class zfloat:
    def __init__(self,value):
        self.value = value
        self._pyObject = value
        self._class = zfloat
        self.raw = value

class zlist:
    def __init__(self,*value):
        self.value = list(value)
        self._pyObject = list(value)
        self._class = zlist
        self.raw = "["+",".join(self.value)+"]"

class zset:
    def __init__(self,*value):
        self.value = set(value)
        self._pyObject = set(value)
        self._class = zset
        self.raw = "<"+",".join(self.value)+">"

class ztuple:
    def __init__(self,*value):
        self.value = tuple(value)
        self._pyObject = tuple(value)
        self._class = ztuple
        self.raw = "("+",".join(self.value)+")"

class zdict:
    def __init__(self,*value):
        self.value = dict(value)
        self._pyObject = dict(value)
        self._class = zdict