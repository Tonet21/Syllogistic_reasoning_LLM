import random
from collections import OrderedDict
from Mixtral import model_conclusions


sylloExamples = [('actuaries', 'sculptors', 'writers')]


class Figure:
    def __init__(self, type=None):
        self.figureType = type
        self.conclusion = ["S", "P"]
        if type == 1:
            self.major = ["M", "P"]
            self.minor = ["S", "M"]
            self.conclusion = ["S", "P"]
        elif type == 2:
            self.major = ["P", "M"]
            self.minor = ["S", "M"]
            self.conclusion = ["S", "P"]
        elif type == 3:
            self.major = ["M", "P"]
            self.minor = ["M", "S"]
            self.conclusion = ["S", "P"]
        elif type == 4:
            self.major = ["P", "M"]
            self.minor = ["M", "S"]
            self.conclusion = ["S", "P"]


class Mood:
    linkMapping = {"a": "all ",
                   "e": "no ",
                   "i": "some ",
                   "o": "some ",    
    }
    postVerbLink = {"a": "",
                    "e": "",
                    "i": "",
                    "o": "not "}
    
    def __init__(self, links):
        self.links = links
        self.majorLink = links[0]
        self.minorLink = links[1]
        self.conclusionLink = links[2]


logical = OrderedDict([("1aaa","barbara"), ("1eae","celarent"), 
    ("1aii","darii"), ("1eio","ferio"), 
    ("1aai","barbari"), ("1eao","celaront"),
    ("2eae","cesare"), ("2aee","camestres"), ("2eio","festino"), 
    ("2aoo","baroco"), ("2eao","cesaro"), ("2aeo","camestros"),
    ("3aii","datisi"), ("3iai","disamis"), ("3eio","ferison"),
    ("3oao","bocardo"), ("3eao","felapton"), ("3aai","darapti"),
    ("4aee","calemes"), ("4iai", "dimatis"), ("4eio","fresison"),
    ("4aeo","calemos"), ("4eao", "fesapo"), ("4aai","bamalip")
])




wordType = {"S": "subject",
            "M": "middle",
            "P": "predicate"}

class Syllogism:    
    def __init__(self, figure, mood, syllowords=None):
        self.figure = Figure(figure)
        self.mood = Mood(mood)
        if syllowords is None:
            syllowords = random.choice(sylloExamples)
        self.subject = syllowords[0]
        self.middle = syllowords[1]
        self.predicate = syllowords[2]
    
    def generate(self):
        allSentences = []
        for sentence in ("major", "minor", "conclusion"):
            sOut = ""
            
            linkage = getattr(self.mood, sentence + "Link")
            linkWord = self.mood.linkMapping[linkage]
            if sOut == "":
                linkWord = linkWord.capitalize()
            sOut += linkWord
            sFormat = getattr(self.figure, sentence)
            wt = wordType[sFormat[0]]
            sOut += getattr(self, wt)
            sOut += " are "
            sOut += self.mood.postVerbLink[linkage]
            wt = wordType[sFormat[1]]
            sOut += getattr(self, wt)
            allSentences.append(sOut)
        return allSentences
    
def generateAll():
    syllos = []
    for i in range(1 ,5):
        for a in "aeio":
            for b in "aeio":
                for c in "aeio":
                    s = Syllogism(i, a+b+c)
                    shorthand = "{0}{1}".format(i, a+b+c)
                    if shorthand in logical:
                        syllo = [shorthand] + s.generate()
                        syllos.append(syllo)
                    else:
                        syllos.append("Not a valid conclusion")
                    
                    
    return syllos              
    
Syllos = generateAll()


vcMood = []  ##list that contains the mood and the conclusion of valid syllogisms but if it's not valid it says "Not a valid conclusion"
for x in Syllos:
        if x != "Not a valid conclusion":
            arg = [x[0][3].capitalize()] + [x[3]]
            vcMood.append(arg)
        else:
            arg = "Not a valid conclusion"
            vcMood.append(arg)



Conclusions = model_conclusions
CsMood =[]
for Conclusion in Conclusions:
    if "All" in Conclusion:
        M = "A"
    elif "No" in Conclusion:
        M = "E"
    elif "Some" and "not" in Conclusion:
        M = "O"
    elif "Some" in Conclusion:
        M = "I"
    elif "Nothing follows" in Conclusion:
        M = Conclusion

    CMood = [M + ", " + Conclusion]
    CsMood.append(CMood)

