import datetime
import uuid  # Para generación de IDs únicos
from typing import List, Dict, Optional

class Producto:
    def __init__(self, id: str, nombre: str, descripcion: str, precio: float, fecha_creacion: datetime.datetime):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.fecha_creacion = fecha_creacion

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "fecha": self.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")
        }

def existe_id(productos: List[Producto], codigo: str) -> bool:
    """Verifica si un ID ya existe en la lista de productos"""
    return any(p.id == codigo for p in productos)

def existe_nombre(productos: List[Producto], nombre: str) -> bool:
    """Verifica si un nombre de producto ya existe (insensible a mayúsculas)"""
    return any(p.nombre.lower() == nombre.lower() for p in productos)

def generar_id_unico() -> str:
    """Genera un ID único usando UUID"""
    return f"PRO_{uuid.uuid4().hex[:8].upper()}"

def validar_precio(precio_str: str) -> Optional[float]:
    """Valida el precio ingresado y lo devuelve como float o None si es inválido"""
    try:
        precio = float(precio_str)
        return precio if precio >= 0 else None
    except ValueError:
        return None

def agregar_producto(productos: List[Producto]) -> None:
    print("\n==== Agregar Producto ====")
    
    # Generar ID único
    id_producto = generar_id_unico()
    print(f"ID generado automáticamente: {id_producto}")

    # Validación del nombre
    nombre_producto = ""
    while not nombre_producto:
        nombre_producto = input("Nombre del producto: ").strip().title()
        if not nombre_producto:
            print("❌ Error: El nombre no puede estar vacío")
            continue
            
        if existe_nombre(productos, nombre_producto):
            print("⚠️ Advertencia: Ya existe un producto con este nombre")
            confirmacion = input("¿Desea continuar de todos modos? (s/n): ").lower()
            if confirmacion != 's':
                nombre_producto = ""

    # Validación de descripción
    descripcion = input("Descripción: ").strip()
    
    # Validación del precio
    precio = None
    while precio is None:
        precio_input = input("Precio: ").strip()
        precio = validar_precio(precio_input)
        if precio is None:
            print("❌ Error: Debe ingresar un número válido no negativo")

    # Crear nuevo producto
    nuevo_producto = Producto(
        id=id_producto,
        nombre=nombre_producto,
        descripcion=descripcion,
        precio=precio,
        fecha_creacion=datetime.datetime.now()
    )

    productos.append(nuevo_producto)
    print(f"\n✅ Producto '{nombre_producto}' agregado exitosamente!")
    print(f"ID: {id_producto} | Precio: ${precio:.2f}\n")