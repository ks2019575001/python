import turtle as t
t.shape("turtle")

def left():
    t.setheading(90)
    t.forward(100)
def right():
    t.setheading(0)
    t.forward(100)
def up():
    t.setheading(270)
    t.forward(100)
def down():
    t.setheading(180)
    t.forward(100)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s = t.Screen()

s.onkeypress(left, "Left")
s.onkeypress(right, "Right")
s.onkeypress(up, "Up")
s.onkeypress(down, "Down")
s.onkeypress(clear, "r")
s.listen()
