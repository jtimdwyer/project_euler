with open('p22.txt') as file:
    l = list(file)

l = l[0].split(',')
l = [name.replace('"','') for name in l]
l.sort()

total = 0
for position, name in enumerate(l,1):
    if name == 'COLIN':
        print(position, name.lower())
    alph_value = sum(ord(char) - 96 for char in name.lower())
    total += position * alph_value


print(total)
