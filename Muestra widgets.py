from tkinter import *
from tkinter import ttk

raiz=Tk()
self=Tk
raiz.title("Inicio de Sesion")

self.Nombre="Ivan"
self.Contraseña="123"

Frame1=ttk.Frame(raiz)

Frame1 = ttk.Frame(raiz, relief="raised",padding="3 3 12 12")
Frame1.grid(column=0, row=0) 
usuarioEntry=ttk.Entry(Frame1,width=30,textvariable=self.Nombre)
usuarioEntry.grid(column=1, row=0)

ttk.Label(Frame1,text="Nombre").grid(column=0,row=0)
usuarioEntry=ttk.Entry(Frame1, width=30, textvariable=self.Nombre)
usuarioEntry.grid(column=1, row=3)
ttk.Label(Frame1,textvariable=self.Contraseña).grid(column=1,row=1)

ttk.Label(Frame1,text="Apellido P").grid(column=0,row=3)
usuarioEntry=ttk.Entry(Frame1, width=30, textvariable=self.Nombre)
usuarioEntry.grid(column=1, row=3)
ttk.Label(Frame1).grid(column=0,row=4)  

ttk.Label(Frame1,text="Apellido M").grid(column=0,row=5)
usuarioEntry=ttk.Entry(Frame1, width=30, textvariable=self.Nombre)
usuarioEntry.grid(column=1, row=5)


ttk.Label(Frame1,text="Correo").grid(column=0,row=6)
usuarioEntry=ttk.Entry(Frame1, width=30, textvariable=self.Nombre)
usuarioEntry.grid(column=1, row=7)


ttk.Label(Frame1,text="Movil").grid(column=0,row=9)
usuarioEntry=ttk.Entry(Frame1, width=30, textvariable=self.Nombre)
usuarioEntry.grid(column=1, row=11)

frame2=ttk.Frame(raiz)
frame2.grid(column=0,row=8)
ttk.Button(frame2,text="Guardar",command=self.Contraseña).grid(column=1,row=10,sticky=(W)) 
ttk.Button(frame2,text="Cancelar",command=self.Contraseña).grid(column=2,row=10,sticky=(W)) 

frame5=ttk.Frame(raiz,relief="raised",padding="3 3 12 12")
frame5.grid(column=4,row=4)
estado=StringVar()
comboEstados=ttk.Combobox(frame5,textvariable=estado)
comboEstados.grid()
comboEstados["values"]=("Estados(32)")


frame3=ttk.Frame(raiz)
frame3.grid(column=4,row=0)
home=ttk.Radiobutton(frame3,text="Estudiante").grid(column=0,row=2,sticky=(W))
home=ttk.Radiobutton(frame3,text="Empleado").grid(column=0,row=3,sticky=(W))
home=ttk.Radiobutton(frame3,text="Desempleado").grid(column=0,row=4,sticky=(W))

frame4=ttk.Frame(raiz,relief="raised",padding="3 3 12 12")
frame4.grid(column=0,row=4)
chkBoton=ttk.Checkbutton(frame4,text="Leer").grid(column=1,row=0,sticky=(W))
chkBoton=ttk.Checkbutton(frame4,text="Musica").grid(column=2,row=0,sticky=(W))
chkBoton=ttk.Checkbutton(frame4,text="Videojuegos").grid(column=3,row=0,sticky=(W))




raiz.mainloop()
