import os
from tkinter import *
from tkinter import filedialog, ttk
from pygame import mixer
class musica:
    def __init__(self, ventana):
        # Estas variables sirve para controlar la app
        self.repro_musica = False
        self.musica_a_reproducir = ''
        self.nombre_musica = ''

        # Notebook
        barra_menu = Menu(ventana)
        menu_archivo = Menu(barra_menu, tearoff=0)
        menu_archivo.add_command(label="Guida de uso",
                                 command=self.guia_de_uso)
        barra_menu.add_cascade(label="Como se usa", menu=menu_archivo)
        ventana.config(menu=barra_menu)

        # Que esta reproduciendo
        self.ReproduciendoLabel = Label(
            ventana, text="No estas reproduciendo nada", bg="black", fg="white", font=("Arial", 20))
        self.ReproduciendoLabel.config(
            bg="black", fg="white", font=("Arial", 12))
        self.ReproduciendoLabel.config(width=50, height=5, border=0)
        self.ReproduciendoLabel.place(x=77, y=440)

        # Boton Pausa
        self.pause = Button(ventana, text="⏸", bg="white",
                            fg="black", font=("Arial", 20), command=self.pausa)
        self.pause.place(x=16,y=590)
        self.pause.config(width=8, height=2)

        # Boton Reproducir
        self.play = Button(ventana, text="▶️", bg="white", fg="black", font=(
            "Arial", 20), command=self.reproducir)
        self.play.place(x=150,y=590)
        self.play.config(width=10, height=2)

    # Boton Reiniciar
        self.reset = Button(ventana, text="↻", bg="white",
                            fg="black", font=("Arial", 20), command=self.reset)
        self.reset.place(x=300,y=590)
        self.reset.config(width=10, height=2)

    # Boton Abrir
        self.open = Button(ventana, text="📁", bg="white",
                           fg="black", font=("Arial", 20), command=self.abrir)
        self.open.place(x=450,y=590)
        self.open.config(width=8, height=2)

    # Funciones
   # Abrir archivo
    def abrir(self):
        self.musica_a_reproducir = filedialog.askopenfilename()
        # lo guarda en una variable
        self.nombre_musica = os.path.basename(self.musica_a_reproducir)
        #   Muestra que estas reproduciendo
        self.ReproduciendoLabel = Label(
            ventana, text=self.nombre_musica, bg="black", fg="white", font=("Arial", 20))
        self.ReproduciendoLabel.config(
            bg="black", fg="white", font=("Arial", 12))
        self.ReproduciendoLabel.config(width=50, height=5, border=0)
        self.ReproduciendoLabel.place(x=77, y=440)

     # Esta funcion reproduce la cancion
    def reproducir(self):
            mixer.init()
            mixer.music.load(self.musica_a_reproducir)
            mixer.music.play()
            self.play["state"] = DISABLED
            self.repro_musica = True

    # Esta funcion Pausa la cancion
    def pausa(self):
        # Si esta repro_musica es true quiere decir que esta reproduciendo
        if self.repro_musica:
            mixer.music.pause()
            self.repro_musica = False
            self.pause.config(text="▶️")
        # Si esta repro_musica es false quiere decir que esta pausada
        else:
            mixer.music.unpause()
            self.repro_musica = True
            self.pause.config(text="⏸")

    # Reinicia la cancion
    def reset(self):
        mixer.music.stop()
        mixer.music.load(self.musica_a_reproducir)
        mixer.music.play()
        # Volvemos a poner repro_musica en true para que se pueda pausar
        self.repro_musica = True

    def guia_de_uso(self):
        ventana_secundaria = Toplevel()
        ventana_secundaria.title("Guia de uso")
        ventana_secundaria.geometry("200x200")
        ventana_secundaria.resizable(0, 0)
        etiqueta = Label(
            ventana_secundaria, text="1. Abre la cancion \n  2.haz click en reproducir \n 3. Pausa la cancion \n 4. Reinicia la cancion")
        etiqueta.pack()
        ventana_secundaria.config(width=300, height=200)
        boton_cerrar = ttk.Button(
            ventana_secundaria,
            text="cerrar",
            command=ventana_secundaria.destroy
        )
        boton_cerrar.place(x=60, y=85)

# Elementos Pantalla
ventana = Tk()
ventana.iconbitmap(
    '.\\assets\\img\\icono.ico')
ventana.resizable(0, 0)
imagen = PhotoImage(
    file=".\\assets\\img\\portada.png")

imagenLogo = PhotoImage(
    file=".\\assets\\img\\headset.png")
Label(ventana, image=imagen).place(x=0, y=0)
Label(ventana, image=imagenLogo).place(x=180, y=120)

# Titulo de la ventana
ventana.title('Reproductor de Audio')
ventana.geometry("600x700")
ventana.config(bg="gray", bd=0)
ventana.configure(bg="black")

# Instanciamos
musica(ventana)
ventana.mainloop()
