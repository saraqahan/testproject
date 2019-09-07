x,y,z="apple","orange","limon"
basket=x+y+z
x_len = len(x)
y_len = len(y)
z_len = len(z)
print(basket[:x_len], basket[x_len:y_len+x_len], basket[-1*z_len:])
