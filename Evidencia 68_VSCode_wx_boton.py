import wx

class Ventana(wx.Frame):
    def __init__(self, *args, **kw):
        super(Ventana, self).__init__(*args, **kw)
        self.boton1 =wx.Button(self, label="Presionar")
        self.Bind(wx.EVT_BUTTON, self.presion_boton,self.boton1)
    
    def presion_boton(self,evento):
        wx.MessageBox("Hola Santana, ¿cómo estás?")

aplicacion = wx.App()
frm = Ventana(None, title='Ventana VS Code')
frm.Show()
aplicacion.MainLoop()
