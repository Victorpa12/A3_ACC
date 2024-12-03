upos = '(123,134)'
upos9 = upos.split("(")
print(upos9)
upos0 = upos9[1].split(')')
print(upos0)
ipos = upos0[0].split(",")
print(ipos)
pos = (int(ipos[0]), int(ipos[1]))
print(pos)
