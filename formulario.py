import tkinter as tk
import Estudiante.Alumno as form  

# Función que oculta la ventana y abre el formulario
def abrir_formulario_y_ocultar(ventana_padre, tipo):
    ventana_padre.withdraw()
    form.ventana_formulario(ventana_padre, tipo)

# Ventana principal
ventana = tk.Tk()
ventana.title("INSCRIPCIÓN")
ventana.geometry("300x300")

tk.Label(ventana, text="¿Qué curso desea realizar?", font=("Arial", 14)).pack(pady=20)

btn_python = tk.Button(ventana, text="Python", width=25, bg="lightblue",
                       command=lambda: abrir_formulario_y_ocultar(ventana, "Python"))
btn_python.pack(pady=10)

btn_java = tk.Button(ventana, text="Java", width=25, bg="lightgreen",
                     command=lambda: abrir_formulario_y_ocultar(ventana, "Java"))
btn_java.pack(pady=10)

btn_js = tk.Button(ventana, text="JavaScript", width=25, bg="lightcoral",
                   command=lambda: abrir_formulario_y_ocultar(ventana, "JavaScript"))
btn_js.pack(pady=10)

btn_bd = tk.Button(ventana, text="Base de Datos", width=25, bg="lightsalmon",
                   command=lambda: abrir_formulario_y_ocultar(ventana, "Base de Datos"))
btn_bd.pack(pady=10)

ventana.mainloop()



