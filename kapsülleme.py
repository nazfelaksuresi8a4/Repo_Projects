class Animal:    #ana sınıf
    def __init__(self,name,prop):
        self.name = name    
        self.prop = prop


class Dog(Animal):    #alt sınıf
    def __init__(self,name,prop):      #tanımlama sırası üstteki ile aynı olmalıdır
        super().__init__(name,'kedi')    #üst sınıfa erişir ve super init içindeki name ve prop ile değiştirir


kopek = Dog('dog','animal')
print(kopek.prop)  #animal gelmez çünkü kedi olarak değiştirdik.
