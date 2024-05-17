#aqui defino mis pantallitas que se mostraran
from tkinter import *
import tkinter as tk
from constantes import style, config #<-- esto toma de mi otro codigo mis especificaciones
#esto va a tener muchos comentarios por que estoy mernso y me pierdo

#esto es mi pantalla principal
class Home(tk.Frame):
    
    def move_to_game(self):#esta  se va a usar mas adelante para cambiar de pagina con un boton
        self.controller.mode = self.gameMode.get()# esto es para que cambie de pantalla,tambien es para que llame en manager
        self.controller.show_frame(Game) # este es para que llame a mi otra clase que es la otra pantalla
    
    #aqui defino lo que hay dentro de mi ventana o frame
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background= style.BACKGROUND)
        self.controller = controller
        self.gameMode = tk.StringVar(self, value="ubicacion3")
        
        self.init_widgets()
        
        #esto es para los frames dentro de la ventana config basica o no?
    def init_widgets(self):
        tk.Label(
            self, 
            text= " App de vacaciones",
            **style.STYLE
            ).pack(
                side = tk.TOP,
                fill = tk.BOTH,
                expand = True,
                padx = 22, #pone los margenes de tolerancia de x
                pady = 11  #pone los margenes de tolerancia de y
            )
            #esto es para un frame dentro de un frame
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background=style.COMPONENT)
        optionsFrame.pack( #hago exactamente lo mismo pero con el otro frame
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )     
        tk.Label(
            optionsFrame, #esto lo pongo como optionframe ya que solo quiero que use nadamas esta
            text=" elige tu lugar a vacacionar Y(>Vo 7)",#que quiero que diga mi frame
            justify= tk.CENTER, #justificar es para que me lo acomode
            **style.STYLE #esto es para que le ponga el estilo que ya habia definido no hay que olvidar el .style para que furule
        ).pack(
            side = tk.TOP,
            fill = tk.X, #aqui nadamas usa el x por que no quiero que se expanda solo quiero que sea a lo largo 
            padx = 22,
            pady = 11
        )
        
        for (key, value) in config.MODES.items(): #esto son para tuplas de mi diccionario
            tk.Radiobutton( 
                # pues en si esto es para edfinir un boton xd
                optionsFrame, #empaquetamos en el frame
                #" v--- esto es ma que nada por cosmetico"
                text = key + ("ᡣ𐭩" if key == "UBICACION3" else ""),
                variable= self.gameMode, 
                #gracias a esta variable nuestro mapeo de este puede ser diferente, se guarda en variable gameMode
                value= value,
                #esto llama a la key de nuestro diccionario
                activebackground = style.BACKGROUND, # personalizar que cuando lo pulse le cambie color
                activeforeground = style.TEXT,
                 **style.STYLE
                ).pack(
                    side = tk.LEFT, # como quiero que esten uno al aldo delotro lo pongo asi
                    fill = tk.BOTH, # un poquito de lo mismo
                    expand = True,
                    padx = 5,
                    pady = 5
                    )
                    #aqui ya empezamos con lo dificil

        tk.Button( #este boton es el que me mueve de lugar de una ventana a otra
                    self,
                text = "Seleccionar >>>",
                command = self.move_to_game, 
                #en python las funciones se pueden usar como objetos por ende este codigo hace eso
                **style.STYLE,
                relief= tk.FLAT, #esto es para que el boton no tenga relieves 
                activebackground = style.BACKGROUND, # un poco de lo mismo
                activeforeground = style.TEXT,
                ).pack(
                    side = tk.TOP,
                    fill = tk.X,
                    padx = 22,
                    pady = 11
                )
        
#esta es otra pantalla dentro de otra pantalla
#tecnicamente lo que hice fue copiar lo de arriba lo modifico para que enseñe lo que quiero

class Game(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background= style.BACKGROUND)
        self.controller = controller
        self.currentOption = tk.StringVar(self, value= "Preparados...<_(°v°;)_>")# esta es la modificacion que agregamos para que actualice lo que queremos ver
        self.ficheros  = None
        self.planMode = tk.StringVar(self, value="plan_1")
        self.init_widgets()   
        
    def move_to_cotizacion(self):#esta  se va a usar mas adelante para cambiar de pagina con un boton
        self.controller.mode = self.planMode.get()# esto es para que cambie de pantalla,tambien es para que llame en manager
        self.controller.show_frame(Cotizacion)

    def update_option(self):
        self.mode = self.controller.mode
        if (self.ficheros == None) or (self.controller.mode.lower() not in self.ficheros.name.lower()):#este es para que se asegure de cual es la variable en la que esta
            self.ficheros = open(f'./App/ficheros/{self.mode}.txt', 'r', encoding="utf-8")
        tmp = self.ficheros.readline()
        if tmp != "":
            self.currentOption.set(tmp)
        else:
            self.currentOption.set("Son todas las opciones volvemos a empezar")
            self.ficheros.close()
            self.ficheros = open(f'./App/ficheros/{self.mode}.txt', 'r', encoding="utf-8")
            #esto es para que se quede guardado lo que hemos hecho de interacciones
            #para abrir correctamente el modo seleccionado
    
        #esto es para los frames dentro de la ventana config basica o no?
    def init_widgets(self):
        tk.Label(
            self, 
            text= " App de vacaciones ...",
            **style.STYLE
            ).pack(
                side = tk.TOP,
                fill = tk.BOTH,
                expand = True,
                padx = 22, #pone los margenes de tolerancia de x
                pady = 11  #pone los margenes de tolerancia de y
            )
        tk.Label(
            self, #esto lo pongo como self ya que es la funcion principal
            text="Elige tu hotel para vacacionar dale mi rey Y(>Vo 7)",#que quiero que diga mi frame
            textvariable = self.currentOption, #esta es ka nueva variable
            justify= tk.CENTER, #justificar es para que me lo acomode
            **style.STYLE 
        ).pack(
            side = tk.TOP,
            fill = tk.X, #aqui nadamas usa el x por que no quiero que se expanda solo quiero que sea a lo largo 
            padx = 22,
            pady = 11
        )
        
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background=style.COMPONENT)
        optionsFrame.pack( #hago exactamente lo mismo pero con el otro frame
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )     
        tk.Label(
            optionsFrame, #esto lo pongo como optionframe ya que solo quiero que use nadamas esta
            text=" elige tu plan de vacaciones Y(>Vo 7)",#que quiero que diga mi frame
            justify= tk.CENTER, #justificar es para que me lo acomode
            **style.STYLE #esto es para que le ponga el estilo que ya habia definido no hay que olvidar el .style para que furule
        ).pack(
            side = tk.TOP,
            fill = tk.X, #aqui nadamas usa el x por que no quiero que se expanda solo quiero que sea a lo largo 
            padx = 22,
            pady = 11
        )
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background=style.COMPONENT)
        optionsFrame.pack( #hago exactamente lo mismo pero con el otro frame
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )     
        
        for (key, value) in config.PLAN_A.items(): #esto son para tuplas de mi diccionario
            tk.Radiobutton( 
                # pues en si esto es para edfinir un boton xd
                optionsFrame, #empaquetamos en el frame
                #" v--- esto es ma que nada por cosmetico"
                text = key + ("ᡣ𐭩" if key == "PLAN 3" else ""),
                variable= self.planMode, 
                #gracias a esta variable nuestro mapeo de este puede ser diferente, se guarda en variable gameMode
                value= value,
                #esto llama a la key de nuestro diccionario
                activebackground = style.BACKGROUND, # personalizar que cuando lo pulse le cambie color
                activeforeground = style.TEXT,
                 **style.STYLE
                ).pack(
                    side = tk.LEFT, # como quiero que esten uno al aldo delotro lo pongo asi
                    fill = tk.BOTH, # un poquito de lo mismo
                    expand = True,
                    padx = 5,
                    pady = 5
                    ) #aqui ya empezamos con lo dificil

        
        tk.Button( #este boton es el que me mueve de lugar de una ventana a otra
                    self,
                text = "Siguiente ->",
                command = self.update_option, 
                #en python las funciones se pueden usar como objetos por ende este codigo hace eso
                **style.STYLE,
                relief= tk.FLAT, #esto es para que el boton no tenga relieves 
                activebackground = style.BACKGROUND, # un poco de lo mismo
                activeforeground = style.TEXT,
                ).pack(
                    side = tk.TOP,
                    fill = tk.BOTH,
                    expand = True,
                    padx = 22,
                    pady = 11
                )
                
        tk.Button( #este boton es el que me mueve de lugar de una ventana a otra
                    self,
                text = "<<< Seleccionar >>>",
                command = self.move_to_cotizacion, 
                #en python las funciones se pueden usar como objetos por ende este codigo hace eso
                **style.STYLE,
                relief= tk.FLAT, #esto es para que el boton no tenga relieves 
                activebackground = style.BACKGROUND, # un poco de lo mismo
                activeforeground = style.TEXT,
                ).pack(
                    side = tk.TOP,
                    fill = tk.X,
                    padx = 22,
                    pady = 11
                )
        
        tk.Button( #este boton es el que me mueve de lugar de una ventana a otra
                    self,
                text = "<<< Home",
                command = lambda: self.controller.show_frame(Home), #con lambda cambias de pantalla
                **style.STYLE,
                relief= tk.FLAT, #esto es para que el boton no tenga relieves 
                activebackground = style.BACKGROUND, # un poco de lo mismo
                activeforeground = style.TEXT,
                ).pack(
                    side = tk.TOP,
                    fill = tk.BOTH,
                    expand = True,
                    padx = 22,
                    pady = 11
                )
                
                
class Cotizacion(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background= style.BACKGROUND)
        self.controller = controller
        self.currentOptionplan = tk.StringVar(self, value= "")# esta es la modificacion que agregamos para que actualice lo que queremos ver
        self.totales  = None
        
        
        self.init_widgets()   
    def update_option(self):
        self.mode = self.controller.mode
        if (self.totales == None) or (self.controller.plan_a.lower() not in self.totales.name.lower()):#este es para que se asegure de cual es la variable en la que esta
            self.totales = open(f'./App/totales/{self.PLAN_A}.txt', 'r', encoding="utf-8")
    
        tmp = self.totales.readline()
        if tmp != "":
            self.currentOptionplan.set(tmp)
        else:
            self.currentOptionplan.set("Son todas las opciones volvemos a empezar")
            self.totales.close()
            self.totales = open(f'./App/totales/{self.Plan_A}.txt', 'r', encoding="utf-8")
    def init_widgets(self):
        tk.Label(
            self, 
            text= " App de vacaciones ...",
            **style.STYLE
            ).pack(
                side = tk.TOP,
                fill = tk.BOTH,
                expand = True,
                padx = 22, #pone los margenes de tolerancia de x
                pady = 11  #pone los margenes de tolerancia de y
            )
        
        tk.Label(
            self, #esto lo pongo como optionframe ya que solo quiero que use nadamas esta
            text="Total a pagar es de: Y(>Vo 7)",#que quiero que diga mi frame
            justify= tk.CENTER, #justificar es para que me lo acomode
            **style.STYLE #esto es para que le ponga el estilo que ya habia definido no hay que olvidar el .style para que furule
        ).pack(
            side = tk.TOP,
            fill = tk.X, #aqui nadamas usa el x por que no quiero que se expanda solo quiero que sea a lo largo 
            padx = 22,
            pady = 11
        )
        tk.Label(
            self, #esto lo pongo como self ya que es la funcion principal
            #que quiero que diga mi frame
            text= config.TOTALES , #esta es ka nueva variable
            justify= tk.CENTER, #justificar es para que me lo acomode
            **style.STYLE 
        ).pack(
            side = tk.TOP,
            fill = tk.X, #aqui nadamas usa el x por que no quiero que se expanda solo quiero que sea a lo largo 
            padx = 22,
            pady = 11
        )
        tk.Button( #este boton es el que me mueve de lugar de una ventana a otra
                    self,
                text = "<<< Atras",
                command = lambda: self.controller.show_frame(Game), #con lambda cambias de pantalla
                **style.STYLE,
                relief= tk.FLAT, #esto es para que el boton no tenga relieves 
                activebackground = style.BACKGROUND, # un poco de lo mismo
                activeforeground = style.TEXT,
                ).pack(
                    side = tk.TOP,
                    fill = tk.BOTH,
                    expand = True,
                    padx = 22,
                    pady = 11
                )