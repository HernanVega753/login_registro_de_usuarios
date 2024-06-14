import psycopg2
from tkinter import Tk, Frame, Label, Entry, ttk, Button
from registro_usuarios import RegistroUsuario  # Importa la clase RegistrarUsuario

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Constructora BYTEBUSTERS | Iniciar Sesión")

        # Frame
        self.frame = Frame(root)
        self.frame.pack(fill='both', expand=True)

        # Label Título
        label = Label(self.frame, text="Ingreso de usuarios | CONSTRUCTORA BYTEBUSTERS")
        label.grid()

        # Separador horizontal
        self.separador(1, 0)

        # Guardo los nombres que tendrán los Labels y los posiciono
        campos = ['Usuario', 'Contraseña']
        self.entries = {}  # Diccionario para guardar las respuestas
        for i, campo in enumerate(campos):
            label = Label(self.frame, text=campo)
            label.grid(row=2 * i + 2, column=0)
            entry = Entry(self.frame, width=30, show="*")  # show="*" para ocultar la contraseña
            entry.grid(row=2 * i + 3, column=0)
            self.entries[campo] = entry

        # Separador después de los campos
        self.separador(2 * len(campos) + 2, 0)

        # Label para mensajes de error
        self.error_label = Label(self.frame, text="", fg="red")
        self.error_label.grid(row=2 * len(campos) + 4, column=0, pady=10)

        # Botón CONFIRMAR
        button = Button(self.frame, text="CONFIRMAR", command=self.validar_campos)
        button.grid(row=2 * len(campos) + 2, column=0, pady=10)

        # Botón REGISTRARSE
        button_registrar = Button(self.frame, text="REGISTRARSE", command=self.ir_a_registrar)
        button_registrar.grid(row=2 * len(campos) + 3, column=0, pady=10)

    def separador(self, fila, columna):
        separador = ttk.Separator(self.frame, orient='horizontal')
        separador.grid(row=fila, column=columna, columnspan=3, sticky='ew', pady=20)

    def ir_a_registrar(self):
        # Función para abrir la ventana de registro
        self.root.withdraw()  # Oculta la ventana actual
        registrar_root = Tk()  # Crea una nueva ventana para el registro
        registrar_usuario = RegistroUsuario(registrar_root)
        registrar_root.mainloop()

    def validar_campos(self):
        try:
            usuario = self.entries['Usuario'].get()
            contraseña = self.entries['Contraseña'].get()

            if usuario and contraseña:
                try:
                    conexion = psycopg2.connect(user='postgres',
                                                password='admin',
                                                host='127.0.0.1',
                                                port='5432',
                                                database='integrador_constructora')

                    with conexion:
                        with conexion.cursor() as cursor:
                            query = "SELECT * FROM usuarios WHERE usuario = %s AND contrasenia = %s"
                            cursor.execute(query, (usuario, contraseña))
                            usuario_valido = cursor.fetchone()

                            if usuario_valido:
                                self.error_label.config(text="Inicio de sesión exitoso", fg="green")
                                print("Inicio de sesión exitoso para:", usuario)
                            else:
                                self.error_label.config(text="Usuario o contraseña incorrectos", fg="red")
                                print("Usuario o contraseña incorrectos")

                except Exception as e:
                    self.error_label.config(text=f'Ocurrió un error: {e}')
                    print(f'Ocurrió un error: {e}')

                finally:
                    if 'conexion' in locals():
                        conexion.close()

                self.limpiar_campos()

            else:
                self.error_label.config(text="Por favor, llene todos los campos.")

        except KeyError as e:
            self.error_label.config(text=f"Error al obtener el campo: {e}")
            print(f"Error al obtener el campo: {e}")

    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, 'end')

if __name__ == "__main__":
    root = Tk()
    login = Login(root)
    root.mainloop()