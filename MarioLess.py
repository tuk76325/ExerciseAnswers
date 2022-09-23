num = int(input('Please input an integer value from 1 - 8. '))
jfif = num

while num > 8 or num < 1:
    num = int(input('Please input an integer value that is between or including 1 and 8. '))
    jfif = num
while 1 <= num <= 8:
    i = 1
    while i <= jfif:
        print((num-1) * ' ', i * '#')
        i = i + 1
        num = num - 1
