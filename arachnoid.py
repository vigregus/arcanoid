#! /usr/bin/python3
from tkinter import *
import time
import random
from random import randint
ball_count = 5s0
ball_array = []
block_array = []
heightWindow = 400
widthWindow = 900
positionX = []
positionY = []
color_array = ['red','Blue','green','white','orange','black','brown','yellow','purple','gray','pink']

tk = Tk()
tk.title('Game')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk, width=widthWindow, height=heightWindow, highlightthickness=0)
canvas.pack()




tk.update()

class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        random.shuffle(color_array)
        self.id = canvas.create_oval(10,10,25,25,fill=color_array[0])
        positionX = [randint(0,widthWindow-30) for x in range(ball_count)]
        positionY = [randint(0,heightWindow-30) for x in range(ball_count)]
        random.shuffle(positionX)
        random.shuffle(positionY)
        self.canvas.move(self.id,positionX[0],positionY[0])
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        direction = [-2,2]
        random.shuffle(direction)
        self.y = direction[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:

            # задаём падение на следующем шаге = 2

            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(250, 120, text='You lose', font=('Courier',30), fill='red')
        if self.hit_paddle(pos) == True:
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2

class Paddle:
    def __init__(self, canvas, color):
    	self.canvas = canvas
    	self.id = canvas.create_rectangle(0,0,widthWindow,10,fill=color)
    	#start_1 = [40,60,90,120,150,180,200]
    	start_1 = [0,0]
    	random.shuffle(start_1)
    	self.starting_point_x = start_1[0]
    	self.canvas.move(self.id, self.starting_point_x, 390)
    	self.x = 0
    	self.canvas_width = self.canvas.winfo_width()
    	self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    	self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
    	self.started = False
    	self.canvas.bind_all('<KeyPress-Return>',self.start_game)
#        self.canvas.bind_all('<Escape>', exit)

    def turn_right(self, event):
        self.x = 2

    def turn_left(self, event):
        self.x = -2

    def start_game(self, event):
        self.started = True

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >=self.canvas_width:
            self.x = 0

class Score:
    def __init__(self,canvas,color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(widthWindow-50,10,text=self.score,font=('Courier',15),fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id,text=self.score)

class Block:
    def __init__(self,canvas,posX,posY):
        random.shuffle(color_array)
        self.canvas = canvas
        self.id = canvas.create_rectangle(posX,posY,20,10,fill=color_array[0])

score = Score(canvas,'green')
paddle = Paddle(canvas, 'Black')

for i in range(ball_count):
    ball_array.append(Ball(canvas,paddle, score, 'blue'))


while not ball_array[1].hit_bottom :
    if paddle.started == True:
        for i in range(ball_count):
            ball_array[i].draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    #time.sleep(0.01)
#time.sleep(1)
