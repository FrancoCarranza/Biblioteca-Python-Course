import os
import sqlite3
from tkinter import messagebox as mb
import Prestamos
os.system('cls') 

class ConnectionDB:
    def __init__(self):
        self.conexion=Prestamos.ConnectionDB()
    def abrir(self):
        conexion=sqlite3.connect('biblioteca.db')
        return conexion
    def crear(self):
        conexion=self.abrir()
        try:
            conexion.execute('''create table biblioteca(
                        titulo text,
                        autor text,
                        edicion text,
                        impresion text,
                        editorial text,
                        paginas real,
                        traduccion text,
                        condicion text
                        )
                ''')
        except sqlite3.OperationalError:
            print('La tabla biblioteca ya existe')
    def alta(self, datos):
        conexion=self.abrir()
        cursor=conexion.cursor()
        sql="insert into biblioteca(titulo, autor, edicion, impresion, editorial, paginas, traduccion, condicion) values (?,?,?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()
    def cambiarTitulo(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update biblioteca set titulo=? where titulo=?"
            cursor.execute(sql, datos)
            cone.commit()  
            return cursor.rowcount  
        except:
            cone.close()
    def cambiarAutor(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update biblioteca set autor=? where titulo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount           
        except:
            cone.close()
    def cambiarEdicion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update biblioteca set edicion=? where titulo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount           
        except:
            cone.close()
    def cambiarImpresion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update biblioteca set impresion=? where titulo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount           
        except:
            cone.close()
    def cambiarEditorial(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update biblioteca set editorial=? where titulo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount           
        except:
            cone.close()
    def cambiarPaginas(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update biblioteca set paginas=? where titulo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount           
        except:
            cone.close()
    def cambiarTraduccion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update biblioteca set traduccion=? where titulo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount           
        except:
            cone.close()
    
    def eliminarLibro(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from biblioteca where titulo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()

    def mostrar1libro(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select titulo, autor, edicion, impresion, editorial, traduccion, paginas, condicion from biblioteca where titulo=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
        
    def mostrarLibros(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select titulo, autor, edicion, impresion, editorial, traduccion, paginas, condicion from biblioteca"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def realizarPrestamo(self, titulo, datos, condicionNueva):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select condicion from biblioteca where titulo=? "
            cursor.execute(sql,titulo)
            cone.commit()  
            condicion=cursor.fetchall()
            if condicion != [] :
                disponible=[('Disponibe',)]
                if condicion[0][0]=='Disponible':
                    self.conexion.alta(datos)
                    cone=self.abrir()
                    cursor=cone.cursor() 
                    datoss=(condicionNueva, titulo[0])
                    sql2=('update biblioteca set condicion=? where titulo=? ')
                    cursor.execute(sql2, datoss)
                    cone.commit()
                    mb.showinfo('Informacion', 'El prestamo fue registrado')
                elif condicion==disponible:
                    self.conexion.alta(datos)
                    cone=self.abrir()
                    cursor=cone.cursor() 
                    datoss=(condicionNueva, titulo[0])
                    sql2=('update biblioteca set condicion=? where titulo=? ')
                    cursor.execute(sql2, datoss)
                    cone.commit()
                    mb.showinfo('Informacion', 'El prestamo fue registrado')
                else:
                    mb.showinfo('Informacion', 'Este libro no esta disponible para prestamos')
            else:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo')
        finally:
            cone.close()
        
    def finalizarPrestamo(self, titulo):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select condicion from biblioteca where titulo=?"
            cursor.execute(sql, titulo)
            cone.commit()  
            condicion=cursor.fetchall()
            if condicion==[('Prestamo en proceso',)] or condicion==[('Retraso',)]:
                try:
                    cone=self.abrir()
                    cursor=cone.cursor()
                    sql="update biblioteca set condicion=? where titulo=?"
                    condicionNueva='Disponibe'
                    datos=(condicionNueva, titulo[0])
                    cursor.execute(sql, datos)
                    cone.commit()
                    mb.showinfo('Informacion', 'El prestamo fue finalizado')
                    return cursor.rowcount 
                finally:
                    cone.close()
            elif condicion==[('Retraso')]:
                mb.showinfo('Informacion', 'Este libro esta en condicion de retraso')
            else:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo en prestamo')
        finally:
            cone.close()
    def consultaCondicion(self, titulo):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select condicion from biblioteca where titulo=?"
            cursor.execute(sql, titulo)
            cone.commit()  
            return cursor.fetchall()
        finally:
            cone.close()

    def retraso(self, titulo):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select condicion from biblioteca where titulo=? "
            cursor.execute(sql,titulo)
            cone.commit()  
            condicion=cursor.fetchall()
            if condicion != [] :
                if condicion[0][0] == 'Prestamo en proceso':
                    cone=self.abrir()
                    cursor=cone.cursor()
                    condicionNueva='Retraso' 
                    datoss=(condicionNueva, titulo[0])
                    sql2=('update biblioteca set condicion=? where titulo=? ')
                    cursor.execute(sql2, datoss)
                    cone.commit()
                    mb.showinfo('Informacion', 'La condicion del libro se ha actualizado a Retraso')
                    return cursor.rowcount
                elif condicion[0][0]=='Retraso':
                    mb.showinfo('Informacion', 'Este libro ya esta en condicion de retraso')
                else:
                    mb.showinfo('Informacion', 'Este libro no esta en prestamo')
            else:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo')
        finally:
            cone.close()
        
    def restauracion(self, titulo):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select condicion from biblioteca where titulo=? "
            cursor.execute(sql,titulo)
            cone.commit()  
            condicion=cursor.fetchall()
            if condicion != [] :
                if condicion[0][0] == 'Disponible':
                    cone=self.abrir()
                    cursor=cone.cursor()
                    condicionNueva='En restauracion' 
                    datoss=(condicionNueva, titulo[0])
                    sql2=('update biblioteca set condicion=? where titulo=? ')
                    cursor.execute(sql2, datoss)
                    cone.commit()
                    mb.showinfo('Informacion', 'La condicion del libro se ha actualizado a Restauracion')
                    return cursor.rowcount
                elif condicion==[('Disponibe',)]:
                    cone=self.abrir()
                    cursor=cone.cursor()
                    condicionNueva='En restauracion' 
                    datoss=(condicionNueva, titulo[0])
                    sql2=('update biblioteca set condicion=? where titulo=? ')
                    cursor.execute(sql2, datoss)
                    cone.commit()
                    mb.showinfo('Informacion', 'La condicion del libro se ha actualizado a Restauracion')
                    return cursor.rowcount
                elif condicion==[('En restauracion',)] :
                    mb.showinfo('Informacion', 'Este libro ya esta en restauracion')
                else:
                    mb.showinfo('Informacion', 'Este libro esta en prestamo')
                
            else:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo')
        finally:
            cone.close()

    def disponible(self, titulo):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select condicion from biblioteca where titulo=? "
            cursor.execute(sql,titulo)
            cone.commit()  
            condicion=cursor.fetchall()
            if condicion != [] :
                if condicion[0][0] == 'En restauracion':
                    cone=self.abrir()
                    cursor=cone.cursor()
                    condicionNueva='Disponible' 
                    datoss=(condicionNueva, titulo[0])
                    sql2=('update biblioteca set condicion=? where titulo=? ')
                    cursor.execute(sql2, datoss)
                    cone.commit()
                    mb.showinfo('Informacion', 'La condicion del libro se ha actualizado a Disponible')
                    return cursor.rowcount
                elif condicion==[('Disponible',)] :
                    mb.showinfo('Informacion', 'Este libro ya esta Disponible')    
                elif condicion[0][0]=='Retraso':
                    mb.showinfo('Informacion', 'Este libro esta en prestamo')
            else:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo')
        finally:
            cone.close()