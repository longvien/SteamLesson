from turtle import *

drawing_area = Screen()
drawing_area.setup(width=750, height=500)

shape('square')
for i in range(76):
    right(21 + i)
    forward(3 + (i * 5))
    right(41 + i)

done()