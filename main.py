#Шифровки
message = input("Введите сообщение: ")
#1
cipher_one = message.replace('и', 'o')
print("Первый шифр: " + cipher_one)
#2
cipher_two = message[::-1]
print("Второй шифр: " + cipher_two)
#3
cipher_three = message[::2] + message[1::2]
print("Третий шифр: "+ cipher_three)
#4
first_symbol = message[0]
last_symbol = message[-1]

length = len(message)

cipher_four = last_symbol + message[1:length-1] + first_symbol
print("Четвертый шифр: " + cipher_four)
#5
cipher_five = message
half_length = len(message)//2
cipher_five = message[half_length:] + message[:half_length]
print("Пятый шифр: " + cipher_five)
#Рассшифровки
#1 
cipher_one = message.replace('о', 'и')
print("Первая расшифровка: " + cipher_one)
#2
print("Вторая расшифровка: " + cipher_two[::-1])
#3
result = '' 
even = message[::2]
odd = message[1::2]
counter = 0

for symbol in even:
    result+=symbol 
    if counter<len(odd):
        result+=odd[counter]
    counter+=1
print('Третья расшифровка:',result)
#4
first_letter = cipher_four[-1]
last_letter = cipher_four[0]

length = len(cipher_four)

cipher_four = first_symbol + message[1:length-1] + last_symbol
print("Четвертая расшифровка: " + cipher_four)
#5
half_length = len(message)//2
cipher_five = cipher_five[half_length:] + cipher_five[:half_length]
print("Пятая расшифровка: " + cipher_five)





