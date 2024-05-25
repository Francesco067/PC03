import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)


if __name__ == "__main__":
  
    mi_circulo = CIRCULO(5)
    area = mi_circulo.calcular_area()
    print(f"El área del círculo con radio {mi_circulo.radio} es {area:.2f}")