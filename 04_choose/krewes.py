"""
Chicken Fries (Mahir Riki, Vivian Teo, Gabriel Thompson)
SoftDev
K04 -- python file that randomly generates a developer from a dictionary
2022-09-22
time spent: 0.5 hours
"""
import dictionary
import random

def randomDevo(krewes):
# printing only the devo's name
    # print(random.choice(random.choice(list(krewes.values()))))
# printing both the devo's name and period
    key = random.choice(list(dict.keys(krewes)))
    name = random.choice(list(krewes[key]))
    print(str(key)+", "+name)
    
(randomDevo(dictionary.krewes))

    