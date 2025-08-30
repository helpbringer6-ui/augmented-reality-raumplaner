import sys

class Raumplaner:
    def __init__(self):
        self.moeebel = []

    def moebel_hinzufuegen(self, moebel):
        self.moeebel.append(moebel)

    def anzeigen(self):
        for m in self.moeebel:
            print(f"Möbel: {m}")

if __name__ == '__main__':
    raumplaner = Raumplaner()
    raumplaner.moebel_hinzufuegen("Sofa")
    raumplaner.moebel_hinzufuegen("Tisch")
    raumplaner.anzeigen()