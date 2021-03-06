import re
from zclass import *
func = {}
var = {}

def log(value=None):
    if value is not None:
        v = do(value).value
        print(v)
        return v
func["log"] = log

func["x"] = exit
func["ep"] = exit
func["end"] = exit
func["done"] = exit
func["exit"] = exit
func["quit"] = exit
func["close"] = exit
func["close_the_console_and_zeroscript_process_from_my_system"] = exit

def inp(text=None):
    return zstr(input(text.value if text is not None else ""))
func["input"] = inp

def getFunc(name):
    v = do(name).value
    return func[v]
func["getFunc"] = getFunc

def do(script,**kargs):
    global func,var
    if type(script) == zstr:
        script = script._raw()
    if type(script) == str:
        script = re.split("[\n;]",script)
        if kargs.get("execute",False):
            r = None
            for c in script:
                last = do([eval(c)])
                r = last if not last is None else r
            return r
    for c in script:
        if kargs.get("debug",False): print(c)
        if c == "": continue
        elif re.match("^var +[^ ]+ *= *.*$",c):
            m = re.match("^var +(?P<varname>[^ ]+) *= *(?P<value>.*)$",c)
            value = do(m["value"])
            var[m["varname"]] = value
            return value
        elif re.match("^[^ ]+ *= *.*$",c):
            m = re.match("^(?P<varname>[^ ]+) *= *(?P<value>.*)$",c)
            vname = m["varname"]
            if not vname in var:
                raise NameError(f"Variable {c} is not defined.")
            value = do(m["value"])
            var[vname] = value
            return value
        elif re.match("^[^ \d\.][^ \.]*\.[^ \.]+$",c):
            m = re.match("(?P<parent>^[^ \d\.][^ ]*)\.(?P<sub>[^ \.]+)$",c)
            parent = do(m["parent"])
            sub = getattr(parent,m["sub"])
            if kargs.get("interpret",False) and not kargs.get("call",False): log(sub)
            return sub
        elif re.match("^\".*[^\\\\]*\"$",c):
            obj = zstr(re.match("^\"(?P<value>.*)\"$",c)["value"])
            if kargs.get("interpret",False) and not kargs.get("call",False): print(obj._raw())
            return obj
        elif re.match("^\d+$",c):
            obj = zint(re.match("^(?P<value>\d+)$",c)["value"])
            if kargs.get("interpret",False) and not kargs.get("call",False): print(obj._raw())
            return obj
        elif re.match("^\d+\.\d*$",c):
            obj = zfloat(re.match("^(?P<value>\d+\.\d*)$",c)["value"])
            if kargs.get("interpret",False) and not kargs.get("call",False): print(obj._raw())
            return obj
        elif re.match("^[^ \d][^ ]*?\(.*\)$",c):
            m = re.match("^(?P<fname>[^ ]*?)\((?P<args>.*)\)$",c)
            fname = m["fname"]
            if not fname in func:
                raise NameError(f"Function {fname} is not defined.")
            elif fname == "do":
                fargs = []
                for arg in str.split(m["args"],","):
                    fargs.append(do(arg))
                v = do(*fargs,execute=True)
            else:
                fargs = []
                for arg in str.split(m["args"],","):
                    fargs.append(do(arg))
                v = func[fname](*fargs)
            # if kargs.get("interpret",False) and not kargs.get("call",False): log(v)
            return v
        elif re.match("^[^ \d\.][^ \.]*$",c):
            try:
                if kargs.get("interpret",False) and not kargs.get("call",False): print(var[c]._raw())
                return var[c]
            except:
                raise NameError(f"Variable {c} is not defined.")
        else:
            raise SyntaxError("Invalid syntax")
func["do"] = do