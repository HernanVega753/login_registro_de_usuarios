
from tkinter import Tk, Canvas, Frame, Label, Entry, ttk, Button


def separador(fila, columna, frame):
    separador = ttk.Separator(frame, orient='horizontal')
    separador.grid(row=fila, column=columna, columnspan=3, sticky='ew', pady=20)


class RegistroUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title("Constructora BYTEBUSTERS | Registración")

        # Canvas
        self.canvas = Canvas(root, height=470, width=260)
        self.canvas.pack()

        # Frame
        self.frame = Frame(root)
        self.frame.place(relwidth=1, relheight=1)

        #root.resizable(False, False)
        # Label Título
        label = Label(self.frame, text="Regístrate aquí a CONSTRUCTORA BYTEBUSTERS")
        label.grid()

        # Separador horizontal
        separador(1, 0, self.frame)

        # Label datos (ejemplo de algunos campos)
        campos = ['Nombre', 'Apellido', 'Teléfono', 'Email', 'Usuario', 'Contraseña', 'Confirmar Contraseña']
        self.entries = {}  # Diccionario para almacenar las entradas de texto
        for i, campo in enumerate(campos):
            label = Label(self.frame, text=campo)
            label.grid(row=2 * i + 2, column=0)
            entry = Entry(self.frame, width=30)
            entry.grid(row=2 * i + 3, column=0)
            self.entries[campo] = entry  # Agregar entrada al diccionario

        # Separador después de los campos
        separador(2 * len(campos) + 2, 0, self.frame)

        # Label para mensajes de error
        self.error_label = Label(self.frame, text="", fg="red")
        self.error_label.grid(row=2 * len(campos) + 4, column=0, pady=10)

        # Botón "CONFIRMAR"
        button = Button(self.frame, text="CONFIRMAR", command=self.validar_campos)
        button.grid(row=2 * len(campos) + 3, column=0, pady=10)

    def validar_campos(self):
        # Obtener valores de los campos
        nombre = self.entries['Nombre'].get()
        apellido = self.entries['Apellido'].get()
        telefono = self.entries['Teléfono'].get()
        email = self.entries['Email'].get()
        usuario = self.entries['Usuario'].get()
        contraseña = self.entries['Contraseña'].get()
        confirmar_contraseña = self.entries['Confirmar Contraseña'].get()

        # Verificar si todos los campos están llenos
        if nombre and apellido and telefono and email and usuario and contraseña and confirmar_contraseña:
            # Verificar si las contraseñas coinciden
            if contraseña == confirmar_contraseña:
                # Si todo está correcto, proceder con la lógica de tu aplicación
                self.error_label.config(text="")
                print("Usuario guardado correctamente")
                # Aquí deberías escribir el código para continuar con la lógica de tu aplicación
                # Por ejemplo, guardar los datos en una base de datos o hacer otra acción.

                # Limpiar los campos después de procesar
                self.limpiar_campos()
            else:
                # Mostrar mensaje de error si las contraseñas no coinciden
                self.error_label.config(text="Las contraseñas no coinciden")
                self.limpiar_campos()
        else:
            # Mostrar mensaje de error si no todos los campos están llenos
            self.error_label.config(text="Por favor, llene todos los campos.")
            self.limpiar_campos()

    def limpiar_campos(self):
        # Limpiar todos los campos de entrada
        for entry in self.entries.values():
            entry.delete(0, 'end')


if __name__ == "__main__":
    root = Tk()
    registro_usuario = RegistroUsuario(root)
    root.mainloop()