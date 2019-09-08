#age=36
#txt= "My name is Jhon, I am "+ age
#print(txt)
age=36
txt= "My name is Jhon, I am {}"
print(txt.format(age))
quantity=3
itemno=567
price=49.65
myorder="I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity , itemno, price))
quantity=3
itemno=567
price=49.65
myorder="I want to pay {2} dollars for{0}  pieces of item{1}."
print(myorder.format(quantity , itemno, price))
