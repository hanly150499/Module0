import Constant

print(Constant.SALES_TAX)
print(Constant.SHIPPING_CHARGE)
print(Constant.Price)
x = int(240)
y = float(7.5)
z = str('shoes')
v = str(x)
c = str(y)
b = str('size')
print(v, z, b, c)
p = (Constant.Price * Constant.SALES_TAX + Constant.SHIPPING_CHARGE)
           #p is price of shoes
a = str('are')
print(z, a, p)
