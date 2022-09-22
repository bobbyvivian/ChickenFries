""""""
krewes = {2:["a2","b2","c2"], 7:["a7","b7","c7"], 8:["a8","b8","c8"]}

import random
def randomDevo(krewes):
    return random.choice(random.choice(list(krewes.values())))

print(randomDevo(krewes))

    