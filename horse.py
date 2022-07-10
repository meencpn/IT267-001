class Horse:
    def __init__(self,max_hight:float,name:str,color:str) -> None:
        self.max_hight = max_hight
        self.name = name
        self.color = color

    def run(self):
        print(f'{self.name} is running')

    def show_name(self,name):
        self.name = name

    def show_info(self):
        print(f'Name: {self.name}')
        print(f'Color: {self.color}')
        print(f'Max Hight: {self.max_hight} cm')

if __name__ == "__main__":
    khankhan = Horse(200,"Khan Khan","Gray")
    print("*****Khan Khan*****")
    print(khankhan.show_info())