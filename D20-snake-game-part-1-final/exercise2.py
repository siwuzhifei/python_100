import turtle

# loop for motion with
# default tracer as 1
for i in range(20):
    turtle.forward(1 + 1 * i)
    turtle.right(45)
turtle.tracer(n=1, delay=5)

# loop for motion with
# above tracer values
for i in range(20, 40):
    turtle.forward(1 + 1 * i)
    turtle.right(45)
turtle.tracer(n=1, delay=10)

for i in range(40, 120):
    turtle.forward(1 + 1 * i)
    turtle.right(45)