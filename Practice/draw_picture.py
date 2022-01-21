from turtle import *

drawing_area = Screen()
drawing_area.setup(width=750, height=500)

shape('square')
for i in range(75):
    right(21 + i)
    forward(1 + (i * 5))
    right(40 + i)

done()