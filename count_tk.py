import json
from tkinter import *

class Count:
    '''
    counts which hands occur during a game of poker
    '''

    royal_flush = 0
    straight_flush = 0
    four_of_a_kind = 0
    full_house = 0
    flush = 0
    straight = 0
    three_of_a_kind = 0
    two_pair = 0
    one_pair = 0
    total_trials = 0

    """
    If you want to save the counts each time you run the project then:
    1. comment out self.reset()
    2. uncomment self.load() and self.save()
    
    If you want to only see the results of the current process then:
    1. comment out self.load() and self.save()
    2. uncomment self.reset()
    """
    def __init__(self):
        self.reset()

        self.load()
        self.save()

    def get_count(self, hand_ranking):
        if hand_ranking == 1:
            return self.royal_flush
        elif hand_ranking == 2:
            return self.straight_flush
        elif hand_ranking == 3:
            return self.four_of_a_kind
        elif hand_ranking == 4:
            return self.full_house
        elif hand_ranking == 5:
            return self.flush
        elif hand_ranking == 6:
            return self.straight
        elif hand_ranking == 7:
            return self.three_of_a_kind
        elif hand_ranking == 8:
            return self.two_pair
        elif hand_ranking == 9:
            return self.one_pair

    def print_counts(self, output):
        output.insert(END, "Hand Counts:")
        output.insert(END, "\n==============================")
        output.insert(END, "\nRoyal Flush:\t\t\t" + str(self.royal_flush))
        output.insert(END, "\nStraight Flush:\t\t\t" + str(self.straight_flush))
        output.insert(END, "\nFour of a Kind:\t\t\t" + str(self.four_of_a_kind))
        output.insert(END, "\nFull House:\t\t\t" + str(self.full_house))
        output.insert(END, "\nFlush:\t\t\t" + str(self.flush))
        output.insert(END, "\nStraight:\t\t\t" + str(self.straight))
        output.insert(END, "\nThree of a Kind:\t\t\t" + str(self.three_of_a_kind))
        output.insert(END, "\nTwo Pair:\t\t\t" + str(self.two_pair))
        output.insert(END, "\nOne Pair:\t\t\t" + str(self.one_pair))
        output.insert(END, "\n==============================")
        output.insert(END, "\nTotal Trials:\t\t" + str(self.total_trials))

    def save(self):
        file = open("data.json", "w")
        self.data = {"royal_flush": self.royal_flush,
                     "straight_flush": self.straight_flush,
                     "four_of_a_kind": self.four_of_a_kind,
                     "full_house": self.full_house,
                     "flush": self.flush,
                     "straight": self.straight,
                     "three_of_a_kind": self.three_of_a_kind,
                     "two_pair": self.two_pair,
                     "one_pair": self.one_pair,
                     "total_trials": self.total_trials}
        json.dump(self.data, file)
        file.close()

    def load(self):
        json_data = open("data.json", "r")
        data = json.load(json_data)
        for key in data.keys():
            if key == "royal_flush":
                self.royal_flush = data[key]
            elif key == "straight_flush":
                self.straight_flush = data[key]
            elif key == "four_of_a_kind":
                self.four_of_a_kind = data[key]
            elif key == "full_house":
                self.full_house = data[key]
            elif key == "flush":
                self.flush = data[key]
            elif key == "straight":
                self.straight = data[key]
            elif key == "three_of_a_kind":
                self.three_of_a_kind = data[key]
            elif key == "two_pair":
                self.two_pair = data[key]
            elif key == "one_pair":
                self.one_pair = data[key]
            elif key == "total_trials":
                self.total_trials = data[key]

        json_data.close()

    def reset(self):
        file = open("data.json", "w")
        self.data = {"royal_flush": 0,
                     "straight_flush": 0,
                     "four_of_a_kind": 0,
                     "full_house": 0,
                     "flush": 0,
                     "straight": 0,
                     "three_of_a_kind": 0,
                     "two_pair": 0,
                     "one_pair": 0,
                     "total_trials": 0}
        json.dump(self.data, file)
        file.close()
