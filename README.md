# 📝 Formulario de Inscripción con Tkinter y Excel

Este proyecto es un **formulario de inscripción** desarrollado en **Python** usando **Tkinter** para la interfaz gráfica y **OpenPyXL** para guardar los datos en un archivo Excel (`inscripciones.xlsx`).  
Permite registrar estudiantes o participantes de cursos, validar la información y mostrar un mensaje de éxito.

---

## 🚀 Características

- Interfaz gráfica amigable con **Tkinter**  
- Validación de campos obligatorios: nombre, edad, email, teléfono y domicilio  
- Verificación de datos:  
  - Edad y teléfono deben ser números  
  - Nombre solo puede contener letras  
- Guardado automático en un archivo **Excel**  
- Mensaje de éxito al enviar el formulario  
- Opción de volver al formulario o salir de la aplicación  
- Adaptable a distintos tipos de cursos

---

## 🖥️ Requisitos

- Python 3.x  
- Librerías:  
  ```bash
  pip install openpyxl

## ▶️ Cómo ejecutar

   Cloná el repositorio:

   git clone https://github.com/TuUsuario/tu-repo.git

## 📊 Funcionalidad de Excel

   Los datos se guardan automáticamente en inscripciones.xlsx

   Cada registro incluye: Nombre, Edad, Email, Teléfono, Domicilio, Curso

   Si el archivo no existe, se crea automáticamente con los encabezados correspondientes

  ## 🛠️ Tecnologías utilizadas

     Python 3

     Tkinter: interfaz gráfica

     OpenPyXL: manejo de archivos Excel
