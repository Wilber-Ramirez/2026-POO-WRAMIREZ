from __future__ import annotations

import tkinter as tk
from typing import Callable


class LoginView(tk.Frame):
    def __init__(self, master: tk.Tk, servicio, on_login: Callable[[], None]) -> None:
        super().__init__(master)
        self.servicio = servicio
        self.on_login = on_login
        self._build()

    def _build(self) -> None:
        self.columnconfigure(0, weight=1)

        titulo = tk.Label(self, text="Acceso - Restaurante App", font=(None, 14, "bold"))
        titulo.grid(row=0, column=0, pady=(10, 10))

        frm = tk.Frame(self)
        frm.grid(row=1, column=0, padx=20, pady=10)

        tk.Label(frm, text="Identificación:").grid(row=0, column=0, sticky="w")
        self.entry_id = tk.Entry(frm)
        self.entry_id.grid(row=0, column=1, pady=4)

        tk.Label(frm, text="Contraseña (correo):").grid(row=1, column=0, sticky="w")
        self.entry_clave = tk.Entry(frm, show="*")
        self.entry_clave.grid(row=1, column=1, pady=4)

        self.lbl_mensaje = tk.Label(self, text="", fg="red")
        self.lbl_mensaje.grid(row=2, column=0)

        btn_login = tk.Button(self, text="Ingresar", command=self._on_ingresar)
        btn_login.grid(row=3, column=0, pady=(8, 0))

    def _on_ingresar(self) -> None:
        identificacion = self.entry_id.get().strip()
        clave = self.entry_clave.get().strip()

        if not identificacion or not clave:
            self.lbl_mensaje.config(text="Complete usuario y contraseña.")
            return

        if self.servicio.validar_acceso(identificacion, clave):
            self.lbl_mensaje.config(text="", fg="green")
            self.on_login()
        else:
            self.lbl_mensaje.config(text="Credenciales incorrectas.", fg="red")
