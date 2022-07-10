class JuiceOder:
    def __init__(self,menu:str,size='R') -> None:
        self.menu = menu.upper()
        self.size = size.upper()
        self.price = 0

    def check_menu(self):
        menu_dictionary = {
                        'OJ':25,
                        'AJ':25,
                        'WJ':30,
                        'PJ':30}
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)
    def compute_price(self):
        if self.size == 'L':
            self.price += 5
        else:
            self.price
        
        JuiceOder.total = self.price

    def display_order(self):
        self.check_menu()
        self.compute_price()
        return f'{self.menu}({self.size} * {self.price}) => {JuiceOder.total} bath'

if __name__ == "__main__":
    order1 = JuiceOder("WJ","L")
    order2 = JuiceOder("OJ","R")
    order3 = JuiceOder("PJ","L")

    print(order1.display_order())
    print(order2.display_order())
    print(order3.display_order())
