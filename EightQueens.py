from tkinter import *
from PIL import Image,ImageTk
import random
import time
class Board:
    def __init__(self,size):
        self.board=[] #אתחול לוח לפי גודל מסוים
        for i in range(size):
            self.board.append([])
            for j in range(size):
                self.board[i].append(0)
        self.size=size
        self.rows=[]
        self.cols=[]
        for i in range(self.size):
            self.rows.append(True)
            self.cols.append(True)

    def get_board(self):
        return self.board

    def check_possible(self,row,col): #פעולה שבודקת עבור קואורדינטות מסוימות האם אפשרי לשים שם מלכה

        for i in range(self.size):  #בדיקת השורה
            if self.board[i][col] == 1:
                return False

        for i in range(self.size): #בדיקת התור
            if self.board[row][i] == 1:
                return False

        for i in range(self.size):  #בדיקת האלכסונים
            for j in range(self.size):
                if self.board[i][j] == 1:
                    if abs(i - row) == abs(j - col):
                        return False
        return True

    def check_n_queens(self): #פעולה שבודקת האם כל המלכות האפשריות הונחו על הלוח
        self.count=0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j]==1:
                    self.count+=1
        return self.count==self.size

    def solve_board(self):
        for row in range(self.size): #עובר על כל הלוח
                for col in range(self.size):
                    if self.board[row][col] == 0: #אם המקום פנוי
                        if self.check_possible(row, col): #אם אפשרי לשים במיקום הנוכחי מלכה
                            self.board[row][col] = 1  #אם אפשרי הספרה 1 מייצגת מלכה
                            self.solve_board() #המשך פתירה
                            if self.check_n_queens():  # אם יש n מלכות על המסך
                                return True#סיום הרצף
                            self.board[row][col] = 0 #אם אין n מלכות התוכנית ממשיכה


class Game:
    def __init__(self,root):
        self.opening_setup() #איתחול מסך הפתיחה

    def new_game(self): #אפשרות למשחק חדש
        if self.size>=4:
            for i in range(self.size):
                for j in range(self.size):
                    self.arr[i][j].grid_forget()
        self.again.grid_forget()
        if self.size<4:
            self.error.grid_forget()
        self.opening_setup()

    def opening_setup(self):
        root.config(bg='black')
        self.opening_label=Label(root,text="Welcome to the n queens problem!"+'\n'+"Please enter number of queens: ",font='Times 24',fg='gold',bg='black')
        self.opening_label.grid(row=0,column=0)
        self.qnum=Entry(root)
        self.qnum.insert(END,'8')
        self.qnum.grid(row=4,column=0)
        self.solve=Button(root,text="Solve",bg='black',font='Times 14',fg='gold',command=self.start_game)
        self.solve.grid(row=5,column=0)

    def open_image(self, name):  # פעולה שפותחת תמונה
        card_pic = Image.open(name)
        card_pic.thumbnail((100, 100))
        card_pic = ImageTk.PhotoImage(card_pic)
        return card_pic

    def print_board(self, temp): #פעולה שבונה לוח שחמט גרפי ומלכות לפי המספר
        if self.size<4:
            self.error=Label(root,text="There is no possible solution!")
            self.error.grid(row=self.size+1,column=self.size+2)
            return
        self.b = temp
        self.arr=[]
        self.check = 0
        data_folder = 'queen2.jpg'
        self.img = self.open_image(data_folder)
        for i in range(self.size):
            self.arr.append([])
            if self.size % 2 == 0:
                self.check += 1
            for j in range(self.size):
                if self.check % 2 == 0:
                    bg = 'sienna'
                else:
                    bg = 'black'


                temp = Label(root, bg=bg)
                temp.config(height=5, width=10)
                temp.grid(row=i, column=j)
                self.arr[i].append(temp)
                self.check += 1
        for i in range(self.size):
            for j in range(self.size):
                if self.b[i][j] == 1:
                    temp = Label(root, image=self.img)
                    temp.grid(row=i,column=j)
                    self.arr[i][j].grid_forget()
                    self.arr[i][j]=temp

                    time.sleep(1)
                    root.update()



    def start_game(self): #הפעולה מתחילה את המשחק
        self.opening_label.grid_forget()
        self.qnum.grid_forget()
        self.solve.grid_forget()
        self.size=int(self.qnum.get())
        root.config(bg='white')
        b=Board(self.size)
        b.solve_board()
        temp=b.get_board()
        self.print_board(temp)
        self.again=Button(root,text="Solve Again",command=self.new_game)
        self.again.grid(row=self.size+2,column=self.size+2)
root=Tk()
root.geometry('1000x1000')
root.config(bg='black')
Game(root)
root.mainloop()








