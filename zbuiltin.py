import re
from zclass import *
func = {}
var = {}

def log(value): print(do(value).value)
func["log"] = log

def do(script,**kargs):
    global func,var
    if type(script) == str: script = [script]
    for c in script:
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
        elif re.match("^[^ \d][^ ]*\(.*\)$",c):
            m = re.match("^(?P<fname>[^ ]*)\((?P<args>.*)\)$",c)
            return func[m["fname"]](*str.split(m["args"],","))
        elif re.match("^[^ \d][^ ]*$",c):
            try:
                if kargs.get("interpret",False) and not kargs.get("call",False): print(var[c].raw)
                return var[c]
            except:
                raise NameError(f"{c} is not defined.")
        else:
            raise SyntaxError("Invalid syntax")
func["do"] = do