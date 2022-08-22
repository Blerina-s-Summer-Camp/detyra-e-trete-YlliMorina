import turtle

# Pjesa e kodit me turtle librarine
trendafili1 = turtle.Turtle()
trendafili1.pencolor("red")

trendafili2 = turtle.Turtle()
trendafili2.pencolor("red")

for i in range(20):
   trendafili1.forward(i*4)
   trendafili1.right(110)
   trendafili1.left(0)

for i in range(20):
   trendafili2.forward(i*1)
   trendafili2.right(110)
   trendafili2.left(0)
