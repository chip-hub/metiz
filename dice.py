from random import randint

class Dice():
    """Класс - игральная кость"""
    def __init__(self, n=6):
        self.namber_faces = n

    def roll_dice(self, k=1):
        if k == 1:
            self.res_roll = randint(1, self.namber_faces)
        else:
            self.res_roll = [randint(1, self.namber_faces) for i in range(k)]
        
        return self.res_roll