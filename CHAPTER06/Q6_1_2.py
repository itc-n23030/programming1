class person:
    def __init__(self, name="", nationality="", birth="", address=""):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print(f"name: {self.name}")
        print(f"nationality: {self.nationality}")
        print(f"birth: {self.birth}")
        print(f"address: {self.address}")


heroin = person("かぐや姫", "日本", "685", "静岡県、富士市")
print(heroin.show_attributes())
