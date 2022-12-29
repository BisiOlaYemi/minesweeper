from tkinter import *
from cell import Cell
import settings
import util

root = Tk()

# override the setting of the window

root.configure(bg="black")
root.wm_geometry(F'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Sweeper")
root.resizable(False, False)

top_frame = Frame(

    root,
    bg='black',  # to be changed back to Black
    width=1440,
    height=util.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
        top_frame,
        bg='black',
        fg='white',
        text='OlayemiSweeperGame',
        font=('', 20)
)

game_title.place(
    x=util.height_prct(25), y=0
)

left_frame = Frame(
    root,
    bg='black',  # to be changed back to Black
    width=360,
    height=540
)
left_frame.place(x=0, y=180)

center_frame = Frame(

        root,
        bg='black',
        width=util.width_prct(75),
        height=util.height_prct(75)
)
center_frame.place(
    x=util.width_prct(25),
    y=util.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_objects(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# call the label obj from cell
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0,
    y=0
)
Cell.randomized_mine()

# Run the window
root.mainloop()
