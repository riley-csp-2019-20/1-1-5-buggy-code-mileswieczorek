#   a115_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
# create spider head + body
spider.pensize(40)
spider.circle(20)
# configure spider legs
legs = 8
length_legs = 80
spider_angle = 270 / legs  
spider.pensize(5)
legs_loop = 0
# draw spider legs
while (legs_loop < legs):
  spider.goto(0,20)
  spider.setheading(spider_angle*legs_loop - 180)
  spider.setheading(spider_angle*legs_loop + 180)
  spider.forward(length_legs)
  legs_loop = legs_loop + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()