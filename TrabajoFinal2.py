import os
import sys
import tkinter as tk
from tkinter import ttk
import Conexion
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import Prestamos
os.system('cls')

#Trabajo Practico Final

class Biblioteca:
    def __init__(self):
        self.conexion=Conexion.ConnectionDB()
        self.conexion.crear()
        self.ventana=tk.Tk()    
        self.conexion2=Prestamos.ConnectionDB()
        self.conexion2.crear()
        self.ventana.title(' Biblioteca ')
        self.cuaderno1=ttk.Notebook(self.ventana)
        self.agregarMenu()
        self.libros()
        self.prestamos()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana.mainloop()

    def agregarMenu(self):
        menu = tk.Menu(self.ventana) 
        self.ventana.config(menu=menu) 
        opciones = tk.Menu(menu, tearoff=0) 
        opciones.add_command(label="    Salir    ", command=self.salir)
        menu.add_cascade(label="   Menu   ", menu = opciones)

    def salir(self):
        sys.exit()

    def libros(self):
        self.pagina_1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina_1, text='    Libros    ')
        self.cuaderno_1=ttk.Notebook(self.pagina_1)
        self.alta()
        self.modificarLibro()
        self.sacarLibro()
        self.consultarLibro()
        self.mostrarLibros()
        self.cuaderno_1.grid(column=0, row=0, padx=10, pady=10)

    def alta(self):
        self.pagina__1=ttk.Frame(self.cuaderno_1)
        self.cuaderno_1.add(self.pagina__1, text='  Dar de alta un libro  ')
        self.label1=ttk.Label(self.pagina__1, text='Titulo:')
        self.label1.grid(column=0, row=0, padx=6, pady=6)
        self.label2=ttk.Label(self.pagina__1, text='Autor:')
        self.label2.grid(column=0, row=1, padx=6, pady=6)
        self.label3=ttk.Label(self.pagina__1, text='Edicion:')
        self.label3.grid(column=0, row=2, padx=6, pady=6)
        self.label4=ttk.Label(self.pagina__1, text='Lugar de impresion:')
        self.label4.grid(column=0, row=3, padx=6, pady=6)
        self.label5=ttk.Label(self.pagina__1, text='Editorial:')
        self.label5.grid(column=0, row=4, padx=6, pady=6)
        self.label6=ttk.Label(self.pagina__1, text='Traduccion:')
        self.label6.grid(column=0, row=5, padx=6, pady=6)
        self.label7=ttk.Label(self.pagina__1, text='Cantidad de paginas:')
        self.label7.grid(column=0, row=6, padx=6, pady=6)
        self.titulo=tk.StringVar()
        self.entry1=ttk.Entry(self.pagina__1, textvariable=self.titulo)
        self.entry1.grid(column=1, row=0, padx=6, pady=6)
        self.autor=tk.StringVar()
        self.entry2=ttk.Entry(self.pagina__1, textvariable=self.autor)
        self.entry2.grid(column=1, row=1, padx=6, pady=6)
        self.edicion=tk.StringVar()
        self.entry3=ttk.Entry(self.pagina__1, textvariable=self.edicion)
        self.entry3.grid(column=1, row=2, padx=6, pady=6)
        self.impresion=tk.StringVar()
        self.entry4=ttk.Entry(self.pagina__1, textvariable=self.impresion)
        self.entry4.grid(column=1, row=3, padx=6, pady=6)
        self.editorial=tk.StringVar()
        self.entry5=ttk.Entry(self.pagina__1, textvariable=self.editorial)
        self.entry5.grid(column=1, row=4, padx=6, pady=6)
        self.paginas=tk.StringVar()
        self.entry6=ttk.Entry(self.pagina__1, textvariable=self.paginas)
        self.entry6.grid(column=1, row=6, padx=6, pady=6)
        self.seleccion1=tk.IntVar()
        self.radio1=ttk.Radiobutton(self.pagina__1, text='Si', variable=self.seleccion1, value=1)
        self.radio1.grid(column=1, row=5)
        self.radio2=ttk.Radiobutton(self.pagina__1, text='No', variable=self.seleccion1, value=2)
        self.radio2.grid(column=2, row=5)
        self.boton1=ttk.Button(self.pagina__1, text='Agregar', command=self.agregar)
        self.boton1.grid(column=1, row=8, padx=10, pady=10)
    def modificarLibro(self):
        self.pagina__2=ttk.Frame(self.cuaderno_1)
        self.cuaderno_1.add(self.pagina__2, text='  Modificar libro  ')
        self.label9=ttk.Label(self.pagina__2, text='Ingrese el titulo del libro al que quiere modificar:')
        self.label9.grid(column=0, row=0, padx=6, pady=6)
        self.label10=ttk.Label(self.pagina__2, text='Seleccione que quiere modificar:')
        self.label10.grid(column=0, row=1, padx=6, pady=6)
        self.label11=ttk.Label(self.pagina__2, text='Ingrese la nueva informacion:')
        self.label11.grid(column=0, row=5, padx=6, pady=6)
        self.buscarTitulo=tk.StringVar()
        self.entry7=ttk.Entry(self.pagina__2, textvariable=self.buscarTitulo)
        self.entry7.grid(column=1, row=0, padx=6, pady=6)
        self.nuevaInfo=tk.StringVar()
        self.entry8=ttk.Entry(self.pagina__2, textvariable=self.nuevaInfo)
        self.entry8.grid(column=1, row=5, padx=6, pady=6)
        self.cambiar=tk.IntVar()
        self.radio8=ttk.Radiobutton(self.pagina__2, text='Titulo', variable=self.cambiar, value=1)
        self.radio8.grid(column=0, row=2, padx=6, pady=6)
        self.radio9=ttk.Radiobutton(self.pagina__2, text='Autor', variable=self.cambiar, value=2)
        self.radio9.grid(column=1, row=2, padx=6, pady=6)
        self.radio10=ttk.Radiobutton(self.pagina__2, text='Edicion', variable=self.cambiar, value=3)
        self.radio10.grid(column=2, row=2, padx=6, pady=6)
        self.radio11=ttk.Radiobutton(self.pagina__2, text='Impresion', variable=self.cambiar, value=4)
        self.radio11.grid(column=0, row=3, padx=6, pady=6)
        self.radio12=ttk.Radiobutton(self.pagina__2, text='Editorial', variable=self.cambiar, value=5)
        self.radio12.grid(column=1, row=3, padx=6, pady=6)
        self.radio13=ttk.Radiobutton(self.pagina__2, text='Paginas', variable=self.cambiar, value=6)
        self.radio13.grid(column=2, row=3, padx=6, pady=6)
        self.radio14=ttk.Radiobutton(self.pagina__2, text='Traduccion', variable=self.cambiar, value=7)
        self.radio14.grid(column=0, row=4, padx=6, pady=6)
        self.boton2=ttk.Button(self.pagina__2, text='Modificar', command=self.modificarDatos)
        self.boton2.grid(column=0, row=6, padx=10, pady=10)
    def sacarLibro(self):
        self.pagina__3=ttk.Frame(self.cuaderno_1)
        self.cuaderno_1.add(self.pagina__3, text='  Eliminar un Libro  ')
        self.label12=ttk.Label(self.pagina__3, text='Ingrese el titulo del libro al que quiera eliminar')
        self.label12.grid(column=0, row=0, padx=6, pady=6)
        self.buscarTitulo2=tk.StringVar()
        self.entry9=ttk.Entry(self.pagina__3, textvariable=self.buscarTitulo2)
        self.entry9.grid(column=1, row=0, padx=6, pady=6)
        self.boton3=ttk.Button(self.pagina__3, text='Eliminar', command=self.eliminar)
        self.boton3.grid(column=1, row=1, padx=10, pady=10)
    def consultarLibro(self):
        self.pagina__4=ttk.Frame(self.cuaderno_1)
        self.cuaderno_1.add(self.pagina__4, text=' Consultar sobre un libro ')
        self.label13=ttk.Label(self.pagina__4, text='Ingrese el titulo del libro al que quiere consultar')
        self.label13.grid(column=0, row=0, padx=6, pady=6)
        self.buscarTitulo3=tk.StringVar()
        self.entry10=ttk.Entry(self.pagina__4, textvariable=self.buscarTitulo3)
        self.entry10.grid(column=1, row=0, padx=6, pady=6)
        self.boton4=ttk.Button(self.pagina__4, text='Mostrar Libro', command=self.mostrar)
        self.boton4.grid(column=1, row=1, padx=10, pady=10)
        self.label15=ttk.Label(self.pagina__4, text='Titulo:')
        self.label15.grid(column=0, row=2, padx=6, pady=6)
        self.label16=ttk.Label(self.pagina__4, text='Autor:')
        self.label16.grid(column=0, row=3, padx=6, pady=6)
        self.label17=ttk.Label(self.pagina__4, text='Edicion:')
        self.label17.grid(column=0, row=4, padx=6, pady=6)
        self.label18=ttk.Label(self.pagina__4, text='Lugar de impresion:')
        self.label18.grid(column=0, row=5, padx=6, pady=6)
        self.label19=ttk.Label(self.pagina__4, text='Editorial:')
        self.label19.grid(column=0, row=6, padx=6, pady=6)
        self.label20=ttk.Label(self.pagina__4, text='Traduccion:')
        self.label20.grid(column=0, row=7, padx=6, pady=6)
        self.label21=ttk.Label(self.pagina__4, text='Cantidad de paginas:')
        self.label21.grid(column=0, row=8, padx=6, pady=6)
        self.label22=ttk.Label(self.pagina__4, text='Condicion:')
        self.label22.grid(column=0, row=9, padx=6, pady=6)
        self.titulo_=tk.StringVar()
        self.entry11=ttk.Entry(self.pagina__4, textvariable=self.titulo_, state='readonly')
        self.entry11.grid(column=1, row=2, padx=6, pady=6)
        self.autor_=tk.StringVar()
        self.entry12=ttk.Entry(self.pagina__4, textvariable=self.autor_, state='readonly')
        self.entry12.grid(column=1, row=3, padx=6, pady=6)
        self.edicion_=tk.StringVar()
        self.entry13=ttk.Entry(self.pagina__4, textvariable=self.edicion_, state='readonly')
        self.entry13.grid(column=1, row=4, padx=6, pady=6)
        self.impresion_=tk.StringVar()
        self.entry14=ttk.Entry(self.pagina__4, textvariable=self.impresion_, state='readonly')
        self.entry14.grid(column=1, row=5, padx=6, pady=6)
        self.editorial_=tk.StringVar()
        self.entry15=ttk.Entry(self.pagina__4, textvariable=self.editorial_, state='readonly')
        self.entry15.grid(column=1, row=6, padx=6, pady=6)
        self.traduccion_=tk.StringVar()
        self.entry16=ttk.Entry(self.pagina__4, textvariable=self.traduccion_, state='readonly')
        self.entry16.grid(column=1, row=7, padx=6, pady=6)
        self.paginas_=tk.StringVar()
        self.entry17=ttk.Entry(self.pagina__4, textvariable=self.paginas_, state='readonly')
        self.entry17.grid(column=1, row=8, padx=6, pady=6)
        self.condicion_=tk.StringVar()
        self.entry18=ttk.Entry(self.pagina__4, textvariable=self.condicion_, state='readonly')
        self.entry18.grid(column=1, row=9, padx=6, pady=6)
    def mostrarLibros(self):
        self.pagina__5=ttk.Frame(self.cuaderno_1)
        self.cuaderno_1.add(self.pagina__5, text= '  Todos los libros  ')
        self.label23=ttk.Label(self.pagina__5, text='Libro de la biblioteca:')
        self.label23.grid(column=0, row=0, padx=10, pady=10)
        self.scrolledtext1=st.ScrolledText(self.pagina__5, width=50, height=20)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)
        self.boton5=ttk.Button(self.pagina__5, text='Actualizar', command=self.todos_los_libros)
        self.boton5.grid(column=1, row=0, padx=10, pady=10)
    
    def agregar(self):
        self.seleccion_1=''
        self.seleccion_2=''
        if self.seleccion1.get()==1:
            self.seleccion_1='Si'
        elif self.seleccion1.get()==2:
            self.seleccion_1='No'

        self.seleccion_2='Disponible'

        datos=(self.titulo.get(), self.autor.get(), self.edicion.get(), self.impresion.get(), self.editorial.get(), self.paginas.get(), self.seleccion_1, self.seleccion_2)
        self.conexion.alta(datos)
        self.titulo.set('')
        self.autor.set('')
        self.edicion.set('')
        self.impresion.set('')
        self.editorial.set('')
        self.paginas.set('')
        mb.showinfo('Informacion', 'El libro fue agregado')
        
    def modificarDatos(self):
        if self.cambiar.get()==1:
            datos=(self.nuevaInfo.get(), self.buscarTitulo.get())
            cantidad=self.conexion.cambiarTitulo(datos)
            if cantidad==1:
                mb.showinfo('Informacion', 'El libro fue modificado')
            else:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo')
            self.buscarTitulo.set('')
            self.nuevaInfo.set('')
        elif self.cambiar.get()==2:
            datos=(self.nuevaInfo.get(), self.buscarTitulo.get())
            cantidad=self.conexion.cambiarAutor(datos)
            if cantidad==1:
                mb.showinfo('Informacion', 'El libro fue modificado')
            else:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo')
            self.buscarTitulo.set('')
            self.nuevaInfo.set('')
        elif self.cambiar.get()==3:
            datos=(self.nuevaInfo.get(), self.buscarTitulo.get())
            cantidad=self.conexion.cambiarEdicion(datos)
            if cantidad==1:
                mb.showinfo('Informacion', 'El libro fue modificado')
            else:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo')
            self.buscarTitulo.set('')
            self.nuevaInfo.set('')
        elif self.cambiar.get()==4:
            datos=(self.nuevaInfo.get(), self.buscarTitulo.get())
            cantidad=self.conexion.cambiarImpresion(datos)
            if cantidad==1:
                mb.showinfo('Informacion', 'El libro fue modificado')
            else:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo')
            self.buscarTitulo.set('')
            self.nuevaInfo.set('')
        elif self.cambiar.get()==5:
            datos=(self.nuevaInfo.get(), self.buscarTitulo.get())
            cantidad=self.conexion.cambiarEditorial(datos)
            if cantidad==1:
                mb.showinfo('Informacion', 'El libro fue modificado')
            else:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo')
            self.buscarTitulo.set('')
            self.nuevaInfo.set('')
        elif self.cambiar.get()==6:
            datos=(self.nuevaInfo.get(), self.buscarTitulo.get())
            cantidad=self.conexion.cambiarPaginas(datos)
            if cantidad==1:
                mb.showinfo('Informacion', 'El libro fue modificado')
            else:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo')
            self.buscarTitulo.set('')
            self.nuevaInfo.set('')
        elif self.cambiar.get()==7:
            datos=(self.nuevaInfo.get(), self.buscarTitulo.get())
            cantidad=self.conexion.cambiarTraduccion(datos)
            if cantidad==1:
                mb.showinfo('Informacion', 'El libro fue modificado')
            else:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo')
            self.buscarTitulo.set('')
            self.nuevaInfo.set('')
        
    def eliminar(self):
        datos=(self.buscarTitulo2.get(), )
        cantidad=self.conexion.eliminarLibro(datos)
        self.buscarTitulo2.set('')
        if cantidad==1:
            mb.showinfo('Informacion', 'Se elimino el libro')
        else:
            mb.showinfo('Informacion', 'No existe un libro con ese titulo')

    def mostrar(self):
        self.titulo_.set('')
        self.autor_.set('')
        self.edicion_.set('')
        self.impresion_.set('')
        self.editorial_.set('')
        self.traduccion_.set('')
        self.paginas_.set('')
        self.condicion_.set('')
        datos=(self.buscarTitulo3.get(), )
        respuesta=self.conexion.mostrar1libro(datos)
        if len(respuesta) > 0:
            self.titulo_.set(respuesta[0][0])
            self.autor_.set(respuesta[0][1])
            self.edicion_.set(respuesta[0][2])
            self.impresion_.set(respuesta[0][3])
            self.editorial_.set(respuesta[0][4])
            self.traduccion_.set(respuesta[0][5])
            self.paginas_.set(respuesta[0][6])
            self.condicion_.set(respuesta[0][7])
            self.buscarTitulo3.set('')
        else:
            self.buscarTitulo3.set('')
            mb.showinfo("Información", "No existe un libro con ese titulo")

    def todos_los_libros(self):
        respuesta=self.conexion.mostrarLibros()
        self.scrolledtext1.delete('1.0', tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "Titulo: "+str(fila[0])+
                                              "\nAutor: "+fila[1]+
                                              "\nEdicion: "+str(fila[2])+
                                              '\nImpresion: '+str(fila[3])+
                                              '\nEditorial: '+str(fila[4])+
                                              '\nTraduccion: '+str(fila[5])+
                                              '\nPaginas: '+str(fila[6])+
                                              '\nCondicion: '+str(fila[7])+'\n\n')
        
    def prestamos(self):
        self.pagina_2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina_2, text='    Prestamos    ')
        self.cuaderno_2=ttk.Notebook(self.pagina_2)
        self.resgistrar()
        self.terminar()
        self.reclamar()
        self.cuaderno_2.grid(column=0, row=0, padx=10, pady=10)

    def resgistrar(self):
        self.pagina__6=ttk.Frame(self.cuaderno_2)
        self.cuaderno_2.add(self.pagina__6, text='  Registrar un prestamo  ')
        self.label24=ttk.Label(self.pagina__6, text='Ingrese el titulo del libro que quiere prestar:')
        self.label24.grid(column=0, row=0, padx=6, pady=6)
        self.label25=ttk.Label(self.pagina__6, text='Ingrese los datos de la persona a la que se le va a prestar el libro:')
        self.label25.grid(column=0, row=2, padx=6, pady=6)
        self.label26=ttk.Label(self.pagina__6, text='Ingrese el nombre completo:')
        self.label26.grid(column=0, row=3, padx=6, pady=6)
        self.label27=ttk.Label(self.pagina__6, text='Ingrese el numero de telefono:')
        self.label27.grid(column=0, row=4, padx=6, pady=6)
        self.label28=ttk.Label(self.pagina__6, text='Ingrese el mail:')
        self.label28.grid(column=0, row=5, padx=6, pady=6)
        self.label29=ttk.Label(self.pagina__6, text='Fecha de inicio del prestamo:')
        self.label29.grid(column=0, row=6, padx=6, pady=6)
        self.label30=ttk.Label(self.pagina__6, text='Fecha de devolucion del libro:')
        self.label30.grid(column=0, row=7, padx=6, pady=6)
        self.tituloPrestamo=tk.StringVar()
        self.entry19=ttk.Entry(self.pagina__6, textvariable=self.tituloPrestamo)
        self.entry19.grid(column=1, row=0, padx=6, pady=6)
        self.nombre=tk.StringVar()
        self.entry120=ttk.Entry(self.pagina__6, textvariable=self.nombre)
        self.entry120.grid(column=1, row=3, padx=6, pady=6)
        self.tel=tk.StringVar()
        self.entry21=ttk.Entry(self.pagina__6, textvariable=self.tel)
        self.entry21.grid(column=1, row=4, padx=6, pady=6)
        self.mail=tk.StringVar()
        self.entry22=ttk.Entry(self.pagina__6, textvariable=self.mail)
        self.entry22.grid(column=1, row=5, padx=6, pady=6)
        self.inicio=tk.StringVar()
        self.entry23=ttk.Entry(self.pagina__6, textvariable=self.inicio)
        self.entry23.grid(column=1, row=6, padx=6, pady=6)
        self.final=tk.StringVar()
        self.entry24=ttk.Entry(self.pagina__6, textvariable=self.final)
        self.entry24.grid(column=1, row=7, padx=6, pady=6)
        self.boton6=ttk.Button(self.pagina__6, text= ' Realizar Prestamo ', command=self.prestamo)
        self.boton6.grid(column=1, row=9, padx=10, pady=10)
        self.label43=ttk.Label(self.pagina__6, text='Ingrese las fechas del prestamos del libro con numeros\n                                    ej: 02/05')
        self.label43.grid(padx=6, pady=6, column=1, row=8)


    def terminar(self):
        self.pagina__7=ttk.Frame(self.cuaderno_2)
        self.cuaderno_2.add(self.pagina__7, text='  Terminar Prestamo  ')
        self.label31=ttk.Label(self.pagina__7, text='Ingrese el titulo del libro al que quiere finalizar el prestamo:')
        self.label31.grid(column=0, row=0, padx=6, pady=6)
        self.titulo___=tk.StringVar()
        self.entry25=ttk.Entry(self.pagina__7, textvariable=self.titulo___)
        self.entry25.grid(column=1, row=0, padx=10, pady=10)
        self.boton7=ttk.Button(self.pagina__7, text= ' Finalizar Prestamo ', command=self.finalizar)
        self.boton7.grid(column=1, row=1, padx=10, pady=10)
    def reclamar(self):
        self.pagina__8=ttk.Frame(self.cuaderno_2)
        self.cuaderno_2.add(self.pagina__8, text='  Condicion  ')
        self.label32=ttk.Label(self.pagina__8, text='Ingrese el titulo del libro al cual quiere ver su condicion:')
        self.label32.grid(column=0, row=0, padx=6, pady=6)
        self.titulo1=tk.StringVar()
        self.entry26=ttk.Entry(self.pagina__8, textvariable=self.titulo1)
        self.entry26.grid(column=1, row=0, padx=10, pady=10)
        self.boton8=ttk.Button(self.pagina__8, text='Ver condicion', command=self.verCondicion)
        self.boton8.grid(column=1, row=1, padx=10, pady=10)
        self.nombre_=tk.StringVar()
        self.entry27=ttk.Entry(self.pagina__8, textvariable=self.nombre_, state='readonly')
        self.entry27.grid(column=1, row=3, padx=6, pady=6)
        self.tel_=tk.StringVar()
        self.entry28=ttk.Entry(self.pagina__8, textvariable=self.tel_, state='readonly')
        self.entry28.grid(column=1, row=4, padx=6, pady=6)
        self.mail_=tk.StringVar()
        self.entry29=ttk.Entry(self.pagina__8, textvariable=self.mail_, state='readonly')
        self.entry29.grid(column=1, row=5, padx=6, pady=6)
        self.inicio_=tk.StringVar()
        self.entry30=ttk.Entry(self.pagina__8, textvariable=self.inicio_, state='readonly')
        self.entry30.grid(column=1, row=6, padx=6, pady=6)
        self.final_=tk.StringVar()
        self.entry31=ttk.Entry(self.pagina__8, textvariable=self.final_, state='readonly')
        self.entry31.grid(column=1, row=7, padx=6, pady=6)
        self.condicion1=tk.StringVar()
        self.entry32=ttk.Entry(self.pagina__8, textvariable=self.condicion1, state='readonly')
        self.entry32.grid(column=1, row=8, padx=6, pady=6)
        self.label33=ttk.Label(self.pagina__8, text='Datos del cliente:')
        self.label33.grid(column=0, row=2, padx=6, pady=6)
        self.label34=ttk.Label(self.pagina__8, text='Nombre:')
        self.label34.grid(column=0, row=3, padx=6, pady=6)
        self.label35=ttk.Label(self.pagina__8, text='Numer de telefono:')
        self.label35.grid(column=0, row=4, padx=6, pady=6)
        self.label36=ttk.Label(self.pagina__8, text='Mail:')
        self.label36.grid(column=0, row=5, padx=6, pady=6)
        self.label37=ttk.Label(self.pagina__8, text='Fecha de inicio del prestamo:')
        self.label37.grid(column=0, row=6, padx=6, pady=6)
        self.label38=ttk.Label(self.pagina__8, text='Fecha de devolucion del libro:')
        self.label38.grid(column=0, row=7, padx=6, pady=6)
        self.label39=ttk.Label(self.pagina__8, text='Condicion')
        self.label39.grid(column=0, row=8, padx=6, pady=6)
        self.label40=ttk.Label(self.pagina__8, text='Si desea cambiar la condicion del libro a Restraso presione el boton:')
        self.label40.grid(column=0, row=9, padx=6, pady=6)
        self.boton9=ttk.Button(self.pagina__8, text=' Cambiar Condicion del libro a Retraso ', command=self.retraso)
        self.boton9.grid(column=1, row=9, padx=10, pady=10)
        self.label41=ttk.Label(self.pagina__8, text='Si desea cambiar la condicion del libro a Restauracion presione el boton:')
        self.label41.grid(column=0, row=10, padx=6, pady=6)
        self.boton10=ttk.Button(self.pagina__8, text=' Cambiar condicion a Restauracion ', command=self.restauracion)
        self.boton10.grid(column=1, row=10, padx=10, pady=10)
        self.label42=ttk.Label(self.pagina__8, text='        Si desea cambiar la condicion del libro\nde Restauracion a Disponible presione el boton:')
        self.label42.grid(column=0, row=11, padx=6, pady=6)
        self.boton11=ttk.Button(self.pagina__8, text=' Cambiar condicion del libro de Restauracion a Disponible ', command=self.disponible)
        self.boton11.grid(column=1, row=11, padx=10, pady=10)

    def prestamo(self):
        self.condicion=True
        if self.inicio.get()>self.final.get():
            self.condicion=False
        if self.condicion==True:
            self.condicionNueva='Prestamo en proceso'
            titulo=(self.tituloPrestamo.get(),)
            datos=(self.tituloPrestamo.get(), self.nombre.get(), self.tel.get(), self.mail.get(), self.inicio.get(), self.final.get())
            self.conexion.realizarPrestamo(titulo, datos, self.condicionNueva)
            self.nombre.set('')
            self.tel.set('')
            self.mail.set('')
            self.inicio.set('')
            self.final.set('')
            self.tituloPrestamo.set('')
        else:
            mb.showinfo('Error', 'Ingrese bien las fechas del prestamo del libro')
        
    def finalizar(self):
        titulo=(self.titulo___.get(),)
        self.conexion.finalizarPrestamo(titulo)
        self.conexion2.finalizarPrestamo(titulo)
        self.titulo___.set('')
    
    def verCondicion(self):
        self.nombre_.set('')
        self.tel_.set('')
        self.mail_.set('')
        self.inicio_.set('')
        self.final_.set('')
        self.condicion1.set('')
        datos=(self.titulo1.get(),)
        respuesta=self.conexion2.condicion(datos)
        respuesta2=self.conexion.consultaCondicion(datos)
        self.condicion1.set(respuesta2[0][0])
        if respuesta!= []:
            self.nombre_.set(respuesta[0][0])
            self.tel_.set(respuesta[0][1])
            self.mail_.set(respuesta[0][2])
            self.inicio_.set(respuesta[0][3])
            self.final_.set(respuesta[0][4])

    def retraso(self):
        datos=(self.titulo1.get(),)
        cant=self.conexion.retraso(datos)
        if cant==1:
            self.condicion1.set('En retraso')
    
    def restauracion(self):
        datos=(self.titulo1.get(),)
        cant=self.conexion.restauracion(datos)
        if cant==1:
            self.condicion1.set('En restauracion')

    def disponible(self):
        datos=(self.titulo1.get(),)
        cant=self.conexion.disponible(datos)
        if cant==1:
            self.condicion1.set('Disponible')
                 
biclioteca1=Biblioteca()