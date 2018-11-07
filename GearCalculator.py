import math
j = int(input("Numero de Engrenagens: "))
z = [None]*j
m = [None]*j
o = [None]*j
dp = [None]*j
di = [None]*j
de = [None]*j
db = [None]*j
p = [None]*j
s = [None]*j
sc = [None]*j
dia = [True]*j

for i in range(j):
    print("Engrenagem: "+str(i))
    z[i] = int(input("Numero de Dentes: "))
    m[i] = int(input("Numero do Modulo: "))
    o[i] = float(input("Numero do Angulo: "))
    print("")

for i in range(j):
    dp[i] = (m[i]*z[i])
    di[i] = m[i]*(z[i]-2.334)
    de[i] = m[i]*(z[i]+2)
    db[i] = (dp[i])*(math.cos(math.radians(o[i])))
    p[i] = (3.14)*m[i]
    s[i] = p[i]/2
    sc[i] = (dp[i])*(math.sin(math.radians(o[i])))
    if(db[i]<=di[i]):
        dia[i] = False

for i in range(j):
    print("Engrenagem: "+str(i))
    print("Diamentro Interno: "+str(di[i]))
    print("Diamentro de Base: "+str(db[i]))
    print("Diamentro Primitivo: "+str(dp[i]))
    print("Diamentro Externo: "+str(de[i]))
    print("Passo: "+str(p[i]))
    print("Engrenagem da Certo? "+str(dia[i]))
    print(" ")
