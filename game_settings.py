"""GUI made in tkinter that gives at the start of the game the player some basic choices.
size of grid, choosing X or O and playing vs computer or other player"""
import tkinter as tk


def settings():
    # Setting main widget
    root = tk.Tk()
    root.title("Game settings")
    root.geometry("600x280")

    # Labels
    info = tk.Label(root, text="Select game specifications.", font=" ComicSans 16").grid(row=0, column=1)
    grid = tk.Label(root, text="Select game size.", font="ComicSans 12").grid(row=2, column=0)
    players = tk.Label(root, text="Players", font="ComicSans 12").grid(row=2, column=2)
    turn = tk.Label(root, text="Play as X or O", font="ComicSans 12").grid(row=2, column=1)

    # Start button
    button = tk.Button(root, text="Start", width=25, command=root.destroy).grid(row=6, column=2)

    # Radio buttons and their variables
    grid = tk.IntVar()
    grid.set(3)
    tk.Radiobutton(root, text="3x3", padx=20, variable=grid, value=3).grid(row=3, column=0)
    tk.Radiobutton(root, text="4x4", padx=20, variable=grid, value=4).grid(row=4, column=0)
    tk.Radiobutton(root, text="5x5", padx=20, variable=grid, value=5).grid(row=5, column=0)

    turn = tk.StringVar()
    turn.set("x")
    tk.Radiobutton(root, text="X", padx=20, variable=turn, value="x").grid(row=3, column=1)
    tk.Radiobutton(root, text="O", padx=20, variable=turn, value="o").grid(row=4, column=1)

    versus = tk.IntVar()
    versus.set(0)
    tk.Radiobutton(root, text="Player vs Player", padx=20, variable=versus, value=0).grid(row=3, column=2)
    tk.Radiobutton(root, text="Player vs Computer", padx=20, variable=versus, value=1).grid(row=4, column=2)

    # Configure weights of col and rows
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=4)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=2)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=2)

    # Lock window size
    root.update()
    root.minsize(600, 280)
    root.maxsize(600, 280)

    root.mainloop()

    return grid.get(), turn.get(), versus.get()
