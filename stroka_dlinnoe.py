
#Longest in string/

s = "jhifbcweohoewxwaab"
dictionary = "abcdefghijklmnopqrstuvwxyz"
final, promez, invertor_cifr =[], [], []

for litera in s:
    for i in range(len(dictionary)):
        if litera  == dictionary[i]:
            invertor_cifr.append(i)
for i in range(len(invertor_cifr) - 1):
    if invertor_cifr[i] <= invertor_cifr[i + 1]:
        promez.append(invertor_cifr[i])
    else:
        promez.append(invertor_cifr[i])
        final.append(promez)
        promez = []
if promez != []:
    final.append(promez)

if invertor_cifr[-1] < invertor_cifr[-2]:
    promez = []
    promez.append(invertor_cifr[-1])
    final.append(promez)
else:
    final[-1].append(invertor_cifr[-1])
razmer = []
for i in final:
    u = len(i)
    razmer.append(u)
i = 0
a = 0
vtoroi_razmer = []

while i < len(razmer):
    if a >= razmer[i]:
        i += 1
    else:
        a = razmer[i]
        i += 1
i = 0
while i < len(razmer):
    if razmer[i] == a:
        vtoroi_razmer.append(final[i])
    i += 1
otvet = []
for i in range(len(vtoroi_razmer)):
    slo = []
    for j in range(len(vtoroi_razmer[i])):
        slo.append(dictionary[vtoroi_razmer[i][j]])
    otvet.append("".join(slo))

print(" ".join(otvet))
        





    

