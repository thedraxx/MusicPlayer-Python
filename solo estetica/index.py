from tkinter import *

# Elementos Pantalla
ventana = Tk()
ventana.iconbitmap('C:\\Users\\thedr\\OneDrive\\Desktop\\Trabajo Practico Final Tkinter\\assets\\img\\icono.ico')
ventana.resizable(0,0)
imagen = PhotoImage(file="C:\\Users\\thedr\\OneDrive\\Desktop\\Trabajo Practico Final Tkinter\\assets\\img\\portada.png")
imagenLogo = PhotoImage(file="C:\\Users\\thedr\\OneDrive\\Desktop\\Trabajo Practico Final Tkinter\\assets\\img\\headset.png")
Label(ventana, image=imagen).place(x=0, y=0)
Label(ventana, image=imagenLogo).place(x=180, y=120)

barra_menu = Menu(ventana)
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Guida de uso")
barra_menu.add_cascade(label="Como se usa", menu=menu_archivo)
ventana.config(menu=barra_menu)

ventana.title("Reproductor de audio")
ventana.geometry("600x900")
ventana.config(bg="gray", bd=0)
ventana.configure(bg="black")

botonPausa = Button(ventana, text="⏸", bg="white", fg="black", font=("Arial", 20))
botonPausa.place(x=16, y=780)
botonPausa.config(width=8, height=2)

botonPlay = Button(ventana, text="▶️", bg="white", fg="black", font=("Arial", 20))
botonPlay.place(x=150, y=780)
botonPlay.config(width=10, height=2)

botonReplay = Button(ventana, text="↻", bg="white", fg="black", font=("Arial", 20))
botonReplay.place(x=300, y=780)
botonReplay.config(width=10, height=2)

botonAbrir = Button(ventana, text="📁", bg="white", fg="black", font=("Arial", 20))
botonAbrir.place(x=450, y=780)
botonAbrir.config(width=8, height=2)



# Instanciamos
ventana.mainloop()