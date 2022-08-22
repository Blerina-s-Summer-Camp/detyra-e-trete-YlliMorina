import turtle
#Ushtrimi i tretë
ylli = turtle.Turtle()
ylli.pencolor("blue")

katror = turtle.Turtle()
katror.pencolor("red")


for i in range(20):
  ylli.forward(i * 2)
  ylli.right(144)
    

for i in range(20):
   katror.forward(i*2)
   katror.right(90)


trekendesh = turtle.Turtle()
trekendesh.pencolor("brown")


for i in range(30):
   trekendesh.forward(i*8)
   trekendesh.left(120)
   