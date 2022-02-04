"""GUI made in tkinter that gives at the start of the game the player some basic choices.
 playing vs computer or other player  and choosing X or O"""
import tkinter as tk


def settings():
    # Setting main widget
    width = 400
    height = 280
    root = tk.Tk()
    root.title("Game settings")
    root.geometry(f"{width}x{height}")
    root.configure(background="black")

    # Start button
    pressed = False

    def got_pressed():
        nonlocal pressed
        pressed = True
        root.destroy()

    button = tk.Button(root, text="Start", command=got_pressed,
                       fg="white", bg="black").grid(row=3, column=1, sticky="news")
    # Radio buttons and their variables

    turn = tk.StringVar()
    turn.set("x")
    tk.Radiobutton(root, text="X", padx=20, variable=turn, value="X", indicator=0, activebackground="#252525",
                   fg="white", bg="black", selectcolor="#252525").grid(row=1, column=1, sticky="news")
    tk.Radiobutton(root, text="O", padx=20, variable=turn, value="O", indicator=0, activebackground="#252525",
                   fg="white", bg="black", selectcolor="#252525").grid(row=2, column=1, sticky="news")

    versus = tk.IntVar()
    versus.set(0)
    tk.Radiobutton(root, text="Player vs Player", padx=20, variable=versus, value=0, activebackground="#252525",
                   indicator=0, fg="white", bg="black", selectcolor="#252525").grid(row=1, column=0, sticky="news")
    tk.Radiobutton(root, text="Player vs Computer", padx=20, variable=versus, value=1, activebackground="#252525",
                   indicator=0, fg="white", bg="black", selectcolor="#252525").grid(row=2, column=0, sticky="news")

    # Configure weights of col and rows
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)

    # Lock window size
    root.update()
    root.minsize(width, height)
    root.maxsize(width, height)

    root.mainloop()

    if pressed:
        return grid.get(), turn.get(), versus.get()
    else:
        return None, None, None
