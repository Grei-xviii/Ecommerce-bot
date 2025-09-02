print('hello world')

total = 0
while total < 10:
    total += 1
    print(total)


for i in range(5):
    print(i)
 

list1 = ['A','B', 'C', 'D', 'E']
list1[4] = 'nill'
print(list1)
print(list1[3])
print(list1[2:])


numbers = [3, 4, 6, 14, 2, 43]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)