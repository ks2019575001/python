import turtle as t

default_shape = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
user_shape = ["7s0.gif", "7s1.gif", "7s2.gif"]

t.setup(400,400)
t.delay(1000)
for i in range(6):
    t.shape(default_shape[i])
    t.delay(1000)

for j in range(3):
    t.addshape(user_shape[j])
    t.shape(user_shape[j])
    t.delay(1000)

