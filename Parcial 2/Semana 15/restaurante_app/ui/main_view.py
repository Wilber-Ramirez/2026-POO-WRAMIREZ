from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    def __init__(self, master: tk.Tk, servicio: RestauranteServicio, usuario: Usuario) -> None:
        super().__init__(master, padding=16)
        self.servicio, self.usuario = servicio, usuario
        self.logo = None
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self._crear_cabecera()
        self._crear_navegacion()
        self.contenido = ttk.Frame(self)
        self.contenido.grid(row=1, column=1, sticky="nsew", padx=(16, 0))
        self.mostrar_productos()

    def _crear_cabecera(self) -> None:
        cabecera = ttk.Frame(self)
        cabecera.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 16))
        ruta_logo = Path(__file__).resolve().parents[1] / "assets" / "logo.ppm"
        try:
            self.logo = tk.PhotoImage(file=str(ruta_logo))
            ttk.Label(cabecera, image=self.logo).pack(side="left", padx=(0, 10))
        except tk.TclError:
            pass
        ttk.Label(cabecera, text=f"Restaurante App | Bienvenido, {self.usuario.nombre}",
                  style="Title.TLabel").pack(side="left")

    def _crear_navegacion(self) -> None:
        menu = ttk.LabelFrame(self, text="Navegación", padding=10)
        menu.grid(row=1, column=0, sticky="ns")
        ttk.Button(menu, text="Productos", command=self.mostrar_productos).pack(fill="x", pady=4)
        ttk.Button(menu, text="Usuarios", command=self.mostrar_usuarios).pack(fill="x", pady=4)
        ttk.Button(menu, text="Ventas", command=self.mostrar_ventas).pack(fill="x", pady=4)

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
        self.codigo, self.nombre, self.categoria = tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.precio, self.stock = tk.StringVar(), tk.StringVar()
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
        self.nombre.set(producto.nombre)
        self.categoria.set(producto.categoria)
        self.precio.set(str(producto.precio))
        self.stock.set(str(producto.stock))
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

    def mostrar_ventas(self) -> None:
        self._limpiar()
        ttk.Label(self.contenido, text="Registrar ventas", style="Heading.TLabel").pack(anchor="w")
        formulario = ttk.LabelFrame(self.contenido, text="Nueva venta", padding=12)
        formulario.pack(fill="x", pady=(12, 10))
        self.usuario_venta = tk.StringVar()
        self.producto_venta = tk.StringVar()
        usuarios = self.servicio.listar_usuarios()
        productos = self.servicio.listar_productos()
        ttk.Label(formulario, text="Usuario").grid(row=0, column=0, sticky="w", padx=4)
        ttk.Label(formulario, text="Producto").grid(row=0, column=1, sticky="w", padx=4)
        ttk.Combobox(formulario, textvariable=self.usuario_venta, state="readonly",
                     values=[f"{u.identificacion} - {u.nombre}" for u in usuarios], width=28).grid(
                         row=1, column=0, padx=4, pady=4)
        ttk.Combobox(formulario, textvariable=self.producto_venta, state="readonly",
                     values=[f"{p.codigo} - {p.nombre}" for p in productos], width=28).grid(
                         row=1, column=1, padx=4, pady=4)
        ttk.Button(formulario, text="Registrar venta", command=self.registrar_venta).grid(
            row=1, column=2, padx=8, pady=4)
        self.tabla_ventas = ttk.Treeview(self.contenido,
                                         columns=("fecha", "usuario", "producto"), show="headings")
        for columna, texto in (("fecha", "Fecha"), ("usuario", "Usuario"), ("producto", "Producto")):
            self.tabla_ventas.heading(columna, text=texto)
            self.tabla_ventas.column(columna, width=220)
        self.tabla_ventas.pack(fill="both", expand=True)
        self.actualizar_tabla_ventas()

    def registrar_venta(self) -> None:
        if not self.usuario_venta.get() or not self.producto_venta.get():
            messagebox.showwarning("Venta", "Seleccione un usuario y un producto.")
            return
        usuario_id = self.usuario_venta.get().split(" - ", 1)[0]
        producto_codigo = self.producto_venta.get().split(" - ", 1)[0]
        try:
            venta = self.servicio.registrar_venta(usuario_id, producto_codigo)
        except ValueError as exc:
            messagebox.showerror("Venta no registrada", str(exc))
            return
        self.actualizar_tabla_ventas()
        messagebox.showinfo("Venta registrada", f"Venta guardada el {venta.fecha}.")

    def actualizar_tabla_ventas(self) -> None:
        for fila in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(fila)
        usuarios = {u.identificacion: u.nombre for u in self.servicio.listar_usuarios()}
        productos = {p.codigo: p.nombre for p in self.servicio.listar_productos()}
        for venta in self.servicio.listar_ventas():
            self.tabla_ventas.insert("", "end", values=(venta.fecha, usuarios.get(venta.usuario_id, venta.usuario_id),
                                                        productos.get(venta.producto_codigo, venta.producto_codigo)))
