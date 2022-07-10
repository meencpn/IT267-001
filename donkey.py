class Donkey:
    def __init__(self,age: int, weight: float) -> None:
        self.age = age
        self.weight = weight

    def sound(self):
        print("Donkey makes eeyore sound")

    def show_info(self):
        print(f'Age: {self.age}-year-old')
        print(f'Weight: {self.weight} kg')

if __name__ == "__main__":
    donkey1 = Donkey(2,100)

    print("Donkey makes eeyore sound")
    print(donkey1.show_info())