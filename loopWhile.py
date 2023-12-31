a = 1
while a <= 5:
    print(a)
    a = a + 1


#comment couple of rows: ctrl/

a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1
    #В цьому прикладі умова циклу буде виконуватися завжди, адже True завжди буде True. Це приклад нескінченного циклу. Але через перевірку, що a >= 20,
    #  цей цикл завершиться, щойно в a буде значення 20 або більше.
#Нескінченні цикли часто застосовуються там, де потрібно взаємодіяти з клієнтом, чекаючи введення від нього, і завершується тільки при настанні деякої умови.
#Наприклад echo скрипт, який виводить в консоль те, що ви введете, доки ви не введете exit:

while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break


# Також для того, аби одразу перейти до наступної ітерації циклу без виконання виразів, що залишилися, є команда continue. Виклик цієї команди у тілі циклу
# призводить до того, що вирази цієї ітерації, що залишилися, не будуть виконані, а інтерпретатор одразу перейде до наступної ітерації або перевірки умови.
#Інструкція print(a) не виконувалась, коли a ділилося на 2 без залишку, оскільки ітерація завершувалася за допомогою continue.
a = 0
while a < 6:
    a = a + 1
    if not a % 2:# число НЕ ділиться без залишку - тобто число парне
        continue # перериває цей цикл і починає наступний
    print(a)


#Оператори continue та break працюють тільки всередині одного циклу. В ситуації вкладених циклів немає способу вийти з усіх циклів одразу.

while True:
    number = input("number = ")
    number = int(number)
    while True:
        print(number)
        number = number - 1
        if number < 0:
            break
    break

