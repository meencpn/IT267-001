from donkey import Donkey
from horse import Horse
class Mule(Donkey,Horse):
    def __init__(self, name:str, color:str, age: int, weight: float) -> None:
        super().__init__(name, color, age, weight)
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight

    def run(self):
        print("Mule is running")

    def show_info(self):
        super().show_info()
        print(f'Name: {self.name}')
        print(f'Color: {self.color}')
        print(f'Max Hight: {self.max_hight}')
        print(f'Age: {self.age}-year-old')
        print(f'Weight: {self.weight} kg')

if __name__ == "__main__":
    mule1 = Donkey("Blue-eyed cream",200,"Mumu",3)
    mule2 = Donkey("Palomino",120.7,"Meme",3)

    print(mule1.show_info())
    print(mule2.show_info())