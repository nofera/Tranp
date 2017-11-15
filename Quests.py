# This is answer. What question?

import random


class Train:
    def __init__(self, some_var=1):
        self.train = [bool(random.getrandbits(1)) for item in range(some_var)]

    def do_something(self):
        light_status_in_wagon = self.train[-1]
        print("Light in previous wagon is " + str(light_status_in_wagon))
        item = 1
        while (True):
            self.train[item] = not self.train[item]
            if light_status_in_wagon != self.train[-1]:
                print("Answer is " + str(item + 1))
                break
            item = item + 1


Siberia = Train(30)
Siberia.do_something()