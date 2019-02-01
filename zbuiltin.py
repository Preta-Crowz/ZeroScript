import re
from zclass import *
func = {}
var = {}

def log(value): print(do(value).value)
func["log"] = log

func["end"] = exit
func["exit"] = exit
func["quit"] = exit
func["close"] = exit
func["close_the_console_and_zeroscript_process_from_my_system"] = exit

def do(script,**kargs):
    global func,var
    if type(script) == zstr:
        script = script.raw
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
        if c == "": pass
        elif re.match("^var +[^ ]+ *= *\".*\"$",c):
            m = re.match("^var +(?P<varname>[^ ]+) *= *(?P<value>\".*\")$",c)
            value = do(m["value"])
            var[m["varname"]] = value
            return value
        elif re.match("^\".*\"$",c):
            obj = zstr(re.match("^\"(?P<value>.*)\"$",c)["value"])
            if kargs.get("interpret",False) and not kargs.get("call",False): print(obj.raw)
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
                return do(*fargs,execute=True)
            else:
                fargs = []
                for arg in str.split(m["args"],","):
                    fargs.append(do(arg))
                return func[fname](*fargs)
        elif re.match("^[^ \d][^ ]*$",c):
            try:
                if kargs.get("interpret",False) and not kargs.get("call",False): print(var[c].raw)
                return var[c]
            except:
                raise NameError(f"{c} is not defined.")
        else:
            raise SyntaxError("Invalid syntax")
func["do"] = do