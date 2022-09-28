import random
krewes = {2:{"emily":"rain", "devoA":"duckyA"},
          7:{"vivian":"froggy", "devoB":"duckyB"},
          8:{"devo":"ducky", "devoC":"duckyC", "devoD":"duckyD"}
          }
def randomDev(krewes):
    key = random.choice(list(dict.keys(krewes)))
    nameDict = krewes[key]
    devo = random.choice(list(dict.keys(nameDict)))
    ducky = nameDict[devo]
    print(str(key)+", "+devo+", "+ducky+", ")
randomDev(krewes)