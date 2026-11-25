# Solución al Problema 2: Gestión de Menú y Descuentos en Restaurante
# Fase 5 - Evaluación Final (POA) - Fundamentos de Programación
# Estudiante: Luis Fernando Amaya CC79514405
# Grupo:213022-855
# Programa: Ingeniería de Sistemas 
# Curso: Fundamentos de Programación
# Código Fuente: Autoría Propia
"""
Descripción:
Programa estructurado en Python que gestiona el menú de un restaurante almacenado
en una matriz (lista de listas). Evalúa cada producto y aplica un descuento del 15 %
únicamente a aquellos que pertenecen a una categoría objetivo y cuyo precio base
supera un umbral predeterminado.
"""

# ==============================================================================
# 1. DEFINICIÓN DE CONSTANTES GLOBALES
# ==============================================================================
# Categoría que participa en la promoción especial
CATEGORIA_OBJETIVO: str = "Plato Fuerte"

# Precio mínimo requerido para que aplique el descuento (en pesos)
UMBRAL_PRECIO: float = 20000.0

# Porcentaje de descuento a aplicar (15 % equivale a 0.15)
PORCENTAJE_DESCUENTO: float = 0.15


# ==============================================================================
# 2. DEFINICIÓN DE FUNCIONES MODULARES
# ==============================================================================
def calcular_precio_final(categoria: str, precio_base: float) -> float:
    """
    Calcula el precio final de un producto aplicando las reglas de promoción.

    Aplica un descuento del 15 % si el producto pertenece a la categoría
    objetivo y su precio base es estrictamente superior al umbral definido.
    En caso contrario, conserva su valor original.

    Parámetros:
    ----------
    categoria : str
        Nombre de la categoría a la que pertenece el producto.
    precio_base : float
        Precio original del producto antes de evaluar promociones.

    Retorna:
    -------
    float:
        Precio final calculado tras aplicar o no el descuento.
    """
    # Condicional compuesto: evalúa pertenencia a categoría Y superación del umbral
    if categoria == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        descuento = precio_base * PORCENTAJE_DESCUENTO
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base

    return precio_final


def mostrar_reporte_menu(menu: list) -> None:
    """
    Recorre la matriz del menú, calcula los precios e imprime una tabla formateada.

    Parámetros:
    ----------
    menu : list
        Matriz bidimensional donde cada fila representa un producto con la
        estructura: [Nombre (str), Categoría (str), Precio Base (float/int)].
    """
    print("\n" + "=" * 80)
    print("           RESTAURANTE EL BUEN SABOR - REPORTE DE MENÚ Y PROMOCIONES")
    print("=" * 80)
    print(f"Condiciones: {int(PORCENTAJE_DESCUENTO * 100)}% de descuento en '{CATEGORIA_OBJETIVO}' con precio > ${UMBRAL_PRECIO:,.2f}")
    print("-" * 80)
    
    # Encabezado de columnas
    print(f"{'Producto':<22} | {'Categoría':<14} | {'Precio Base':<14} | {'Precio Final':<14} | {'Estado':<10}")
    print("-" * 80)

    # Estructura repetitiva: recorre cada fila (producto) de la matriz
    for item in menu:
        nombre = item[0]
        categoria = item[1]
        precio_base = float(item[2])

        # Llamado a la función para calcular el precio final
        precio_final = calcular_precio_final(categoria, precio_base)

        # Determinación de etiqueta para la tabla
        if precio_final < precio_base:
            estado = "Descuento 15%"
        else:
            estado = "Precio Regular"

        # Impresión de la fila con formato monetario y alineación
        print(f"{nombre:<22} | {categoria:<14} | ${precio_base:>12,.2f} | ${precio_final:>12,.2f} | {estado}")

    print("=" * 80 + "\n")


# ==============================================================================
# 3. PROGRAMA PRINCIPAL
# ==============================================================================
def main() -> None:
    """Función principal que inicializa los datos y ejecuta el flujo del programa."""
    # Matriz del menú (6 productos con diferentes categorías y precios)
    # Formato: [Nombre del producto, Categoría, Precio base]
    menu_restaurante = [
        ["Sopa de Tomate", "Entrada", 12000.0],
        ["Bandeja Paisa", "Plato Fuerte", 28000.0],
        ["Lomo al Trapo", "Plato Fuerte", 35000.0],
        ["Arroz con Pollo", "Plato Fuerte", 18000.0],
        ["Jugo Natural", "Bebida", 8000.0],
        ["Torta de Chocolate", "Postre", 14000.0],
    ]

    # Ejecución del reporte
    mostrar_reporte_menu(menu_restaurante)


# Punto de entrada estándar en Python
if __name__ == "__main__":
    main()
