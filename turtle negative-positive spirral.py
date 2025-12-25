import turtle as t 

screen = t.Screen()
fatih_sultan_mehmet = t.Turtle()

flag = True
r = 0
steps = 0

x,y = screen.screensize()

while flag:
    if t.position()[0] != x and t.position()[1] != y:
        if steps > 8:
            direction = -1
        elif steps == 0:
            direction = 1
        
        if direction == 1:
            try:
                fatih_sultan_mehmet.circle(-r)
                fatih_sultan_mehmet.forward(r / 2)
                t.pencolor(10 / r)
                t.width(r // r + 2)
            except:
                pass

            finally:
                steps += 1
            r += 4

        if direction == -1:
            try:
                fatih_sultan_mehmet.circle(r)
                fatih_sultan_mehmet.forward(-r / 2)
                t.pencolor(10 / r)
                t.width(r // r + 2)

            except:
                pass

            finally:
                steps -= 1

            r -= 4
    else:
        break
    
t.mainloop()
