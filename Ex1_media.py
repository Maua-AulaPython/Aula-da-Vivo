def Media(x, y, z):
	M = (x+y+z)/3
	return M

a = float(raw_input("Nota da P1: "))
b = float(raw_input("Nota da P2: "))
c = float(raw_input("Nota da P3: "))
print("A sua media sera: {0}".format(Media(a,b,c)))
