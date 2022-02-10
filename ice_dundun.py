
import turtle
import glob
from PIL import Image
import os
import sys
import subprocess
import tkinter as _
_.ROUND = _.BUTT

def gray_white_style():
    turtle.pensize(3)
    turtle.pencolor("lightgray")
    turtle.fillcolor("white")


def skip(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def right_hand(x, y):
    skip(x, y)
    gray_white_style()
    turtle.begin_fill()
    turtle.setheading(76)
    turtle.fd(5)
    turtle.circle(-40, extent=120)
    turtle.circle(-50, extent=30)
    turtle.circle(-40, extent=20)
    turtle.circle(-100, extent=30)
    turtle.circle(-150, extent=30)
    turtle.circle(-200, extent=5)
    turtle.end_fill()
    # inner
    skip(x, y - 12)
    turtle.color("black")
    turtle.begin_fill()
    turtle.setheading(73)
    turtle.fd(3)
    turtle.circle(-40, extent=100)
    turtle.circle(-30, extent=70)
    turtle.circle(-50, extent=10)
    turtle.circle(-100, extent=20)
    turtle.circle(-150, extent=25)
    turtle.circle(-200, extent=5)
    turtle.end_fill()

    

def white_body(x, y):
    skip(x, y)
    gray_white_style()
    turtle.begin_fill()
    turtle.setheading(56)
    turtle.circle(50, extent=190)
    turtle.setheading(156)
    turtle.circle(200, extent=50)
    turtle.setheading(126)
    turtle.circle(50, extent=190)
    turtle.setheading(-128)
    turtle.circle(300, extent=80)
    turtle.circle(-60, extent=50)
    turtle.fd(50)
    turtle.circle(20, extent=70)
    turtle.circle(100, extent=10)
    turtle.circle(50, extent=5)
    turtle.circle(100, extent=5)
    turtle.circle(500, extent=5)
    turtle.circle(50, extent=50)
    turtle.circle(10, extent=45)
    turtle.circle(100, extent=10)
    turtle.circle(-30, extent=45)
    turtle.circle(-6, extent=58)
    turtle.fd(60)
    turtle.circle(-6, extent=58)
    turtle.circle(-30, extent=45)
    turtle.circle(100, extent=10)
    turtle.circle(10, extent=45)
    turtle.circle(50, extent=50)
    turtle.circle(300, extent=10)
    turtle.fd(5)
    turtle.circle(50, extent=5)
    turtle.circle(20, extent=85)
    turtle.fd(70)
    turtle.circle(-70, extent=45)
    turtle.circle(350, extent=68)
    turtle.end_fill()

def black_left_ear(x, y):
    skip(x-8, y+5)
    turtle.color("black")
    turtle.setheading(56)
    turtle.begin_fill()
    turtle.circle(40, extent=190)
    turtle.setheading(-20)
    turtle.circle(-280, extent=16)
    turtle.end_fill()

def black_right_ear(x, y):
    skip(x-263, y+40)
    turtle.setheading(126)
    turtle.begin_fill()
    turtle.circle(40, extent=190)
    turtle.setheading(48)
    turtle.circle(-280, extent=16)
    turtle.end_fill()

def black_left_leg(x, y):
    skip(x-295, y-430)
    turtle.setheading(-10)
    turtle.begin_fill()
    turtle.circle(-240, extent=26)
    turtle.setheading(-110)
    turtle.circle(60, extent=40)
    turtle.circle(-10, extent=90)
    turtle.circle(-110, extent=50)
    turtle.circle(-10, extent=70)
    turtle.fd(30)
    turtle.circle(100, extent=28)
    turtle.end_fill()

def black_right_leg(x, y):
    skip(x-18, y-430)
    turtle.setheading(-100)
    turtle.begin_fill()
    turtle.circle(40, extent=26)
    turtle.fd(50)
    turtle.circle(-30, extent=60)
    turtle.circle(-10, extent=20)
    turtle.circle(-70, extent=20)
    turtle.fd(30)
    turtle.circle(-30, extent=120)
    turtle.circle(20, extent=55)
    turtle.setheading(40)
    turtle.circle(-260, extent=20)
    turtle.end_fill()
   
def body(x, y):
    white_body(x, y)
    black_left_ear(x, y)
    black_right_ear(x, y)
    black_right_leg(x, y)
    black_left_leg(x, y)

def left_hand(x, y):
    skip(x, y)
    turtle.setheading(-136)
    gray_white_style()
    turtle.begin_fill()
    turtle.circle(300, 25)
    turtle.circle(50, 160)
    turtle.circle(20, 50)
    turtle.circle(-20, 60)
    turtle.end_fill()
    # inner
    skip(x, y - 15)
    turtle.begin_fill()
    turtle.color("black")
    turtle.setheading(-136)
    turtle.circle(280, 22)
    turtle.circle(40, 160)
    turtle.circle(20, 50)
    turtle.circle(-20, 60)
    turtle.end_fill()

def blue_face(x, y):
    # blue
    skip(x, y)
    turtle.setheading(-90)
    turtle.color("lightblue")
    turtle.circle(-100, 60)
    turtle.circle(-300, 60)
    turtle.circle(-100, 80)
    turtle.circle(-200, 70)
    turtle.circle(-210, 79)

def purple_face(x, y):
    skip(x-8, y)
    turtle.setheading(-90)
    turtle.color("purple")
    turtle.circle(-95, 60)
    turtle.circle(-290, 60)
    turtle.circle(-95, 60)
    turtle.circle(-100, 25)
    turtle.circle(-200, 70)
    turtle.circle(-210, 10)
    turtle.circle(-194, 65)

def red_face(x, y):
    # red
    skip(x-16, y)
    turtle.setheading(-90)
    turtle.color("red")
    turtle.circle(-90, 60)
    turtle.circle(-275, 60)
    turtle.circle(-95, 90)
    turtle.circle(-200, 60)
    turtle.circle(-100, 5)
    turtle.circle(-200, 60)
    turtle.circle(-100, 20)

def yellow_face(x, y):
    skip(x-24, y)
    turtle.setheading(-90)
    turtle.color("yellow")
    turtle.circle(-85, 60)
    turtle.circle(-265, 60)
    turtle.circle(-90, 90)
    turtle.circle(-190, 60)
    turtle.circle(-100, 5)
    turtle.circle(-200, 50)
    turtle.circle(-120, 40)

def green_face(x, y):
    skip(x-32, y)
    turtle.setheading(-90)
    turtle.color("lightgreen")
    turtle.circle(-75, 60)
    turtle.circle(-260, 60)
    turtle.circle(-77, 90)
    turtle.circle(-190, 60)
    turtle.circle(-100, 5)
    turtle.circle(-180, 50)
    turtle.circle(-127, 27)


def face(x, y):
    turtle.pensize(5)
    blue_face(x, y)
    purple_face(x, y)
    red_face(x, y)
    yellow_face(x, y)
    green_face(x, y)

def undo(n=1):
    for i in range(n):
        turtle.undo()
        
def nose(x, y):
    skip(x, y)
    turtle.pensize(1)
    turtle.color("black")
    turtle.begin_fill()
    turtle.setheading(-35)
    turtle.circle(10, 80)
    turtle.fd(10)
    turtle.circle(5, 135)
    turtle.fd(25)
    turtle.circle(5, 135)
    turtle.circle(45, 20)
    turtle.end_fill()
    
def right_eye(x, y):
    eye_color="#00997a"
    # glasses
    skip(x + 30, y + 30)
    turtle.setheading(90)
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(-38, 120)
    turtle.circle(-100, 60)
    turtle.circle(-25, 100)
    turtle.circle(-100, 50)
    turtle.circle(-75, 25)
    turtle.end_fill()
    # white
    skip(x + 40, y + 20)
    turtle.color("white")
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.circle(-27)
    turtle.end_fill()
    # blue
    skip(x + 45, y + 20)
    turtle.color(eye_color)
    turtle.begin_fill()
    turtle.circle(-21)
    turtle.end_fill()
    # black
    skip(x + 58, y + 18)
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(-10)
    turtle.end_fill()
    # white
    skip(x + 65, y + 32)
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(-5)
    turtle.end_fill()
    
def left_eye(x, y):
    # glasses
    eye_color="#00997a"
    skip(x - 30, y + 30)
    turtle.setheading(90)
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(38, 120)
    turtle.circle(100, 60)
    turtle.circle(25, 100)
    turtle.circle(100, 50)
    turtle.circle(75, 25)
    turtle.end_fill()
    # white
    skip(x - 40, y + 20)
    turtle.color("white")
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.circle(27)
    turtle.end_fill()
    # blue
    skip(x - 45, y + 20)
    turtle.color(eye_color)
    turtle.begin_fill()
    turtle.circle(21)
    turtle.end_fill()
    # black
    skip(x - 58, y + 18)
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    # white
    skip(x - 65, y + 32)
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()


def mouth(x, y):
    skip(x+30, y-8)
    turtle.color("black")
    turtle.begin_fill()
    turtle.setheading(-120)
    turtle.circle(-35, 120)
    turtle.setheading(-62) 
    turtle.fd(5)
    turtle.circle(33, 140)
    turtle.end_fill()

def nose_eye_mouth(x, y):
    nose(x, y)
    right_eye(x, y)
    left_eye(x, y)
    mouth(x, y)

def logo(x, y):
    turtle.pensize(3)
    skip(x, y)
    turtle.setheading(0)
    turtle.color("black")
    turtle.circle(10)
    skip(x + 25, y)
    turtle.color("red")
    turtle.circle(10)
    skip(x - 25, y)
    turtle.color("blue")
    turtle.circle(10)
    skip(x - 12, y-10)
    turtle.color("yellow")
    turtle.circle(10)
    skip(x + 12, y-10)
    turtle.color("green")
    turtle.circle(10)
    turtle.color("black")
    skip(x, y+30)
    turtle.write("BEIJING 2022", font=('Arail', 18, "italic"), align="center")

def heart(x, y):
    skip(x, y)
    turtle.color("red")
    turtle.begin_fill()
    turtle.setheading(6)
    turtle.circle(100, 10)
    turtle.circle(8, 180)
    turtle.fd(2)
    turtle.setheading(100)
    turtle.fd(2)
    turtle.circle(8, 180)
    turtle.circle(100, 10)
    turtle.end_fill()
    turtle.penup()
    turtle.hideturtle()

frames_per_second = 10
running = True

def stop():
    global running
    running = False

def save_eps(counter=[1]):
    turtle.getcanvas().postscript(file="ice_dundun{0:03d}.eps".format(counter[0]))
    counter[0] += 1
    if running:
        
        turtle.ontimer(save_eps, int(1000 / frames_per_second))
    else:
        print("not running")
        eps2gif()
        print("over to gif")
        sys.exit()

def draw():
    turtle.reset()
    turtle.hideturtle()
    turtle.screensize(canvwidth=500, canvheight=600, bg="white")
    turtle.title("ice dun dun by Olivia ~~~")
    turtle.speed(110)
    right_hand(200, 97)
    left_hand(-250, 40)
    body(145, 220)
    face(185, 55)
    nose_eye_mouth(-10, 55)
    logo(-0, -170)
    heart(225, 60)
    turtle.ontimer(stop, 500)

def eps2gif(input_name="ice_dundun*.eps", output_name="ice_dundun.gif"):
    print("start to gif")
    pwd = subprocess.run("pwd", stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
    input_files = os.path.join(pwd, input_name)
    frames = [Image.open(image) for image in glob.glob(input_files)]
    frames.sort(key=lambda x : x.filename)
    frame_one = frames[0]
    print(f"frames{[fn.filename for fn in frames]}")
    frame_one.save(output_name, format="GIF", append_images=frames,save_all=True, duration=100, loop=0)
    print("over to gif")
    [subprocess.run(["rm", f"{fn.filename}"]) for fn in frames]
    print("rm eps...")
    

if __name__ == "__main__":
    print("start save")
    save_eps()
    print("end save")
    turtle.ontimer(draw, 500)
    print("...")
    turtle.done()
    print("done")
    #turtle.mainloop()


