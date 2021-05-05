import deck, count_tk, time, check
from tkinter import *
import tkinter.font as font

window = Tk()
window.title("Poker Calculator")
window.geometry("600x400")
window.configure(bg="darkred")
myfont = font.Font(weight="bold")

# creates a shuffled deck of cards and counter object for possible hands
deck = deck.Deck()
count = count_tk.Count()
check = check.Check()

def click():
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

"""
Use the following function to manually add and test card combinations
You can then print the boolean value of which card combination you seek

It doesnt matter how many hands you enter when you use this function
"""
def test():
    cards = []
    cards.append(deck.Card('A', 'red hearts'))
    cards.append(deck.Card('2', 'red hearts'))
    cards.append(deck.Card('3', 'red hearts'))
    cards.append(deck.Card('4', 'red hearts'))
    cards.append(deck.Card('5', 'red hearts'))

    output.delete(0.0, END)
    check.hand_combinations(count, cards)
    count.print_counts(output)


# The following code block is for creating the GUI of the poker app
output = Text(window, width=40, height=28, wrap=WORD, background="white")
output.place(x=10, y=10, anchor=NW)

lbl_enter = Label(window, text="Enter how many poker hands\nyou want to draw: ", bg="darkred", fg="white", justify="left")
lbl_enter['font'] = myfont
lbl_enter.place(x=350, y=125, anchor=NW)

txt_trials = Entry(window, width=20, bg="white")
txt_trials.place(x=350, y=175, anchor=NW)

btn_calculate = Button(window, text="Calculate", width=15, command=click)
btn_calculate['font'] = myfont
btn_calculate.place(x=375, y=225, anchor=NW)

window.resizable(False, False)
window.mainloop()