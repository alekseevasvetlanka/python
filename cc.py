# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран
 
# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
 
# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print ("Привет! Начнем.")

a = 4
b = 3
print (a , b)

name = input("Как тебя зовут?");
print ("Привет, " + name);

number = input("Загадай число")
print ("Ты загадал:" + str(number));
c = int(number)
print ("Если к твоему числу прибавить 2, получится:")
print (c + 2)

age = int(input("Сколько тебе лет?"));
if age >= 18:
	print ("Доступ разрешен")
else:
	print ("Извините, пользование данным ресурсом только с 18 лет")

