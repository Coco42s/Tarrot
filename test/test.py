import time
a = []
b = []
c = []

carteDistri = [1,2,3,4,5,6,7,8,9,
               10,11,12,13,14,15,16,17,18,19,
               20,21,22,23,24,25,26,27,28,29,
               30,31,32,33,34,35,36,37,38,39,
               40,41,42,43,44,45,46,47,48,49,
               50,51,52,53,54,55,56,57,58,59,
               60,61,62,63,64,65,66,67,68,69,
               70,71,72,73,74,75,76,77,78]

ch = 6
n = 3
for i in range(1,int(((78-ch)/3)/3+1)):
    for i in range(n):
        a.append(carteDistri[0])
        b.append(carteDistri[1])
        c.append(carteDistri[i+2])
        carteDistri = carteDistri[3:]
        time.sleep(0.5)
        
print(a,len(a))
print(b,len(b))
print(c,len(c))

print(carteDistri)
