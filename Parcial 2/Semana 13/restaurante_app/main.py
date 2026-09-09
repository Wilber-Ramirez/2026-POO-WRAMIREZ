from __future__ import annotations

import os
import sys
import tkinter as tk
from pathlib import Path
from typing import Dict

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from restaurante_app.servicios.restaurante_servicio import RestauranteServicio
from restaurante_app.ui.login_view import LoginView
from restaurante_app.ui.main_view import MainView


class App(tk.Tk):
    def __init__(self, ruta_datos: str | None = None) -> None:
        super().__init__()
        self.title("Restaurante App - Semana 13")

        if ruta_datos is None:
            ruta_datos = os.path.abspath(os.path.join(os.path.dirname(__file__), "datos"))

        self.servicio = RestauranteServicio(ruta_datos)

        self.frames: Dict[str, tk.Frame] = {}
        self._setup_frames()
        self.show_frame("LoginView")

    def _setup_frames(self) -> None:
        login = LoginView(self, servicio=self.servicio, on_login=lambda: self.show_frame("MainView"))
        main = MainView(self, servicio=self.servicio, on_logout=lambda: self.show_frame("LoginView"))

        self.frames["LoginView"] = login
        self.frames["MainView"] = main

        login.grid(row=0, column=0, sticky="nsew")
        main.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, name: str) -> None:
        frame = self.frames.get(name)
        if frame is None:
            return
        frame.tkraise()


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
