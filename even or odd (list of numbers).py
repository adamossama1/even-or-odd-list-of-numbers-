

numbers=(input('enter the numbers:'))
print(numbers)

x=numbers.split(',')
print(x)
even=[]
odd=[]
for number in x:
    if int(number)%2==0:
        even.append(int(number))
        

    else:
        odd.append(int(number))
        
print('even :')
print(even)

print('odd :')
print(odd)
