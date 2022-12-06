#Шифровки
message = input("Введите сообщение: ")
#1
cipher_one = message
cipher_one = message.replace('и', 'o')
print("Первый шифр: " + str(cipher_one))
#2
cipher_two = message
print("Второй шифр: " + str(cipher_two[::-1]))
#3
cipher_three = message[::2] + message[1::2]
print("Третий шифр: "+ str(cipher_three))
#4
cipher_four = message
first_letter = cipher_four[0]
last_letter = cipher_four[-1]

length = len(cipher_four)

cipher_four = last_letter + message[1:length-1] + first_letter
print("Четвертый шифр: " + str(cipher_four))
#5
cipher_five = message
half_length = len(message)//2

cipher_five = message[half_length:] + message[:half_length]
print("Пятый шифр: " + str(cipher_five))
#Рассшифровки
#1 
cipher_one = message.replace('о', 'и')
print("Первая расшифровка: " + str(cipher_one))
#2
print("Вторая расшифровка: " + str(cipher_two[::1]))
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
last_letter = cipher_four[-0]

length = len(cipher_four)

cipher_four = first_letter + message[1:length-1] + last_letter
print("Четвертая расшифровка: " + str(cipher_four))
#5
half_length = len(message)//2
cipher_five = message[:half_length] + message[half_length:]
print("Пятая расшифровка: " + str(cipher_five))




