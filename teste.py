
def reset(lista):
    text = ''
    for box in lista:
        text += box + ','
    return text

items = 'box 1,box 2,'

items += input('Insira uma nova Box: ') + ','

array = items[:-1].split(',')
print (array)

if 'box 3' in array:
    array.remove('box 3')
    items = reset(array)
    print(array)

print (items)

array = items[:-1].split(',')

print (array)

