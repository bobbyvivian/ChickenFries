import random

# krewes = {2:{"emily":"rain", "devoA":"duckyA"},
#           7:{"vivian":"froggy", "devoB":"duckyB"},
#           8:{"devo":"ducky", "devoC":"duckyC", "devoD":"duckyD"}
#           }

# opening krewes.txt file
f = open("krewes.txt", "r")
# content has krewes.txt as a string
content = f.read()

# tuples is formatted as ["pd$$$devo$$$ducky", ...]
tuples = content.split("@@@")
# empty dictionary
krewes = {}
# krewes_pds contains all the keys/pds in krewes as a list

for person in tuples:
    # splitting elements tuples into a lists of [pd, devo, ducky]
    temp = person.split("$$$")
    
    pd = temp[0]
    devo = temp[1]
    ducky = temp[2]
    
    if not (pd in krewes): # if there is no dictionary for that period yet
        krewes[pd] = {}
        # pd_dict is the dictionary/value for the key with specific pd
        # adds devo as key, and ducky as value to pd_dict
    krewes[pd][devo] = ducky

# print(krewes)

def random_dev(krewes):
    key = random.choice(list(dict.keys(krewes)))
    nameDict = krewes[key]
    devo = random.choice(list(dict.keys(nameDict)))
    ducky = nameDict[devo]
    print(str(key)+", "+devo+", "+ducky+", ")
random_dev(krewes)