class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho


if __name__ == "__main__":
    rectangulo01 = Rectangulo(5, 10)
    area_rectangulo01 = rectangulo01.calcular_area()
    print("Área del rectángulo 1:", area_rectangulo01)