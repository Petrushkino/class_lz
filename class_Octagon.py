import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Octagon:
    def __init__(self, side: float) -> None:
        self.side = side
        self.angle: float = 135.0
        self.k: float = 1 + math.sqrt(2)
        
    def inscribed_radius(self) -> float:
        return (self.side / 2) * self.k
        
    def inscribed_area(self) -> float:
        return math.pi * (self.inscribed_radius() ** 2)
        
    def circumscribed_radius(self) -> float:
        return (self.side / 2) * math.sqrt(self.k**2 + 1)
        
    def circumscribed_area(self) -> float:
        return math.pi * (self.circumscribed_radius() ** 2)
        
    def perimeter(self) -> float:
        return 8 * self.side
        
    def area(self) -> float:
        return 2 * (self.side ** 2) * self.k
        
    def draw(self) -> None:
        R = self.circumscribed_radius()
        r = self.inscribed_radius()
        
        ax = plt.gca() # Находит активную область для рисования
        
        ax.add_patch(patches.RegularPolygon((0, 0), 8, radius=R, color='green', fill=False))
        ax.add_patch(plt.Circle((0, 0), R, color='blue', fill=False))
        ax.add_patch(plt.Circle((0, 0), r, color='red', fill=False))
        #add_patch прикрепляет двумерную геометрическую фигуру к нашему графику ax
        
        ax.set_aspect('equal')# Фиксирует масштаб осей X и Y в пропорции 1:1
        plt.axis([-R * 1.2, R * 1.2, -R * 1.2, R * 1.2])
        
        plt.show()