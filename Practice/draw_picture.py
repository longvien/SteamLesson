from turtle import *

drawing_area = Screen()
drawing_area.setup(width=750, height=500)

shape('square')
for i in range(77):
    right(21 + i)
    forward(7 + (i * 7))
    right(41 + i)

done()