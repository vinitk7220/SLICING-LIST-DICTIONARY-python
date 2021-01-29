'''
Grocery = ("Shampoo", "Lollypop", "Maggie", "Biscuits", "Chocolate",
           "Salt", "Bread", "Flour", 24, 56)
print(Grocery)
print(Grocery[5])
'''
numbers = [2, 4, 6, 8, 0]
'''
print(numbers[2])  # index 2 print kar dega.
print(numbers.sort())  # mujhe bhi nhi pata "NONE" kyo show ho raha hai.
numbers.sort()  #  sort kar dega (ascending order mai jama dega).
print(numbers)  # hamne pehle sort kiya ab SORT KIYE HUE no's ko print kiya.

numbers.sort()
 numbers.reverse()  # no's ko reverse order mai likh dega (ascending/descending jaruri nhi) jo original list hai use reverse karega.
# agar pehle sort kiya hai fir reverse kiya hai toh DESCENDING order mai ho jayenge.
print(numbers)
'''
# print(numbers[0:4:2])
'''
print(len(numbers))
print(max(numbers))
print(min(numbers))
'''
'''numbers.append(14)
numbers.append(14)
numbers.append(14)
numbers.append(14)
print(numbers)'''
# print(numbers.append(14))  # yeh vahi problem wapas repeat ho gayi "NONE".
# direct print aur append()/sort() nhi kar sakte # pehle sort/append karo fir print kardo.
'''
numbers.insert(3, 23)
print(numbers)
                   # numbers.remove(23, 2)  # TypeError: list.remove() takes exactly one argument (2 given)
numbers.remove(0)
numbers.remove(23)
print(numbers)
'''
'''numbers.pop()  # last no. ko hata dega.
print(numbers)
numbers[1] = 98
print(numbers)
MUTABLE - CAN CHANGE 
IMMUTABLE - Cannot change
'''                 '''
tp = (1, 2, 3, 5)
tp[1] = 23
print(tp)
 '''
# tp = (1, )
# print(tp)
a = 2
b = 76
print(a, b)
a, b = b, a

'''temp = a
a = b
b = temp  # temp = b (nhi kar sakte) temp already defined.
'''
print(a, b)
# python list functions - GOOGLE PLEASE
