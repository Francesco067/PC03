def es_numero(valor):
    return isinstance(valor, (int, float))

def suma(a, b):
    if not es_numero(a) or not es_numero(b):
        return "Error: Tipo de dato no válido."
    return a + b

def resta(a, b):
    if not es_numero(a) or not es_numero(b):
        return "Error: Tipo de dato no válido."
    return a - b

def producto(a, b):
    if not es_numero(a) or not es_numero(b):
        return "Error: Tipo de dato no válido."
    return a * b

def division(a, b):
    try:
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido."
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero."