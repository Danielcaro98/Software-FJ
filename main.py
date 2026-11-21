

import tkinter as tk
from tkinter import messagebox

# ventana principal
ventana = tk.Tk()

ventana.title("Software FJ - Management System")
ventana.geometry("700x500")
ventana.resizable(False, False)

# Titulo
titulo = tk.Label(
    ventana,
    text="SOFTWARE FJ",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=20)

#subtitulo
subtitulo = tk.Label(
    ventana,
    text="customer, services and reservations management",
    font=("Arial", 12)
)
subtitulo.pack(pady=10)

#Funcion prueba
def mostrar_mensaje():
    messagebox.showinfo(
        "Software FJ",
        "Welcome to the management system!"
    )

# Botones principales
boton_clientes = tk.Button(
    ventana,
    text="Manage Customers",
    width=25,
    command=mostrar_mensaje
)
boton_clientes.pack(pady=10)

boton_servicios = tk.Button(
    ventana,
    text="Manage Services",
    width=25,
    command=mostrar_mensaje
)
boton_servicios.pack(pady=10)

boton_reservas = tk.Button(
    ventana,
    text="Manage Reservacions",
    width=25,
    command=mostrar_mensaje
)
boton_reservas.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()

