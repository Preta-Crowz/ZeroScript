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

class zint:
    def __init__(self,value):
        self.value = value
        self._pyObject = value
        self._class = zint

class zfloat:
    def __init__(self,value):
        self.value = values
        self._pyObject = value
        self._class = zfloat

class zlist:
    def __init__(self,*values):
        self.value = values
        self._pyObject = values
        self._class = zlist

class zset:
    def __init__(self,*values):
        self.value = values
        self._pyObject = values
        self._class = zset

class ztuple:
    def __init__(self,*values):
        self.value = values
        self._pyObject = values
        self._class = ztuple

class zdict:
    def __init__(self,*values):
        self.value = values
        self._pyObject = values
        self._class = zdict