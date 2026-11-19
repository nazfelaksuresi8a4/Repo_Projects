#dunder methodlar pythonda bir işlem yaptığımız zaman arkada çalışan metodlardır.
#örnek olarak x == y dediğimiz zaman __eq__ metodu çalışır.

class MyList:
    def __init__(self,items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self,key,item):
        self.items[key] = item

    def __delitem__(self, key):
        del self.items[key]


my_list = MyList([10,20,30])        #liste sınıfı tanımlarız

birinci_item = my_list[0]       #init ile items tanımlayıp sınıfı liste gibi kullanırız ve __getitem__ sayesinde itemleri döndürebiliriz.
print(my_list[0]) 
my_list[0] = 14         #sınıfı liste gibi kullanıp __setitem__ metodu ile var olan bir indeksi set yapısı gibi değiştirebiliriz.
print(my_list[0])
del my_list[0]          #__delitem__ metodu ile var olan bir itemi belirterek silebiliriz
print(list(my_list))    #mylist bir sınıftır bu nedenle list ile onu gerçek listeye çeviririz (sınıftır ancak liste metodlarını içerir dunderler sayesinde)

