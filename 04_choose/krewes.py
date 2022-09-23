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
    print random.choice(random.choice(list(krewes.values())))
#     key = random.choice(dict.keys(krewes))
# #     name = random.choice()
#     print(key)
    
(randomDevo(dictionary.krewes))

    