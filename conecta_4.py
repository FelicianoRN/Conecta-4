import tkinter as tk
from tkinter import messagebox
import time

def traducir_color(color):
    """
    Traduce los colores en español al formato en inglés esperado por tkinter.
    """
    colores = {
        "Rojo": "red",
        "Amarillo": "yellow",
    }
    return colores.get(color, "blue")  # Valor predeterminado: "blue"

class ConectaCuatro:
    def __init__(self, root):
        self.root = root
        self.root.title("Conecta Cuatro")
        self.root.configure(bg="#2C2F33")  # Fondo oscuro moderno

        # Configuración inicial
        self.filas = 6
        self.columnas = 7
        self.turno = "Rojo"  # Comienza siempre la ficha Roja
        self.marcador = {"Rojo": 0, "Amarillo": 0}

        # Crear el tablero
        self.tablero = [[None for _ in range(self.columnas)] for _ in range(self.filas)]

        # Crear interfaz gráfica
        self.crear_interfaz()

    def crear_interfaz(self):
        # Frame para el indicador del turno
        self.frame_turno = tk.Frame(self.root, bg="#2C2F33", pady=10)
        self.frame_turno.pack(pady=10)
        
        # Ficha visual del turno actual
        self.label_turno = tk.Label(self.frame_turno, text="Turno:", font=("Arial", 14), bg="#2C2F33", fg="white")
        self.label_turno.grid(row=0, column=0, padx=10)
        
        self.turno_visual = tk.Canvas(self.frame_turno, width=30, height=30, bg="#2C2F33", highlightthickness=0)
        self.turno_visual.grid(row=0, column=1)
        self.turno_visual.create_oval(5, 5, 25, 25, fill=traducir_color(self.turno))

        # Frame del tablero
        self.frame_tablero = tk.Frame(self.root, bg="#23272A")
        self.frame_tablero.pack(pady=10)

        self.botones_columna = []
        for c in range(self.columnas):
            boton = tk.Button(
                self.frame_tablero, text=f"↓", font=("Arial", 12), 
                command=lambda col=c: self.colocar_ficha(col), bg="#7289DA", fg="white"
            )
            boton.grid(row=0, column=c, padx=5, pady=5)
            self.botones_columna.append(boton)

        self.labels_tablero = []
        for f in range(self.filas):
            fila_labels = []
            for c in range(self.columnas):
                label = tk.Canvas(self.frame_tablero, width=50, height=50, bg="#2C2F33", highlightthickness=0)
                label.grid(row=f + 1, column=c, padx=5, pady=5)
                label.create_oval(5, 5, 45, 45, fill="#23272A")  # Fondo circular oscuro
                fila_labels.append(label)
            self.labels_tablero.append(fila_labels)

        # Frame para marcador y botones
        self.frame_controles = tk.Frame(self.root, bg="#2C2F33")
        self.frame_controles.pack(pady=10)

        self.label_marcador = tk.Label(
            self.frame_controles, text=f"Rojo: 0 | Amarillo: 0", font=("Arial", 14), bg="#2C2F33", fg="white"
        )
        self.label_marcador.pack()

        self.boton_reiniciar = tk.Button(
            self.frame_controles, text="Reiniciar Partida", command=self.reiniciar_partida, font=("Arial", 12), bg="#7289DA", fg="white"
        )
        self.boton_reiniciar.pack(side=tk.LEFT, padx=10)

        self.boton_reset = tk.Button(
            self.frame_controles, text="Resetear Marcador", command=self.resetear_marcador, font=("Arial", 12), bg="#7289DA", fg="white"
        )
        self.boton_reset.pack(side=tk.LEFT, padx=10)

    def colocar_ficha(self, columna):
        """
        Coloca una ficha en la columna seleccionada con animación.
        """
        for fila in reversed(range(self.filas)):
            if self.tablero[fila][columna] is None:
                self.tablero[fila][columna] = self.turno

                # Animación de caída
                for anim_fila in range(fila + 1):
                    color = traducir_color(self.turno)
                    self.labels_tablero[anim_fila][columna].delete("all")
                    self.labels_tablero[anim_fila][columna].create_oval(5, 5, 45, 45, fill=color)
                    self.root.update()
                    time.sleep(0.05)
                    if anim_fila != fila:
                        self.labels_tablero[anim_fila][columna].delete("all")
                        self.labels_tablero[anim_fila][columna].create_oval(5, 5, 45, 45, fill="#23272A")

                # Verificar si alguien ha ganado
                if self.verificar_ganador(fila, columna):
                    self.marcador[self.turno] += 1
                    self.actualizar_marcador()
                    messagebox.showinfo("Juego terminado", f"{self.turno} gana la partida!")
                    self.reiniciar_partida()
                else:
                    self.cambiar_turno()
                return

        # Si la columna está llena
        messagebox.showwarning("Columna llena", "Esa columna ya está llena. Elige otra.")

    def cambiar_turno(self):
        self.turno = "Amarillo" if self.turno == "Rojo" else "Rojo"
        self.turno_visual.delete("all")
        self.turno_visual.create_oval(5, 5, 25, 25, fill=traducir_color(self.turno))

    def verificar_ganador(self, fila, columna):
        ficha = self.tablero[fila][columna]
        return any(
            self.verificar_direccion(fila, columna, delta_f, delta_c, ficha)
            for delta_f, delta_c in [(0, 1), (1, 0), (1, 1), (1, -1)]
        )

    def verificar_direccion(self, fila, columna, delta_f, delta_c, ficha):
        conteo = 0
        for d in range(-3, 4):
            f, c = fila + d * delta_f, columna + d * delta_c
            if 0 <= f < self.filas and 0 <= c < self.columnas and self.tablero[f][c] == ficha:
                conteo += 1
                if conteo == 4:
                    return True
            else:
                conteo = 0
        return False

    def reiniciar_partida(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                self.tablero[f][c] = None
                self.labels_tablero[f][c].delete("all")
                self.labels_tablero[f][c].create_oval(5, 5, 45, 45, fill="#23272A")
        self.turno = "Rojo"  # La nueva partida comienza con Rojo
        self.turno_visual.delete("all")
        self.turno_visual.create_oval(5, 5, 25, 25, fill=traducir_color(self.turno))

    def resetear_marcador(self):
        self.marcador = {"Rojo": 0, "Amarillo": 0}
        self.actualizar_marcador()

    def actualizar_marcador(self):
        self.label_marcador.config(text=f"Rojo: {self.marcador['Rojo']} | Amarillo: {self.marcador['Amarillo']}")

if __name__ == "__main__":
    root = tk.Tk()
    juego = ConectaCuatro(root)
    root.mainloop()
