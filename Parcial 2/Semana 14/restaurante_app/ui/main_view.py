from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    def __init__(self, master: tk.Tk, servicio: RestauranteServicio, usuario: Usuario) -> None:
        super().__init__(master, padding=16)
        self.servicio, self.usuario = servicio, usuario
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self._crear_cabecera()
        self._crear_navegacion()
        self.contenido = ttk.Frame(self)
        self.contenido.grid(row=1, column=1, sticky="nsew", padx=(16, 0))
        self.mostrar_productos()

    def _crear_cabecera(self) -> None:
        ttk.Label(self, text=f"Panel de control | Bienvenido, {self.usuario.nombre}",
                  style="Title.TLabel").grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 16))

    def _crear_navegacion(self) -> None:
        menu = ttk.LabelFrame(self, text="Navegación", padding=10)
        menu.grid(row=1, column=0, sticky="ns")
        ttk.Button(menu, text="Productos", command=self.mostrar_productos).pack(fill="x", pady=4)
        ttk.Button(menu, text="Usuarios", command=self.mostrar_usuarios).pack(fill="x", pady=4)

    def _limpiar(self) -> None:
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_usuarios(self) -> None:
        self._limpiar()
        ttk.Label(self.contenido, text="Usuarios registrados", style="Heading.TLabel").pack(anchor="w")
        tabla = ttk.Treeview(self.contenido, columns=("id", "nombre", "correo"), show="headings")
        for columna, texto in (("id", "Identificación"), ("nombre", "Nombre"), ("correo", "Correo")):
            tabla.heading(columna, text=texto)
            tabla.column(columna, width=180)
        tabla.pack(fill="both", expand=True, pady=(12, 0))
        for usuario in self.servicio.listar_usuarios():
            tabla.insert("", "end", values=(usuario.identificacion, usuario.nombre, usuario.correo))

    def mostrar_productos(self) -> None:
        self._limpiar()
        self.codigo = tk.StringVar()
        self.nombre = tk.StringVar()
        self.categoria = tk.StringVar()
        self.precio = tk.StringVar()
        self.stock = tk.StringVar()
        ttk.Label(self.contenido, text="Gestión de productos", style="Heading.TLabel").pack(anchor="w")
        formulario = ttk.LabelFrame(self.contenido, text="Datos del producto", padding=12)
        formulario.pack(fill="x", pady=(12, 10))
        campos = (("Código", self.codigo), ("Nombre", self.nombre), ("Categoría", self.categoria),
                  ("Precio", self.precio), ("Stock", self.stock))
        for indice, (etiqueta, variable) in enumerate(campos):
            ttk.Label(formulario, text=etiqueta).grid(row=0, column=indice, sticky="w", padx=4)
            ttk.Entry(formulario, textvariable=variable, width=16).grid(row=1, column=indice, padx=4, pady=(4, 0))
        acciones = ttk.Frame(self.contenido)
        acciones.pack(fill="x", pady=(0, 10))
        ttk.Button(acciones, text="Registrar", command=self.registrar).pack(side="left", padx=3)
        ttk.Button(acciones, text="Cargar / consultar", command=self.cargar).pack(side="left", padx=3)
        ttk.Button(acciones, text="Actualizar", command=self.actualizar).pack(side="left", padx=3)
        ttk.Button(acciones, text="Eliminar", command=self.eliminar).pack(side="left", padx=3)
        self.tabla = ttk.Treeview(self.contenido, columns=("codigo", "nombre", "categoria", "precio", "stock"),
                                  show="headings")
        for columna, texto in (("codigo", "Código"), ("nombre", "Nombre"), ("categoria", "Categoría"),
                               ("precio", "Precio"), ("stock", "Stock")):
            self.tabla.heading(columna, text=texto)
            self.tabla.column(columna, width=120)
        self.tabla.pack(fill="both", expand=True)
        self.actualizar_tabla()

    def _datos(self) -> tuple[str, str, str, float, int]:
        if not self.codigo.get().strip():
            raise ValueError("El código es obligatorio.")
        return (self.codigo.get().strip(), self.nombre.get().strip(), self.categoria.get().strip(),
                float(self.precio.get()), int(self.stock.get()))

    def registrar(self) -> None:
        try:
            codigo, nombre, categoria, precio, stock = self._datos()
            if not self.servicio.registrar_producto(Producto(codigo, nombre, categoria, precio, stock)):
                raise ValueError("Ya existe un producto con ese código.")
            self._resultado("Producto registrado correctamente.")
        except (ValueError, TypeError) as exc:
            messagebox.showerror("Datos inválidos", str(exc))

    def cargar(self) -> None:
        producto = self.servicio.buscar_producto(self.codigo.get())
        if producto is None:
            messagebox.showwarning("Consulta", "No se encontró el producto.")
            return
        self.nombre.set(producto.nombre); self.categoria.set(producto.categoria)
        self.precio.set(str(producto.precio)); self.stock.set(str(producto.stock))
        messagebox.showinfo("Consulta", "Producto cargado en el formulario.")

    def actualizar(self) -> None:
        try:
            codigo, nombre, categoria, precio, stock = self._datos()
            if not self.servicio.actualizar_producto(codigo, nombre, categoria, precio, stock):
                raise ValueError("No se encontró el producto.")
            self._resultado("Producto actualizado correctamente.")
        except (ValueError, TypeError) as exc:
            messagebox.showerror("Datos inválidos", str(exc))

    def eliminar(self) -> None:
        if not self.codigo.get().strip():
            messagebox.showerror("Datos inválidos", "Indique el código del producto.")
            return
        if not self.servicio.eliminar_producto(self.codigo.get()):
            messagebox.showwarning("Eliminación", "No se encontró el producto.")
            return
        self._resultado("Producto eliminado correctamente.")

    def _resultado(self, mensaje: str) -> None:
        messagebox.showinfo("Operación completada", mensaje)
        self.actualizar_tabla()

    def actualizar_tabla(self) -> None:
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for producto in self.servicio.listar_productos():
            self.tabla.insert("", "end", values=(producto.codigo, producto.nombre, producto.categoria,
                                                f"{producto.precio:.2f}", producto.stock))
