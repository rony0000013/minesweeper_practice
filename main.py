from tkinter import *
import settings
import utils
import cell


root = Tk()
#Override settings of the window 
root.configure(bg = "black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper Game")
root.resizable(False,False)

top_frame = Frame(root , bg = "Black",
    width = utils.width_prct(100) , 
    height = utils.height_prct(25))
top_frame.place(x=0, y=0)

game_title = Label(top_frame,bg = "Black",fg = "Yellow",text = "Minesweeper Game",font =("",48))
game_title.place(x=utils.width_prct(25),y=0)

left_frame = Frame(root, bg = "Black",
    width = utils.width_prct(25),
    height = utils.height_prct(75))
left_frame.place(x=0, y=utils.height_prct(25))

centre_frame = Frame(root, bg = "Black",
    width = utils.width_prct(75),
    height = utils.height_prct(75))
centre_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

""" How cell opperates
c1 = cell.Cell()
c1.create_btn_obj(centre_frame)
c1.cell_btn_obj.grid(column=0 , row=0 )
"""

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = cell.Cell(x,y)
        c.create_btn_obj(centre_frame)
        c.cell_btn_obj.grid(column=x,row=y)


#Call the label from the Cell class
cell.Cell.create_cell_count_label(left_frame)
cell.Cell.cell_count_label_obj.place(x=30 , y=0)

cell.Cell.randomize_mines()



#Run the Window
root.mainloop()