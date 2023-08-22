class Nigiri:
    category = "にぎり"
    top = "ねた"
    base = "しゃり"

    def show_attributes(self):
        print(f"top: {self.top}, base: {self.base}, category: {self.category}")


class katsuo(Nigiri):
    top = "カツオ"
    topping = "生姜とねぎ"
    price = 100

    def show_attributes(self):
        super().show_attributes()
        print(f"price: {self.price}円")
        print(f"topping: {self.topping}")


a = katsuo()
print(a.show_attributes())
