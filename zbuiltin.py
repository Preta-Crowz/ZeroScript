import re
from zclass import *
func = {}
var = {}

def log(value): print(do(value).value)
func["log"] = log

func["end"] = exit
func["close"] = exit
func["quit"] = exit
func["close_the_console_and_zeroscript_process_from_my_system"] = exit

def do(script,**kargs):
    global func,var
    if type(script) == str:
        if kargs.get("execute",False):
            script = eval(script)
        script = re.split("[\n;]",script)
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
            return obj;'''
        elif re.match("^log\(.*\)$",c):
            things = re.match("^log\((?P<something>.*)\)$",c)["something"]
            things = re.split("[\n;]",things)
            for thing in things:
                print(do(thing,call=True).value,end="")
            print("")'''
        elif re.match("^[^ \d][^ ]*?\(.*\)$",c):
            m = re.match("^(?P<fname>[^ ]*?)\((?P<args>.*)\)$",c)
            fname = m["fname"]
            if not fname in func:
                raise NameError(f"Function {fname} is not defined.")
            elif fname == "do":
                do(*str.split(m["args"],","),execute=True)
            else:
                return func[fname](*str.split(m["args"],","))
        elif re.match("^[^ \d][^ ]*$",c):
            try:
                if kargs.get("interpret",False) and not kargs.get("call",False): print(var[c].raw)
                return var[c]
            except:
                raise NameError(f"{c} is not defined.")
        else:
            raise SyntaxError("Invalid syntax")
func["do"] = do