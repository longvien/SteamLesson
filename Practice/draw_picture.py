from turtle import *

drawing_area = Screen()
drawing_area.setup(width=750, height=500)

shape('square')
for i in range(75):
    right(21 + i)
    forward(2 + (i * 5))
    right(41 + i)

done()