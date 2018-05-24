from tkinter import *
import vlc
p = vlc.MediaPlayer("fut.mp3")
p.play()
tk=Tk()
canvas=Canvas(tk,width=600,height=400)
canvas.pack()
def movefig(event):
    if event.keysym=='Up':
        canvas.move(2,0,-5)
    elif event.keysym=='Down':
        canvas.move(2, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(2, -5, 0)
    elif event.keysym == 'Right':
        canvas.move(2, 5, 0)
arco=PhotoImage(file='arco.png')
canvas.create_image(0,100,anchor=NW,image=arco)
x,y=400,150
ball=PhotoImage(file='ball.gif')
canvas.create_image(x,y,anchor=NW,image=ball)
canvas.bind_all('<KeyPress-Up>', movefig)
canvas.bind_all('<KeyPress-Down>', movefig)
canvas.bind_all('<KeyPress-Left>', movefig)
canvas.bind_all('<KeyPress-Right>', movefig)
canvas.create_text(80,10,text='Coordenadas: '+)
tk.mainloop()