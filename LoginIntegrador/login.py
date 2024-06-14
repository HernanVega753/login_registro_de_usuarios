import psycopg2
from tkinter import Tk, Frame, Label, Entry, ttk, Button


# Reutilizo separador desde registro_usuarios como método estático
def separador(fila, columna, frame):
    separador = ttk.Separator(frame, orient='horizontal')
    separador.grid(row=fila, column=columna, columnspan=3, sticky='ew', pady=20)

class login:
    def __init__(self, root, frame):
        self.root = root
        self.root.title("Constructora BYTEBUSTERS | Registración")

        # Frame
        self.frame = Frame(root)
        self.frame.pack(fill='both', expand=True)