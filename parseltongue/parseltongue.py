from dragonfly import *

#Formatting Functions
def allLowerText(text):
	text = text.lower()
	Text("%(text)s").execute({"text": text})

def allUpperText(text):
	text = text.upper()
	Text("%(text)s").execute({"text": text})

def firstUpperText(text):
	text = text.capitalize()
	Text("%(text)s").execute({"text": text})

def firstAllUpperText(text):
	text = text.title()
	Text("%(text)s").execute({"text": text})
	
def camelCaseText(text):
	text = text.title()
	newText = ''.join(text.split())
	newText = newText[0:1].lower() + newText[1:]
	Text("%(text)s").execute({"text": newText})

#Grammar Dictionaries
arithmetic = {
	"plus": Text(" + "),
	"minus": Text(" - "),
	"into | multiply": Text(" * "),
	"divide | division": Text(" / "),
	"mod | modulo | modulus": Key("space, percent, space"),
	"floor | trunc | truncate": Text(" // "),
	"power": Text(" ** "),
}
			 
read = {
	"read": Text("input()") + Key("left"),
}

assign = {
	"equals | equal": Text(" = "),
	"increment | plus (equals | equal | assign)": Text("  +=  "),
	"decrement | minus (equals | equal | assign)": Text("  -=  "),
	"multiply (equals | equal | assign)": Text("  *=  "),
	"divide (equals | equal | assign)": Text("  /=  "),
	"(exponent | power) (equals | equal | assign)": Text("  **=  "),
	"(mod | modulo | modulus) (equals | equal | assign)": Text(" ") + Key("percent") + Text("=  "),
	"(floor | trunc) (equals | equal | assign)": Text("  //=  "),
}

cast = {	
	"float": Text("float()") + Key("left"),
	"integer": Text("int()") + Key("left"),
	"string": Text("str()") + Key("left"),
}
			
write = {
	"print": Text("print()") + Key("left"),
}
			
other = {
	"(initialize | 	are | variable | say) <text>": Function(allLowerText),
	"(num | number) <n>": Text("%(n)d"),
	"quote | coat": Text("\'\'") + Key("left"),
	"point": Text("."),
	"key <text>": Key("%(text)s"),
}

numchar = {
	"(num | number) to": Text("2"),
	"(num | number) zero": Text("0"),
}

shortcuts = {
	"execute | executive | run": Key("f5"),
	"open": Key("c-o"),
	"save": Key("c-s"),
	"directly save as <text>": Key("c-s") + Text("%(text)s") + Key("enter"),
	"directly replace as <text>": Key("c-s") + Text("%(text)s") + Key("enter,left,enter"),
	"scratch | backspace": Key("backspace"),
	"space": Key("space"),
	"colon": Text(": "),
	"delete": Key("del"),
	"end": Key("end"),
	"start": Key("home"),
	"next": Key("c-right"),
	"back": Key("c-left"),
	"over": Key("end,enter"),
	"tab": Key("tab"),
	"tab <n>": Key("tab:%(n)d"),
	"undo": Key("c-z"),
	"redo": Key("c-y"),
	"left <n>": Key("left:%(n)d"),
	"up <n>": Key("up:%(n)d"),
	"down <n>": Key("down:%(n)d"),
	"right <n>": Key("right:%(n)d"),
	"select all": Key("c-a"),
	"select last word": Key("cs-left"),
	"select next word": Key("cs-right"),
	"select (left | last) <n> (word | words)": Key("cs-left:%(n)d"),
	"select (right | next) <n> (word | words)": Key("cs-right:%(n)d"),
	"select (left | last) <n> ": Key("s-left:%(n)d"),
	"select (right | next) <n>": Key("s-right:%(n)d"),
	"select line": Key("home, s-end"),
	"go to line <n>": Key("c-home, down:%(n)d, up"),
	"comma": Text(", "),
}

conditionalStatements = {
	"inif | inloop": Key("end") + Text(":") + Key("enter,tab"),
	"if": Text("if "),
	"elif": Text("elif "),
	"else": Text("else:") + Key("enter,tab"),
	"while": Text("while "),
	"for": Text("for "),
	"break": Text("break") + Key("enter,tab"),
	"continue": Text("continue") + Key("enter,tab"),
	"equality": Text(" == "),
	"inequality": Text(" != "),
	"identity": Text(" === "),
	"(not | non) identity": Text(" !== "),
	"greater than": Text(" > "),
	"less than": Text(" < "),
	"greater than [and | or](equals | equal)": Text(" >= "),
	"less than [and | or] (equals | equal)": Text(" <= "),
	"and": Text(" and "),
	"or": Text(" or "),
	"not": Text(" not "),
	"in": Text(" in "),
	"is": Text(" is "),
}

inBuiltFunctions = {
	"dot": Text("."),
	"holder": Text("{}") + Key("left"),
	"[function] range": Text("range()") + Key("left"),
	"[function] abs": Text("abs()") + Key("left"),
	"[function] sorted": Text("sorted()") + Key("left"),
	"[function] (len|length)": Text("len()") + Key("left"),
	"[function] type": Text("type()") + Key("left"),
	"[function] map": Text("map()") + Key("left"),
	"[function] format": Text("format()") + Key("left"),
	"[function] split": Text("split()") + Key("left"),
	"[function] join": Text("split()") + Key("left"),
	"[function] add": Text("add()") + Key("left"),
	"[function] append": Text("append()") + Key("left"),
	"[function] extend": Text("extend()") + Key("left"),
	"[function] remove": Text("remove()") + Key("left"),
	"[function] pop": Text("pop()") + Key("left"),
	"[function] upper": Text("upper()"),
	"[function] lower": Text("lower()"),
	"[function] isupper": Text("isupper()"),
	"[function] islower": Text("islower()"),
}

userDefinedFunctions = {
	"define": Text("def "),
	"function <text>": Text("%(text)s():") + Key("left:2"),
	"empty function <text>": Text("%(text)s():") + Key("enter,tab"),
	"over tab": Key("end,enter,tab"),
	"call <text>": Text("%(text)s()"),
}

modules = {
	"import <text>": Text("import %(text)s "),
	"import (all | everything)": Text("import * "),
	"as <text>": Text("as %(text)s "),
	"from <text>": Text("from %(text)s "),
}

casing = {
	"camel <text>" : Function(camelCaseText),
	"full (caps | cap) <text>": Function(allUpperText),
	"uni (caps | cap) <text>": Function(firstUpperText),
	"first (caps | cap) <text>": Function(firstAllUpperText),
}

escapeSequence = {
	"escape [octal]": Text("\\"),
	"escape (hex | hexa)": Text("\\x"),
	"escape newline": Text("\\") + Key("enter"),
	"escape backslash": Text("\\\\"),
	"escape single [quote | coat]": Text("\\\'"),
	"escape double [quote | coat]": Text("\\\""),
	"escape bell": Text("\\a"),
	"escape backspace": Text("\\b"),
	"escape formfeed": Text("\\f"),
	"escape linefeed": Text("\\n"),
	"escape [carriage] return": Text("\\r"),
	"escape horizontal tab": Text("\\t"),
	"escape vertical tab": Text("\\v"),
}

lists = {
	"empty list" : Text("[]") + Key("enter"),
	"list" : Text("[]") + Key("left"),
	"function list" : Text("list()") + Key("left"),
}

letterMap = {
    "alpha": Text("a"),
    "beta ": Text("b"),
    "cell | sell": Text("c"),
    "delta": Text("d"),
    "eta ": Text("e"),
    "phi | fie": Text("f"),
    "gamma": Text("g"),
    "hat": Text("h"),
    "iota": Text("i"),
    "jack": Text("j"),
    "kappa": Text("k"),
    "lambda": Text("l"),
    "mu | mew": Text("m"),
    "nap": Text("n"),
    "omega | ohm | om": Text("o"),
    "pi | pie": Text("p"),
    "quad": Text("q"),
    "rho": Text("r"),
    "sigma": Text("s"),
    "theta | taw | tau": Text("t"),
    "upsi | oopsi": Text("u"),
    "vine": Text("v"),
    "wire": Text("w"),
    "xi | zaai": Text("x"),
    "yolo | yulu": Text("y"),
    "zeta | zeeta": Text("z"),
}

allCommands = dict(
	arithmetic.items() + 
	write.items() + 
	read.items() + 
	assign.items() + 
	cast.items() +
	other.items() +
	numchar.items() +
	shortcuts.items() +
	inBuiltFunctions.items() +
	userDefinedFunctions.items() +
	modules.items() +
	conditionalStatements.items() +
	casing.items() +
	escapeSequence.items() +
	lists.items() +
	letterMap.items()
)

#Converting Dictionary to usable Grammar
class AllCommands(MappingRule):
    mapping  = allCommands
	
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

#Changing commands to work as CCR (Continuous Command Recognition)
alternatives = []
alternatives.append(RuleRef(rule=AllCommands()))
singleCommand = Alternative(alternatives)
sequence = Repetition(singleCommand, min=1, max=16, name="sequence")

class ContinuousRules(CompoundRule):
    spec     = "<sequence> [[[and] repeat [that]] <n> times]"
    extras   = [
                sequence,
                IntegerRef("n", 1, 100),
               ]
    defaults = {
                "n": 1,
               }
	
	#Executes commands sequencially
    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]
        count = extras["n"]
        for i in range(count):
            for action in sequence:
                action.execute()