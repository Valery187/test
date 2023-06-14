# Есть строка-подсчитать кол-во каждой из букв в строке

# aabccdcd

# def strconter(s):
#     for symbol in s: # отвечает за перебор искомых значений
#         counter=0
#         for sub_symbol in s: # отвечает за подсчет количества искомого символа в строке
#             if symbol==sub_symbol:
#                 counter +=1
#         print (symbol,counter)
#
# strconter('aabccdcd')   # буквы выводятся по несколько раз

# Множество-список только уникальных значений 'aabccdcd'->'abcd'

# def strconter(s):
#     for symbol in set(s):  # используется Множество
#         counter = 0
#         for sub_symbol in s:
#             if symbol == sub_symbol:
#                 counter += 1
#         print(symbol, counter)
#
#
# print(set('aabccdcd'))  # Множество
# strconter('aabccdcd')  # буквы выводятся по одному разу

# Оптимизация кода с помощью словаря
def strconter(s):
    syms_counter = {}
    for symbol in s:
        syms_counter[symbol] = syms_counter.get(symbol, 0) + 1

    for symbol, count in syms_counter.items():
        print (symbol, count)

# strconter('aabccdcd')
strconter('hello word')