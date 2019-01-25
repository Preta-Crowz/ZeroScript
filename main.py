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
if not int(input("0. Open File\n1. Interpreter Mode\n> ")):
    do(re.split("[\n;]",open(input("file > ")).read()))
else:
    while True:
        try: do(re.split("[\n;]",input("::> ")),interpret=True)
        except Exception as e: print(e)