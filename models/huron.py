# from animal_exotico import Animal_Exotico
from models import animal_exotico

class Huron(animal_exotico.Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        
    def hacer_sonido(self):
        return "¡Eek Eek!"
