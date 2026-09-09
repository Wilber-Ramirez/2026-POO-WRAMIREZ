from __future__ import annotations

import tkinter as tk
from tkinter import scrolledtext
from typing import Callable


class MainView(tk.Frame):
    def __init__(self, master: tk.Tk, servicio, on_logout: Callable[[], None]) -> None:
        super().__init__(master)
        self.servicio = servicio
        self.on_logout = on_logout
        self._build()

    def _build(self) -> None:
        titulo = tk.Label(self, text="Panel principal - Restaurante", font=(None, 14, "bold"))
        titulo.grid(row=0, column=0, columnspan=3, pady=(10, 10))

        btn_usuarios = tk.Button(self, text="Usuarios", width=15, command=self.mostrar_usuarios)
        btn_usuarios.grid(row=1, column=0, padx=5, pady=5)

        btn_productos = tk.Button(self, text="Productos", width=15, command=self.mostrar_productos)
        btn_productos.grid(row=1, column=1, padx=5, pady=5)

        btn_ventas = tk.Button(self, text="Ventas (pendiente)", width=15, state=tk.DISABLED)
        btn_ventas.grid(row=1, column=2, padx=5, pady=5)

        self.txt_salida = scrolledtext.ScrolledText(self, width=60, height=15, state=tk.DISABLED)
        self.txt_salida.grid(row=2, column=0, columnspan=3, padx=10, pady=(5, 10))

        btn_logout = tk.Button(self, text="Cerrar sesión", command=self.on_logout)
        btn_logout.grid(row=3, column=2, sticky="e", padx=10, pady=(0,10))

    def _write(self, texto: str) -> None:
        self.txt_salida.config(state=tk.NORMAL)
        self.txt_salida.delete("1.0", tk.END)
        self.txt_salida.insert(tk.END, texto)
        self.txt_salida.config(state=tk.DISABLED)

    def mostrar_usuarios(self) -> None:
        usuarios = self.servicio.listar_usuarios()
        if not usuarios:
            self._write("No hay usuarios registrados.")
            return
        texto = "Usuarios registrados:\n\n"
        for u in usuarios:
            texto += f"- {u}\n"
        self._write(texto)

    def mostrar_productos(self) -> None:
        productos = self.servicio.listar_productos()
        if not productos:
            self._write("No hay productos registrados.")
            return
        texto = "Productos registrados:\n\n"
        for p in productos:
            texto += f"- {p}\n"
        self._write(texto)
