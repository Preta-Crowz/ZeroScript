import re
import zclass
func = {}
var = {}
curr = []
code = []
script = ""
startpoint = {"[":"list","(":"tuple","<":"set","{":"dict"}
endpoint = {"list":"]","tuple":")","set":">","dict":"}","byte":"\'","string":"\""}