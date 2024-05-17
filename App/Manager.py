#este codigo es mi host por asi decirlo es el padre el mero mero pues
import tkinter as tk
from constantes import style #<--- esto toma lo que ya tenia en el otro codigo, segun youtube se llama herencia
from screens import Home, Game, Cotizacion#<-- lo mismo que el otro pero en con las pantallas

#esta es una clase para que no me pierda
class Manager(tk.Tk):
    #aqui lo que hace es pura herencia y no tener que definir de uno en uno
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        #esto ya es aparte pero en si mas de lo  mismo de definir
        self.title("App: Vacaciones")
        container = tk.Frame(self) #fram es el pedacito donde digo que quiero poner
        self.mode = "ubicacion3" #esta cosa esta en nuestro screen ahi esta definida
        self.plan_a = "plan_1"
        container.pack( #el .pack lo que hace es transformarlo y enseñarlo en pantalla
            side = tk.TOP, #side es la ubicacion
            fill = tk.BOTH, #esta madre lo que hace es que me rellena todo el fondo soy flojo
            expand = True # la misma wea pero con todo
        )
        container.configure(background = style.BACKGROUND)#aqui llamo a la funcion de color
        container.grid_columnconfigure(0, weight=1)# esto es para acomodar
        container.grid_rowconfigure(0, weight=1)# lo mismo pero con row
        
        self.frames = {} 
        #segun el del video esto es un diccionario de clase
        for F in (Home, Game, Cotizacion):#tecnicamente solo hereda lo que hago en las que estas en parentesis
            frame = F(container,self)#aqui le pido que me maneje frame como mi base
            self.frames[F]= frame#pido que lo llame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)#esto es para el acomodo de manera automatica
        self.show_frame(Home)
    #pues este se encarga de leer los frames        
    def show_frame(self, container):
        frame = self.frames[container] #esto lee el frame que tenemos seleccionado la ubicacion
        frame.tkraise() #esto lo que hace es ponerlo hasta adelante
        