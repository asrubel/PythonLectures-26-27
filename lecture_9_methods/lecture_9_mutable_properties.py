class River:
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        print(f"{self.name} was created!")
        River.all_rivers.append(self)

    def __str__(self):
        return f"{self.name} has length of {self.length} km."

    def show_info(self):
        print(self)


dnipro = River("Dnipro", 2000)
dnipro.show_info()
print(River.all_rivers)
print(dnipro.all_rivers)

dnistro = River("Dnistro", 1500)
dnistro.show_info()
print(River.all_rivers)

danube = River("Danube", 3000)
danube.show_info()
print(River.all_rivers)
print(danube.all_rivers)

for river in River.all_rivers:
    river.show_info()
