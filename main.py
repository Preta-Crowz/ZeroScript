import re
from zclass import *
from zbuiltin import *
curr = []
code = ""
script = ""
# startpoint = {"[":"list","(":"tuple","<":"set","{":"dict"}
# endpoint = {"list":"]","tuple":")","set":">","dict":"}","byte":"\'","string":"\""}
'''
list [1,2,3]
tuple (1,2,3)
set <1,2,3>
dice {"a":1,"b":2}
byte 'asdf'
string "asdf"


var name = value
func name = (input) {
   code 
}
'''
do = func["do"]
mode = int(input("0. Open File\n1. Interpreter Mode\n2. Debug Mode\n> "))
if mode == 0:
    do(re.split("[\n;]",open(input("file > ")).read()))
elif mode == 1 or mode == 2:
    while True:
        try: do(re.split("[\n;]",input("::> ")),interpret=True,debug=(mode==2))
        except Exception as e: print(e)