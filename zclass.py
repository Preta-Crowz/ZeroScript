class zobj:
    def __init__(self,raw):
        value = self._preset(raw)
        self._set(value)
        self.properties = {
            "val": {},
            "func": {}
        }
        self._class = type(self)

    def _preset(self,raw):
        return raw

    def _set(self,value):
        self.value = value
        self._pyObject = value

    def _raw(self):
        return str(self.value)


class zstr(zobj):
    def _preset(self,raw):
        return str(raw)

    def _raw(self):
        return "\""+str(self.value)+"\""

class zbyte(zobj):
    def _preset(self,raw):
        return bytes(raw)

    def _raw(self):
        return "\'"+str(self.value)[2:-1]+"\'"

class zint(zobj):
    def _preset(self,raw):
        return int(raw)

    def _raw(self):
        return str(self.value)

class zfloat(zobj):
    def _preset(self,raw):
        return float(raw)

    def _raw(self):
        return str(self.value)

class zlist(zobj):
    def _preset(self,raw):
        return list(raw)
        
    def _raw(self):
        return "["+",".join(self.value)+"]"

class zset(zobj):
    def _preset(self,raw):
        return set(raw)
        
    def _raw(self):
        return "<"+",".join(self.value)+">"

class ztuple(zobj):
    def _preset(self,raw):
        return tuple(raw)
        
    def _raw(self):
        return "("+",".join(self.value)+")"

class zdict(zobj):
    def _preset(self,raw):
        return dict(raw)
        
    def _raw(self):
        r = "{"
        for k in self.value.keys():
            r += f"\"{k}\":{self.value[k]},"
        return r[:-1]+"}"