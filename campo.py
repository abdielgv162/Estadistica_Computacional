class Campo:
    def __init__(self):
        self.coordenadas_de_persona = {}

    def anadir_persona(self, persona, coordenada):
        self.coordenadas_de_persona[persona] = coordenada

    def mover_persona(self, persona):
        delta_x, delta_y = persona.camina()
        coordenada_actual = self.coordenadas_de_persona[persona]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_persona[persona] = nueva_coordenada

    def obtener_coordenada(self, persona):
        return self.coordenadas_de_persona[persona]