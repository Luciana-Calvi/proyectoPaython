import tkinter as tk
from tkinter import messagebox
from Estudiante.mensajeExito import mensaje_exito

def ventana_formulario(ventana_padre, tipo):
    ventana = tk.Toplevel(ventana_padre)
    ventana.configure(bg="mistyrose")
    ventana.title(f"Formulario de {tipo}")
    ventana.geometry("400x400")

    tk.Label(ventana, text="Nombre:").pack()
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack()

    tk.Label(ventana, text="Edad:").pack()
    entrada_edad = tk.Entry(ventana)
    entrada_edad.pack()

    tk.Label(ventana, text="Email:").pack()
    entrada_mail = tk.Entry(ventana)
    entrada_mail.pack()

    tk.Label(ventana, text="Teléfono:").pack()
    entrada_telefono = tk.Entry(ventana)
    entrada_telefono.pack()

    tk.Label(ventana, text="Domicilio:").pack()
    entrada_domicilio = tk.Entry(ventana)
    entrada_domicilio.pack()

    def validar_datos(nombre, edad, mail, telefono, domicilio):
        if not (nombre and edad and mail and telefono and domicilio):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return False
        if not edad.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número.")
            return False
        if not telefono.isdigit():
            messagebox.showerror("Error", "El teléfono debe ser un número.")
            return False
        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El nombre solo debe contener letras.")
            return False
        return True

    def procesar_formulario():
        nombre = entrada_nombre.get()
        edad = entrada_edad.get()
        mail = entrada_mail.get()
        telefono = entrada_telefono.get()
        domicilio = entrada_domicilio.get()
        curso = tipo
        ventana.configure(bg="mistyrose")

        if not validar_datos(nombre, edad, mail, telefono, domicilio):
            return

        ventana.destroy()  # cerrar formulario
        mensaje_exito(ventana_padre, nombre, edad, mail, telefono, domicilio, tipo)


    tk.Button(ventana, text="Enviar", command=procesar_formulario).pack(pady=10)


    


   