## This code is originally from the blog post
##http://prolatio.blogspot.com/2016/08/all-256-syllogism-forms-with-examples.html
## I modified it a little to get the syllogisms how I wanted them, and then
## I added code to make and append the possible conclusions (be aware that the
## code still needs cleaning, and it is not as efficient as it should)

sylloExamples = [('actuaries', 'sculptors', 'writers'), ('assistants', 'poets', 'scientists'),
                 ('athletes', 'assistants', 'chefs'), ('chemists', 'drivers', 'dancers'), 
                 ('chemists', 'workers', 'painters'), ('clerks', 'butchers', 'athletes'), 
                 ('dancers', 'bankers', 'riders'), ('doctors', 'riders', 'investors'), 
                 ('drivers', 'porters', 'chemists'), ('farmers', 'surfers', 'writers'),
                 ('gamblers', 'cleaners', 'models'), ('golfers', 'cyclists', 'assistants'),
                 ('hunters', 'analysts', 'swimmers'), ('joggers', 'actors', 'carpenters'),
                 ('linguists', 'cooks', 'models'), ('linguists', 'skaters', 'singers'),
                 ('managers', 'clerks', 'butchers'), ('miners', 'tellers', 'poets'), 
                 ('models', 'tailors', 'florists'), ('nurses', 'scholars', 'buyers'),
                 ('planners', 'sailors', 'engineers'), ('riders', 'agents', 'waiters'),
                 ('riders', 'novelists', 'linguists'), ('runners', 'opticians', 'clerks'),
                 ('scientists', 'novelists', 'florists'), ('skaters', 'barbers', 'cooks'),
                 ('students', 'cashiers', 'doctors'), ('students', 'hikers', 'designers'),
                 ('surfers', 'painters', 'porters'), ('therapists', 'hikers', 'opticians')]

## sylloExamples contains the triplets of terms; these terms could be changed
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
    linkMapping = {"A": "all ",
                   "E": "no ",
                   "I": "some ",
                   "O": "some ",
    }
    postVerbLink = {"A": "",
                    "E": "",
                    "I": "",
                    "O": "not "}

    def __init__(self, links):
        self.links = links
        self.majorLink = links[0]
        self.minorLink = links[1]

class Syllogism:
    def __init__(self, figure, mood, syllowords):
        self.figure = Figure(figure)
        self.mood = Mood(mood)
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
    possible_conclusions = []
    for terms in sylloExamples:
        for i in range(1, 5):
            for a in "AEIO":
                for b in "AEIO":         
                         s = Syllogism(i, a + b, terms)
                         syllogism = s.generate() + [a + b]
                         all_generated_syllogisms.append(syllogism)
                         choices = [f"""All {terms[0]} are {terms[2]}""",
                          f"""No {terms[0]} are {terms[2]}""",
                          f"""Some {terms[0]} are {terms[2]}""",
                          f"""Some {terms[0]} are not {terms[2]}""" ]
                         possible_conclusions.append(choices)



    return all_generated_syllogisms, possible_conclusions

syllogisms = generateAll()[0]
possible_conclusions = generateAll()[1]
