"""GUI made in tkinter that gives at the start of the game the player some basic choices.
size of grid, choosing X or O and playing vs computer or other player"""
import tkinter as tk


def settings():
    # Setting main widget
    width = 400
    height = 280
    root = tk.Tk()
    root.title("Game settings")
    root.geometry(f"{width}x{height}")
    root.configure(background="black")

    # Labels
    info = tk.Label(root, text="Select game specifications.", font=" ComicSans 16",
                    fg="white", bg="black").grid(row=0, column=0, columnspan=3)
    grid = tk.Label(root, text="Grid size.", font="ComicSans 12",
                    fg="white", bg="black").grid(row=2, column=0)
    players = tk.Label(root, text="Players", font="ComicSans 12",
                       fg="white", bg="black").grid(row=2, column=1)
    turn = tk.Label(root, text="Play as:", font="ComicSans 12",
                    fg="white", bg="black").grid(row=2, column=2)

    # Start button
    pressed = False

    def got_pressed():
        nonlocal pressed
        pressed = True
        root.destroy()

    button = tk.Button(root, text="Start", command=got_pressed,
                       fg="white", bg="black").grid(row=6, column=2, sticky="news")
    print("1")
    # Radio buttons and their variables
    grid = tk.IntVar()
    grid.set(3)
    tk.Radiobutton(root, text="3x3", padx=20, variable=grid, value=3, indicator=0, activebackground="#252525",
                   fg="white", bg="black", selectcolor="#252525").grid(row=3, column=0, sticky="news")
    tk.Radiobutton(root, text="4x4", padx=20, variable=grid, value=4, indicator=0, activebackground="#252525",
                   fg="white", bg="black", selectcolor="#252525").grid(row=4, column=0, sticky="news")
    tk.Radiobutton(root, text="5x5", padx=20, variable=grid, value=5, indicator=0, activebackground="#252525",
                   fg="white", bg="black", selectcolor="#252525").grid(row=5, column=0, sticky="news")

    turn = tk.StringVar()
    turn.set("x")
    tk.Radiobutton(root, text="X", padx=20, variable=turn, value="x", indicator=0, activebackground="#252525",
                   fg="white", bg="black", selectcolor="#252525").grid(row=3, column=2, sticky="news")
    tk.Radiobutton(root, text="O", padx=20, variable=turn, value="o", indicator=0, activebackground="#252525",
                   fg="white", bg="black", selectcolor="#252525").grid(row=4, column=2, sticky="news")

    versus = tk.IntVar()
    versus.set(0)
    tk.Radiobutton(root, text="Player vs Player", padx=20, variable=versus, value=0, activebackground="#252525",
                   indicator=0, fg="white", bg="black", selectcolor="#252525").grid(row=3, column=1, sticky="news")
    tk.Radiobutton(root, text="Player vs Computer", padx=20, variable=versus, value=1, activebackground="#252525",
                   indicator=0, fg="white", bg="black", selectcolor="#252525").grid(row=4, column=1, sticky="news")

    # Configure weights of col and rows
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=2)
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
    root.minsize(width, height)
    root.maxsize(width, height)

    root.mainloop()

    if pressed:
        return grid.get(), turn.get(), versus.get()
    else:
        return None, None, None
