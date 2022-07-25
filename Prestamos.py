import os
import sqlite3
from tkinter import messagebox as mb
os.system('cls') 

class ConnectionDB:
    def abrir(self):
        conexion=sqlite3.connect('informacion.db')
        return conexion
    def crear(self):
        conexion=self.abrir()
        try:
            conexion.execute('''create table informacion(
                        titulo text,
                        nombre text,
                        telefono text,
                        mail text,
                        inicio text,
                        final text
                        )
                ''')
        except sqlite3.OperationalError:
            print('La tabla informacion ya existe')
    def alta(self, datos):
        conexion=self.abrir()
        cursor=conexion.cursor()
        sql="insert into informacion(titulo, nombre, telefono, mail, inicio, final) values (?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()
    def finalizarPrestamo(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from informacion where titulo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount
        except:
            cone.close()
    def condicion(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql='select nombre, telefono, mail, inicio, final from informacion where titulo=?'
            cursor.execute(sql, datos)
            nombre=cursor.fetchall()
            if nombre == []:
                mb.showinfo('Informacion', 'No existe un libro con ese titulo en prestamo')
            else:
                return nombre
        finally:
            cone.close()