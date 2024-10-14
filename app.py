import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller import user_repository
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk  # Para cargar imágenes

# Crear la ventana principal
master = tk.Tk()
master.title("Formulario de Registro")

def go_to_training():
    notebook.select(frame2)

# Crear un Notebook para gestionar pestañas
notebook = ttk.Notebook(master)
notebook.pack(pady=10)

# Pestaña de registro
frame1 = ttk.Frame(notebook, width=500, height=400)
frame1.pack(fill="both", expand=True)
frame1.pack_propagate(False)  # Para que el frame no cambie de tamaño
notebook.add(frame1, text="Registro")

# Pestaña de entrenamiento
frame2 = ttk.Frame(notebook, width=500, height=400)
frame2.pack(fill="both", expand=True)
frame2.pack_propagate(False)  # Para que el frame no cambie de tamaño
notebook.add(frame2, text="Entrenamiento")

# Etiquetas y campos de entrada en la pestaña de registro
tk.Label(frame1, text="Username:").grid(row=0)
tk.Label(frame1, text="Name:").grid(row=1)
tk.Label(frame1, text="Password:").grid(row=2)
tk.Label(frame1, text="Occupation:").grid(row=3)

e1 = tk.Entry(frame1)
e2 = tk.Entry(frame1)
e3 = tk.Entry(frame1)
e4 = tk.Entry(frame1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

# Radio buttons para seleccionar género
gender_var = tk.StringVar()
tk.Radiobutton(frame1, text="Male", variable=gender_var, value="Male").grid(row=4, sticky=tk.W)
tk.Radiobutton(frame1, text="Female", variable=gender_var, value="Female").grid(row=5, sticky=tk.W)

# Función para validar credenciales desde un archivo JSON
def validate_credentials():
    username = e1.get()
    password = e3.get()
    try:
        dataUsers = user_repository.load_users()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar los usuarios: {e}")
        return

    user = dataUsers.get(username)
    if user and user.get("password") == password:
        go_to_training()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Botón para iniciar sesión
start_button = tk.Button(frame1, text="Iniciar", command=validate_credentials)
start_button.grid(row=6, columnspan=2, pady=10)

# Aquí se muestran las rutinas con 4 ejercicios por cada botón
def routineWindows(routineName):
    newWindow = tk.Toplevel(master)
    newWindow.title(f"Rutina: {routineName}")
    
    # Crear  espacios para las imágenes de los ejercicios
    exercise_names = [f"{routineName} - Ejercicio {i+1}" for i in range(4)]
    
    for i, exercise in enumerate(exercise_names):
        try:
            # Ajusta el nombre de las imágenes según tus archivos
            img_path = f"images/{routineName.lower()}_{i+1}.png"
            img = Image.open(img_path)
            img = img.resize((200, 150), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            
            # Mostrar cada imagen en su propio Label
            img_label = tk.Label(newWindow, image=img)
            img_label.image = img  # Importante para mantener la referencia
            img_label.grid(row=i, column=0, padx=10, pady=10)
            
            # Texto descriptivo del ejercicio
            label = tk.Label(newWindow, text=exercise)
            label.grid(row=i, column=1, padx=10, pady=10)
            
        except Exception as e:
            print(f"Error cargando imagen: {e}")
            tk.Label(newWindow, text=f"{exercise} - Imagen no disponible").grid(row=i, column=0, columnspan=2)

# Botones para actividades de entrenamiento en la pestaña de entrenamiento
button1 = tk.Button(frame2, text="Brazo", command=lambda: routineWindows("Brazo"))
button2 = tk.Button(frame2, text="Espalda", command=lambda: routineWindows("Espalda"))
button3 = tk.Button(frame2, text="Pecho", command=lambda: routineWindows("Pecho"))
button4 = tk.Button(frame2, text="Pierna", command=lambda: routineWindows("Pierna"))
button5 = tk.Button(frame2, text="Full Body", command=lambda: routineWindows("Full Body"))

# Colocar los botones en una cuadrícula
button1.grid(row=0, column=0, padx=5, pady=5)
button2.grid(row=0, column=1, padx=5, pady=5)
button3.grid(row=1, column=0, padx=5, pady=5)
button4.grid(row=1, column=1, padx=5, pady=5)
button5.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Pie de página
footer_label = tk.Label(master, text="BodyBuilder App v1.0 - Desarrollado por XYZ", fg="gray")
footer_label.pack(pady=10)

# Ejecutar el bucle principal
master.mainloop()
