import random
from collections import OrderedDict


## This code is originally from the blog post
##http://prolatio.blogspot.com/2016/08/all-256-syllogism-forms-with-examples.html
## I just modiefied it a little to get the syllogisms how I wanted the and then
## I added code to make and append the possible conclusions (be aware that the
## code still needs cleaning and it is not as efficient as it should)

sylloExamples = [('women', 'men', 'humans'),]

## sylloExamples contains the triplets of terms, these terms could be changed
## depending on if we want them to have semantic relation or not


wordType = {"S": "subject",
            "M": "middle",
            "P": "predicate"}


class Figure:
    def __init__(self, type=None):
        self.figureType = type
        if type == 1:
            self.major = ["M", "P"]
            self.minor = ["S", "M"]

        elif type == 2:
            self.major = ["P", "M"]
            self.minor = ["S", "M"]

        elif type == 3:
            self.major = ["M", "P"]
            self.minor = ["M", "S"]

        elif type == 4:
            self.major = ["P", "M"]
            self.minor = ["M", "S"]


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
        for sentence in ("major", "minor"):
            sOut = ""
            linkage = getattr(self.mood, sentence + "Link")
            linkWord = self.mood.linkMapping[linkage]
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
    all_generated_syllogisms = []
    Syllogisms = []
    for i in range(1, 5):
        for a in "aeio":
            for b in "aeio":
                for c in "aeio":
                    syllogisms = []
                    s = Syllogism(i, a + b + c)
                    syllogism = s.generate()
                    Syllogisms.append(syllogism)
                    syllogisms.append([syllogism[0]])
                    syllogisms.append([syllogism[1]])
                    all_generated_syllogisms.append(syllogisms)



    return all_generated_syllogisms , Syllogisms


generated_syllogisms = generateAll()[0]
premises = generateAll()[1]  ##change the name to premises but look  exactly what it does. the code itself works, just clean the names

## generated_syllogisms is a list that contains 256 list, each of them contains
## two lists (first ans second premise)


def CountFrequency(my_list):


    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

prem_terms = []
for prem in premises:
  Arg = ", ".join(prem)
  Arg = Arg.replace(",", " ")
  Arg = Arg.split()
  prems = []
  for wrd in Arg:
    if wrd in sylloExamples[0]:
      prems.append(wrd)
  prem_terms.append(prems)


freq = []
for i in prem_terms:
  dic= CountFrequency(i)
  freq.append(dic)


term_count = []
for dt in freq:
  list = [(t, s) for t, s in dt.items()]
  term_count.append(list)


Terms = []
for term in term_count:
  lst = []
  for tp in term:
    if tp[1] == 1:
      lst.append(tp[0])


  Terms.append(lst)



Possible_conclusions = []
for term in Terms:
  S = term[0]
  P = term[1]
  conclusion_choices = [
    "All {} are {}".format(S, P),
    "Some {} are {}".format(S, P),
    "No {} are {}".format(S, P),
    "Some {} are not {}".format(S, P),
    "All {} are {}".format(P, S),
    "Some {} are {}".format(P, S),
    "No {} are {}".format(P, S),
    "Some {} are not {}".format(P, S),
    "Nothing follows"
]
  Possible_conclusions.append(conclusion_choices)


x = 0
Prompts = []
for arguments in generated_syllogisms:
  complete_syllogisms = arguments + [Possible_conclusions[x]]
  Prompts.append(complete_syllogisms)
  x += 1
Complete_prompts = []
for prompt in Prompts:
   cprompt = """Choose the conclusion that logically follows the premises, 
if none of the conclusions logically follows choose 'Nothing follows'.

The premises are: {}{}.
The possible conclusions are {}.""".format(prompt[0], prompt[1], prompt[2])

   Complete_prompts.append(cprompt)
