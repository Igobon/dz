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


print("Start task 1")
# ■ Суму негативних чисел;
import random

numbers = []
NUMBERS_LENGTH = 10

for i in range(NUMBERS_LENGTH):
    numbers.append(random.randint(-10, 10))

print(numbers)



negative_sum = 0

for i in range(NUMBERS_LENGTH):
    if numbers[i]<0:
        negative_sum += numbers[i]
print(f"negative_sum= {negative_sum}")
# ■ Суму парних чисел;
import random

numbers = []
NUMBERS_LENGTH = 10

for i in range(NUMBERS_LENGTH):
    numbers.append(random.randint(-10, 10))

print(numbers)

sum_even_numbers=0

for i in range(NUMBERS_LENGTH):
    if numbers[i]%2==0:
        sum_even_numbers += numbers[i]
print(f"sum_even_numbers= {sum_even_numbers}")

# ■ Суму непарних чисел;
import random

numbers = []
NUMBERS_LENGTH = 10

for i in range(NUMBERS_LENGTH):
    numbers.append(random.randint(-10, 10))

print(numbers)
sum_not_even_numbers=0
for i in range(NUMBERS_LENGTH):
    if numbers[i]%2==1:
        sum_not_even_numbers +=numbers[i]
print(f"Sum_not_even_numbers= {sum_not_even_numbers}")

# ■ Добуток елементів з кратними індексами 3;
import random

numbers = []
NUMBERS_LENGTH = 10

for i in range(NUMBERS_LENGTH):
    numbers.append(random.randint(-10, 10))

print(numbers)
n1=numbers [3]
n2=numbers [6]
n3=numbers [9]
dobutok=n1*n2*n3

print(f'Dobutok index/3= {dobutok}')



# ■ Добуток елементів між мінімальним та максимальним елементом;
import random

numbers = []
NUMBERS_LENGTH = 10

for i in range(NUMBERS_LENGTH):
    numbers.append(random.randint(-10, 10))

print(numbers)

min_n=min(numbers)
max_n=max(numbers)
dobutok=min_n*max_n
print(f"minimal_number= {min_n}")
print(f"max_number= {max_n}")
print(f"dobutok= {dobutok}")


# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
import random

numbers = []
NUMBERS_LENGTH = 10

for i in range(NUMBERS_LENGTH):
    numbers.append(random.randint(-10, 10))

print(numbers)

first_positive_number=0
last_positive_number=0
for i in range(NUMBERS_LENGTH):
    if numbers[i]>0:
        first_positive_number=i
        break
for i in range(NUMBERS_LENGTH-1,-1,-1):
    if numbers [i]>0:
        last_positive_number=i
        break
print(f"first_positive_number= {first_positive_number}")
print(f"last_positive_number= {last_positive_number}")
sum_numb=0
for i in range(first_positive_number+1,last_positive_number):
    sum_numb+=numbers[i]
print(f"suma= {sum_numb}")
print("Task number 2")
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


# ■ Створити список цілих, що містить лише парні числа з першого списку;
import random

numbers = []
LIST= 10

for i in range(LIST):
    numbers.append(random.randint(-10, 10))

print(numbers)

even_numbers=[]

for i in range(LIST):
    if numbers[i]%2==0:

        even_numbers=numbers[i]

        print(even_numbers,end=", ")
print("even_numbers")


# ■ Створити список цілих, що містить лише непарні числа з першого списку;
numbers = []
LIST= 10

for i in range(LIST):
    numbers.append(random.randint(-10, 10))

print(numbers)
not_even_numbers=[]
for i in range(LIST):
    if  numbers[i]%2==1:
        not_even_numbers=numbers[i]
        print( not_even_numbers,end=", ")
print("not_even_numbers")


# ■ Створити список цілих, що містить лише негативні числа з першого списку;
import random

numbers = []
LIST= 10

for i in range(LIST):
    numbers.append(random.randint(-10, 10))

print(numbers)

negative_numbers=[]
for i in range(LIST):
    if numbers[i]<0:
        negative_numbers=numbers[i]
        print(negative_numbers,end=", ")
print("negative_numbers")


# ■ Створити список цілих, що містить лише позитивні числа з першого списку.
import random

numbers=[]
LIST=10
for i in range(LIST):
    numbers.append(random.randint(-10, 10))

print(numbers)


positive_numbers=[]
for i in range(LIST):
    if numbers[i]>0:
        positive_numbers=numbers[i]
        print(positive_numbers,end=", ")
print("positive_numbers")
