class Parrot:
    speices="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=Parrot("blu",10)
woo=Parrot("woo",15)
print("blu is a {}".format(blu.speices))
print("woo os a {}".format(woo.speices))
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))
        