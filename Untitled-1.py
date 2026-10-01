from tkinter import *
from PIL import  Image,ImageTk
t=Tk()
e=Image.open("i.png").convert('RGBA')
f=Image.new("RGBA",e.size,"hotpink")
u=Image.alpha_composite(f,e)
e=ImageTk.PhotoImage(u)
Label(t,image=e).pack() 
t.overrideredirect(True)
t.attributes("-transparentcolor", "hotpink")
t.config(bg="hotpink")
t.attributes('-alpha')
t.attributes('-topmost', True)
y=[False,False]
def f(i,l):
    p=f'200x282+{str(i)}+{str(l)}'
    t.geometry(p)
    if y[0] :
        y[0]=True
        i-=1
    if not y[0]:
        i+=1
    if y[1]:
        y[1]=True
        l-=1
    if not y[1]:
        l+=1 
    if i<=0:y[0]=False
    if l<=0:y[1]=False 
    if i>1300:y[0]=True
    if l>600:y[1]=True
    t.after(1,f,i,l)
t.after(1,f,0,0)
mainloop()