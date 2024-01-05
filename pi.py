import turtle
import sys
import random
sys.setExecutionLimit(1000000) 

#change the coordinates of the screen so that all x and y coordinates are between -1 and 1
win = turtle.Screen()
win.setworldcoordinates(-1,-1,1,1)

dart = turtle.Turtle()
dart.tracer(12,25) #speeds up animation with skips=12 and pause=25
dart.up()

total_darts = 10000
dart_red = 0
dart_blue = 0

for _ in range(total_darts):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 <= 1:
        dart.color("red")
        dart.goto(x, y)
        dart.stamp()
        dart_red += 1
     
    else:
        dart.color("blue")
        dart.goto(x, y)
        dart.stamp()
        dart_blue += 1

area_square = 2 * 2

approx_pi = (dart_red / total_darts) * area_square

print(f"The approximate value of pi is {approx_pi}.")


dart.update() #draws any operations that are skipped at the end
