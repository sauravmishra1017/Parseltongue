from dragonfly import *

arithmetic = {

"plus": Text(" + "),
"minus": Text(" - "),
"into|multiply": Text(" * "),
"divide|division": Text(" / "),
"mod|modulo|modulus": Key("percent"),
"floor|trunc|truncate": Text(" // "),
"power": Text(" ** "),

}
			 
read = {
"read": Text("input()") + Key("left"),
}

assign = {
"<text> equals": Text("%(text)s = "),
"(to|two) <text>": Key("home") + Text("%(text)s = "),
}

cast = {	

"float": Text("float()") + Key("left"),
"integer <text>": Text("int(%(text)s)"),
"string": Text("str()") + Key("left"),

}
			
write = {
"print": Text("print()") + Key("left"),
}
			
other = {

"(variable|say) <text>": Text("%(text)s"),
"next": Key("end") + Key("enter"),
"<n>": Text("%(n)d"),
"quote | coat": Text("\'\'") + Key("left"),
"point": Text("."),
"key <text>": Key("%(text)s"),

}

numchar = {

"to": Text("2"),
"be": Text("B"),
"see": Text("C"),

}

interact = {

"execute | executive | run": Key("f5"),
"directly save as <text>": Key("c-s") + Text("%(text)s") + Key("enter"),
"directly save and replace as <text>": Key("c-s") + Text("%(text)s") + Key("enter,left,enter"),

}

allcommands = dict(

arithmetic.items() + 
write.items() + 
read.items() + 
assign.items() + 
cast.items() +
other.items() +
numchar.items() +
interact.items()

)

class AllCommands(MappingRule):
    mapping  = allcommands
	
    extras   = [
                Dictation("text"),				
				Dictation("text1"),
				Dictation("text2"),
				Dictation("text3"),
				
				IntegerRef("n",1,100000000),
				IntegerRef("n1",0,1000),
				IntegerRef("n2",0,1000),	
               ]
    defaults = {
                "n": 1,
               }