import turtle
#Ushtrimi i parë dhe i dytë
ylli = turtle.Turtle()
ylli.pencolor("blue")

katror = turtle.Turtle()
katror.pencolor("red")


for i in range(20):
  ylli.forward(i * 8)
  ylli.right(144)
    

for i in range(20):
   katror.forward(i*8)
   katror.right(90)