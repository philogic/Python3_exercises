import tst
tst.canvas.create_polygon(10, 10, 10, 60, 50, 35)
def movetriangle(event):
    if event.keysym == 'Up':
        tst.canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        tst.canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        tst.canvas.move(1, -3, 0)
    else:
        tst.canvas.move(1, 3, 0)
tst.canvas.bind_all('<KeyPress-Up>', movetriangle)
tst.canvas.bind_all('<KeyPress-Down>', movetriangle)
tst.canvas.bind_all('<KeyPress-Left>', movetriangle)
tst.canvas.bind_all('<KeyPress-Right>', movetriangle)



    
    

    
