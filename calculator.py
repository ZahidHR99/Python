num1 = float(input('Enter Number 1 : '))
num2 = float(input('Enter Number 2 : '))
sign = input('Enter sign (+ - / *) : ')

if sign == '+':
    print('The Sum is : ', float(num1 + num2))
elif sign == '-':
    print('The Sub is: ', float(num1 - num2))
elif sign == '/':
    print('The Div is: ', float(num1 / num2))
elif sign == '*':
    print('The Mul is: ', float(num1 * num2))