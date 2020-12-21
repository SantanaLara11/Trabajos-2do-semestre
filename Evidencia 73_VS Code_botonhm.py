import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Prueba")
        self.boton1=tk.Button(self.ventana1, text="Hombre", command=self.presionhombre)
        self.boton1.grid(column=0, row=0)
        self.boton2=tk.Button(self.ventana1, text="Mujer", command=self.presionmujer)
        self.boton2.grid(column=4, row=2)
        self.ventana1.mainloop()
   
    def presionhombre(self):
        self.ventana1.title('Hombre')

    def presionmujer(self):
        self.ventana1.title('Mujer')

aplicacion=Aplicacion()    
