from tkinter import *
import tkinter.messagebox as msg
from matplotlib import image
import pyqrcode
import png
from pyqrcode import QRCode
import tkinter.ttk as ttk

root = Tk()
root.geometry("1200x700")
root.resizable(False,False)
root.configure(bg="#EAF0F2")

global links
global color_var
global title_var
links = StringVar()
color_var = StringVar()
title_var = StringVar()


###################colors####################
Blue = [ 11, 183, 211]
green = [108, 211, 11]
black = [133, 137, 139]
red = [211, 71, 11]
cyan = [11, 150, 211]

color_t = (Blue,green,black,red,cyan)
# print(color_t[1])


def reset():
    links.set("")
    color_var.set("Select BG Color")
    title_var.set("")
    img_view.config(image="")



def create():

    # new_l = links.get()
    # url = pyqrcode.create(new_l, error='H',version=20,mode='binary')
    # url.png('new.png', scale = 3)
    
    if color_var.get() == "Blue":
        name_ent = title_var.get()
        new_l = links.get()
        url = pyqrcode.create(new_l,error='H',version=20,mode='binary')
        url.png(f"{name_ent}.png", scale=4,module_color=(color_t[0]),background=[255, 255, 255])
        msg.showinfo("Exito", f"{name_ent} Tu Codigo QR fue creado!")

        global Image
        Image = PhotoImage(file= f"{name_ent}.png")
        img_view.config(image=Image)
        
    
    elif color_var.get() =="green":
        name_ent = title_var.get()
        new_l = links.get()
        url = pyqrcode.create(new_l,error='H',version=20,mode='binary')
        url.png(f"{name_ent}.png", scale=4,module_color=(color_t[1]),background=[255, 255, 255])
        msg.showinfo("Exito", f"{name_ent} Tu Codigo QR fue creado!")

        Image = PhotoImage(file= f"{name_ent}.png")
        img_view.config(image=Image)

    
    elif color_var.get() =="black":
        name_ent = title_var.get()
        new_l = links.get()
        url = pyqrcode.create(new_l,error='H',version=20,mode='binary')
        url.png(f"{name_ent}.png", scale=4,module_color=(color_t[2]),background=[255, 255, 255])
        msg.showinfo("Exito", f"{name_ent} Tu Codigo QR fue creado!")

        Image = PhotoImage(file= f"{name_ent}.png")
        img_view.config(image=Image)

    elif color_var.get() =="red":
        name_ent = title_var.get()
        new_l = links.get()
        url = pyqrcode.create(new_l,error='H',version=20,mode='binary')
        url.png(f"{name_ent}.png", scale=4,module_color=(color_t[3]),background=[255, 255, 255])
        msg.showinfo("Exito", f"{name_ent} Tu Codigo QR fue creado!")
   
        Image = PhotoImage(file= f"{name_ent}.png")
        img_view.config(image=Image)
    
    elif color_var.get() =="cyan":
        name_ent = title_var.get()
        new_l = links.get()
        url = pyqrcode.create(new_l,error='H',version=20,mode='binary')
        url.png(f"{name_ent}.png", scale=4,module_color=(color_t[4]),background=[255, 255, 255])
        msg.showinfo("Exito", f"{name_ent} Tu Codigo QR fue creado!")
        
        Image = PhotoImage(file= f"{name_ent}.png")
        img_view.config(image=Image)

    else:
        color_var.get() == "" or title_var.get() == "" or links.get() == ""
        msg.showerror("Error", "Tienes que llenar todos los campos")

            


#################images#################
create_img = PhotoImage(file=r'images\create.png')
reset_img = PhotoImage(file=r'images\reset.png')
################################################################


############## UI Part ###################

frame = Frame(root,bg="#EAF0F2")
frame.place(x = 70, y = 90, height=580, width= 1050)

head_img = Label(root,text="App para crear codigos QR", bg="#EAF0F2",font="Comic-Sans-MS 15 bold")
head_img.place(x = 430, y= 10)


title_lbl = Label(frame,text="Titulo de la imagen",bg="#f2f2f2",fg="#595959",font="Comic-Sans-MS 15 bold")  #Verdana
title_lbl.place(x= 40, y= 40)

title_ent = Entry(frame,textvariable=title_var,bd=0,font="Comic-Sans-MS 12 bold")
title_ent.place(x = 40, y=90, height=30, width=400)

lbl1 = Label(frame,text="URL",bg="#f2f2f2",fg="#595959",font="Comic-Sans-MS 15 bold")  #Verdana
lbl1.place(x= 40, y= 300)

ent = Entry(frame,textvariable=links,bd=0,font="Comic-Sans-MS 12 bold")
ent.place(x = 40, y=360, height=40, width=500)



lbl2 = Label(frame,text="Color del QR",bg="#f2f2f2",fg="#595959",font="Comic-Sans-MS 15 bold")  #Verdana
lbl2.place(x= 40, y= 170)

lbl2_combo = ttk.Combobox(frame,textvariable=color_var,font="Verdana 8 bold", width=18, state="readonly")
lbl2_combo["values"] = ("Selecciona el color", "Blue", "green", "black", "red", "cyan")
lbl2_combo.current(0)
lbl2_combo.place(x = 45, y = 230)


gen_btn = Button(frame,image=create_img,bd=0,command=create)
gen_btn.place(x= 40, y = 450)

reset_btn = Button(frame,image=reset_img,bd=0,command=reset)
reset_btn.place(x= 320, y = 450)


intro = Label(frame,text="~ Creado por Iván Nájera Meléndez ~",bg="#f2f2f2",font="Comic-Sans-MS 9 ")
intro.place(x = 500, y=560)


########## this is for showing qrocode in the box  ##########
img_view = Label(frame)
img_view.pack(padx=50,pady=10,side=RIGHT)



root.mainloop()