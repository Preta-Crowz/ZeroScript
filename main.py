import zclass
func = {}
var = {}
curr = []
code = []
script = ""
startpoint = {"[":"list","(":"tuple","<":"set","{":"dict"}
endpoint = {"list":"]","tuple":")","set":">","dict":"}","byte":"\'","string":"\""}



def obj(inp,type):
    inp = list(inp)
    while inp:
        char = inp.pop(0)

if __name__ == "__main__":
    while True:
        tag = ">>> "
        if curr != []: tag = "... "
        raw = input(tag)
        raw = list(raw)
        while raw:
            char = raw.pop(0)
            if char == ";" and curr == []:
                code.append(script)
                script = ""
                continue
            if char in endpoint.values():
                if len(curr) and endpoint[curr[-1]] == char:
                    curr.pop(-1)
                    continue
            if char in startpoint:
                curr.append(startpoint[char])
                continue
            if char == "\'":
                if len(curr) == 0:
                    continue
                elif curr[-1] != "byte":
                    curr.append("byte")
                    continue
            if char == "\"":
                if len(curr) == 0:
                    continue
                elif curr[-1] != "string":
                    curr.append("string")
                    continue
            script += char
        if curr != []: continue
        code.append(script)
        script = ""
        print(code)
        code = []