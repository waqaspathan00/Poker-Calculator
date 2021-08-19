import json
from tkinter import *


class Count:
    """
    counts which hands occur during a game of poker
    """

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

    def __init__(self):
        """
        If reset is commented, data between program runs will carry over
        If reset is uncommented, data will reset each time the program runs
        """
        # self.reset()

        self.load()
        self.save()

    def print_counts(self, output):
        """
        outputs all data to tkinter window
        """

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
        """
        saves data to data.json

        called from constructor
        """

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
        """
        loads data from data.json

        called from constructor
        """
        json_data = open("data.json", "r")
        data = json.load(json_data)
        print(data)
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
        """
        OPTIONAL METHOD
        resets data in data.json

        called from constructor

        If commented, data between program runs will carry over
        If uncommented, data will reset each time the program runs
        """

        file = open("data.json", "w")
        self.data = {
            "royal_flush": 0,
            "straight_flush": 0,
            "four_of_a_kind": 0,
            "full_house": 0,
            "flush": 0,
            "straight": 0,
            "three_of_a_kind": 0,
            "two_pair": 0,
            "one_pair": 0,
            "total_trials": 0
        }
        json.dump(self.data, file)
        file.close()
