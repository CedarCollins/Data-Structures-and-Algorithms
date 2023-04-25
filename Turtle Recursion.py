"""
Make sure to enter a number of recursion levels into the given input request.
"""

import turtle

def junction(levels, t, scale):
    if levels >= 1:
        draw(levels - 1, t, scale / 2)
    else:
        t.dot(4)

def draw(levels, t, scale):
    
    t.seth(90)
    t.fd(100 * scale)
    t.seth(0)
    t.fd(100 * scale)

    junction(levels, t, scale)
    t.seth(0)

    t.bk(200 * scale)

    junction(levels, t, scale)
    t.seth(0)

    t.fd(100 * scale)
    t.seth(270)
    t.fd(200 * scale)
    t.seth(180)
    t.fd(100 * scale)
        
    junction(levels, t, scale)
    t.seth(180)
        
    t.bk(200 * scale)

    junction(levels, t, scale)
    t.seth(180)

    t.fd(100 * scale)
    t.seth(90)
    t.fd(100 * scale)

def main():

    wn = turtle.Screen()
    wn.bgcolor('black')
    wn.tracer(False)
    
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color('white')
    t.dot(4)

    levels = int(input('Enter recursion levels: '))
    draw(levels, t, 1)
    
    wn.tracer(True)
    wn.exitonclick()
    print('Click turtle screen to exit...')

if __name__ == "__main__":
    main()
