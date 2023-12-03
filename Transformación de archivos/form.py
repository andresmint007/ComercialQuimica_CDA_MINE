import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import queue
import funcion_dashboard as FilePro

selected_files = []  # Lista para almacenar las rutas de los archivos seleccionados
progress_queue = queue.Queue()  # Cola para recibir el progreso desde el hilo secundario

def get_file_path():
    global selected_files, save_directory
    selected_file = filedialog.askopenfilename()
    if selected_file:
        # Obtener la ruta del directorio sin el nombre del archivo seleccionado
        save_directory = os.path.dirname(selected_file)

        # Agregar la ruta del archivo seleccionado a la lista
        selected_files.append(selected_file)

        # Ocultar el botón y la etiqueta al hacer clic en "Examinar archivo"
        button.pack_forget()
        selected_file_label.pack_forget()

        # Mostrar el nombre del archivo seleccionado en una nueva etiqueta
        selected_file_label.config(text="Archivo seleccionado: " + os.path.basename(selected_file))
        selected_file_label.pack()

        process_button.config(state="normal")  # Habilitar el botón "Procesar"

def process_file_in_thread():
    global selected_files
    # Deshabilitar el botón "Procesar" para evitar más clics mientras se procesa
    process_button.config(state="disabled")

    # Ejemplo de función para procesar el archivo y actualizar el progreso
    max_progress = 100

    FilePro.procesarArhcivo(selected_files[0], progress_queue)  # Obtener el progreso

    # Habilitar el botón "Procesar" nuevamente después de finalizar
    process_button.config(state="normal")

    # Mostrar mensaje de "Exportación finalizada"
    completion_label.config(text="Exportación finalizada")

def update_progress_label():
    while not progress_queue.empty():
        progress = progress_queue.get()
        progress_label.config(text=f"Hoja Actual: {progress}")
        root.update_idletasks()  # Actualizar la interfaz gráfica
        progress_queue.task_done()
    root.after(100, update_progress_label)  # Volver a verificar la cola cada 100 ms

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario para Transformación de Archivos")
root.geometry("600x300")  # Cambiar las dimensiones de la ventana (ancho x alto)

# Agregar imagen
image = Image.open("LogoComercial.png")
image = image.resize((519, 128))  # Cambiar el tamaño de la imagen
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)

# Agregar texto
text_label = tk.Label(root, text="Seleccione el archivo a transformar", font=("Arial", 14))
text_label.pack()

# Etiqueta para mostrar el nombre del archivo seleccionado
selected_file_label = tk.Label(root, text="", font=("Arial", 12))

# Botón para abrir el diálogo de selección de archivo
button = tk.Button(root, text="Examinar archivo", command=get_file_path)
button.pack(pady=10)

# Botón para procesar el archivo
process_button = tk.Button(root, text="Procesar", command=lambda: threading.Thread(target=process_file_in_thread).start())
process_button.pack()
process_button.config(state="disabled")  # Inhabilitar el botón de procesar inicialmente


# Etiqueta para mostrar el mensaje de "Exportación finalizada"
completion_label = tk.Label(root, text="", font=("Arial", 12))
completion_label.pack()

# Iniciar el hilo para actualizar el progreso
update_progress_label()

# Ejecutar la aplicación
root.mainloop()