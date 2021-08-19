import time
import tkinter.font as font
from tkinter import *

import deck
import check
import count_tk

# window setup
window = Tk()
window.title("Poker Calculator")
window.geometry("600x400")
window.configure(bg="darkred")
myfont = font.Font(weight="bold")

# creates a shuffled deck of cards and counter object for counting hand combinations
deck = deck.Deck()
count = count_tk.Count()
check = check.Check()

def click():
    """
    run when user clicks submit
    runs all the core logic of the program
    """
    trials = int(txt_trials.get())
    start = time.time()

    for i in range(trials):
        deck.reshuffle()
        cards = []

        for j in range(5):
            cards.append(deck.draw())

        check.hand_combinations(count, cards)

    end = time.time()
    runtime = end - start

    output.delete(0.0, END)
    count.total_trials += trials
    count.print_counts(output)
    output.insert(END, "\nTotal runtime: " + str(runtime))

    count.save()


def test():
    """
    manually add and test card combinations
    """
    cards = [
        deck.Card('A', 'red hearts'),
        deck.Card('2', 'red hearts'),
        deck.Card('3', 'red hearts'),
        deck.Card('4', 'red hearts'),
        deck.Card('5', 'red hearts')
    ]

    output.delete(0.0, END)
    check.hand_combinations(count, cards)
    count.print_counts(output)


# The following code block is for creating the GUI of the poker app
output = Text(window, width=40, height=28, wrap=WORD, background="white")
output.place(x=10, y=10, anchor=NW)

# label on right side of screen
lbl_enter = Label(
    window,
    text="Enter how many poker hands\nyou want to draw: ",
    bg="darkred",
    fg="white",
    justify="left"
)
lbl_enter['font'] = myfont
lbl_enter.place(x=350, y=125, anchor=NW)

# text entry box for amount of poker hands to draw/ trials to run
txt_trials = Entry(window, width=20, bg="white")
txt_trials.place(x=350, y=175, anchor=NW)

# for manual testing, set value of command param to "test"
btn_calculate = Button(window, text="Calculate", width=15, command=click)
btn_calculate['font'] = myfont
btn_calculate.place(x=375, y=225, anchor=NW)

# disable window resizing
window.resizable(False, False)
window.mainloop()