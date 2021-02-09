from turtle import*

pu(); ht(); seth(90)
shape('square'); shapesize(1.5)
color('black')
di=90; col=['white','black']

n=16    # use 8 for chess board
m=210
left(90)
forward(m+50)
left(90)
forward(m)
left(180)
for i in range(n):
    for j in range(n):
        fillcolor(col[j%2])
        stamp(); fd(30)
    for k in range(2):
        rt(di); fd(30)
    di=-di

done()
