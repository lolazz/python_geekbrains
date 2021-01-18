def translate(a):
    if a == 'One':
        return 'Один'
    elif a == 'Two':
        return 'Два'
    elif a == 'Three':
        return 'Три'
    elif a == 'Four':
        return 'Четыре'


rich = []
new_file = open('part4_new_file.txt', 'w+')
with open("part4.txt", "r") as f:
    for line in f:
        a, b = line.split(' - ')
        new_file.write(f'{translate(a)} - {b}')
print(rich)
