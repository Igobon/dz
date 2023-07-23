# Завдання 1
#
# У списку цілих, заповненому випадковими числами обчислити:
#
# ■ Суму негативних чисел;
#
# ■ Суму парних чисел;
#
# ■ Суму непарних чисел;
#
# ■ Добуток елементів з кратними індексами 3;
#
# ■ Добуток елементів між мінімальним та максимальним елементом;
#
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.


import random

numbers = []
NUMBERS_LENGTH = 10

for i in range(NUMBERS_LENGTH):
    numbers.append(random.randint(-10, 10))

print(numbers)



numbers_sum = 0
# ■ Суму негативних чисел;
for i in range(NUMBERS_LENGTH):
    if numbers[i]<0:
        numbers_sum += numbers[i]

# ■ Суму парних чисел;
double_num=0
print(f"Result numbers_minus: {numbers_sum}")
for i in range(NUMBERS_LENGTH):
    if numbers[i]%2==0:
        double_num += numbers[i]
print(f"Suma double numbers{double_num}")

# ■ Суму непарних чисел;
not_double_number=0
for i in range(NUMBERS_LENGTH):
    if numbers[i]%2==1:
        not_double_number +=numbers[i]
print(f"Not double numbers{not_double_number}")

# ■ Добуток елементів з кратними індексами 3;

n1=numbers [3]
n2=numbers [6]
n3=numbers [9]
dob=n1*n2*n3

print(f'dobutok{dob}')



# ■ Добуток елементів між мінімальним та максимальним елементом;


min_n=min(numbers)
max_n=max(numbers)
dobutok=min_n*max_n
print(f"dobutok{dobutok}")


# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
first_number=0
second_number=0
for i in range(NUMBERS_LENGTH):
    if numbers[i]>0:
        first_number=i
        break
for i in range(NUMBERS_LENGTH-1,-1,-1):
    if numbers [i]>0:
        second_number=i
        break
print(f"first number{first_number}")
print(f"last number{second_number}")
sum_numb=0
for i in range(first_number+1,second_number):
    sum_numb+=numbers[i]
print(f"suma{sum_numb}")

# Завдання 2
#
# Є список цілих, заповнений випадковими числами.
#
# На підставі даних цього масиву потрібно:
#
# ■ Створити список цілих, що містить лише парні числа з першого списку;
#
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
#
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
#
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.

import random

numbers = []
LIST= 10

for i in range(LIST):
    numbers.append(random.randint(-10, 10))

print(numbers)
# ■ Створити список цілих, що містить лише парні числа з першого списку;
n11=[]
i
for i in range(LIST):
    if numbers[i]%2==0:

        n11=numbers[i]

        print(n11,end=", ")
print()
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
n12=[]
for i in range(LIST):
    if  numbers[i]%2==1:
        n12=numbers[i]
        print( n12,end=", ")
print()
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
n13=[]
for i in range(LIST):
    if numbers[i]<0:
        n13=numbers[i]
        print(n13,end=", ")
print()
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.
n14=[]
for i in range(LIST):
    if numbers[i]>0:
        n14=numbers[i]
        print(n14,end=", ")
