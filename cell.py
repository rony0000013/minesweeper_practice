from tkinter import Button, Label
import random
import settings
import ctypes
import sys


class Cell:
    all = []
    cell_count_label_obj = None
    cell_count = settings.CELL_COUNT


    def __init__(self,x,y,is_mine = False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.is_opened = False
        self.is_mine_candidate = False
        self.x = x
        self.y = y

        #Append the object to Cell.all list
        Cell.all.append(self)


    def create_btn_obj(self,location):
        btn = Button(location, width = 12, height = 4)

        btn.bind("<Button-1>",self.left_click_actions) # Left click
        btn.bind("<Button-3>",self.right_click_actions) # Right Click
        self.cell_btn_obj = btn


    @staticmethod    
    def create_cell_count_label(location):
        lbl = Label(location, text = f"Cells Left: {Cell.cell_count}",
                    bg="Black",fg="White",font=("",30))
        Cell.cell_count_label_obj = lbl


    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
        if Cell.cell_count == settings.MINES_COUNT:
            ctypes.windll.user32.MessageboxW(0, "Congratulations! You have won the game!","Completed",0)
            sys.exit

        # cancel left nad right click events if cell already opened
        self.cell_btn_obj.unbind("<Button-1>")
        self.cell_btn_obj.unbind("<Button-3>")


    def get_cell_by_axis(self,x,y):
        #  Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y :
                return cell


    @property
    def surrounded_cells(self):
        cells = [self.get_cell_by_axis(self.x -1, self.y -1),
                self.get_cell_by_axis(self.x -1, self.y),
                self.get_cell_by_axis(self.x- 1, self.y +1),
                self.get_cell_by_axis(self.x, self.y -1),
                self.get_cell_by_axis(self.x +1, self.y), 
                self.get_cell_by_axis(self.x +1, self.y +1),
                self.get_cell_by_axis(self.x, self.y +1),
                self.get_cell_by_axis(self.x +1, self.y -1)
                ]
        cells = [cell for cell in cells if cell is not None]
        return cells


    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter


    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_obj.configure(text = self.surrounded_cells_mines_length)        
            #replace the text of cell count label with a new label
            if Cell.cell_count_label_obj:
                Cell.cell_count_label_obj.configure(text = f"Cells Left: {Cell.cell_count}")
            self.cell_btn_obj.configure(bg = "SystemButtonFace")
        #Mark this cell is opned
        self.is_opened = True


    def show_mine(self):         
        self.cell_btn_obj.configure(bg ="Red") 
        ctypes.windll.user32.MessageBoxW(0,"You Clicked on a Mine.","Game Over",0)
        sys.exit()
        # A logic to interrupt the game and display a message that player lost!


    def right_click_actions(self,event):
        if not self.is_mine_candidate:
            self.cell_btn_obj.configure(bg = "Orange")
            self.is_mine_candidate = True
        else:
            self.cell_btn_obj.configure(bg = "SystemButtonFace")
            self.is_mine_candidate = False


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all,settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True


    def __repr__(self):
        return f" Cell({self.x},{self.y}) "


