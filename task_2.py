from main import Stack

def balance_parentheses(text):
    stc = Stack(text)
    tmp = []
    balance = False
    if stc.size() % 2 == 0:
        balance = True
        for el in range(stc.size()):
            element = stc.pop()
            if element in '({[':
                del tmp[-1]
                continue
            tmp.append(element)
    else:
        balance = False

    if balance and len(tmp) == 0:
        print("Сбалансированно")
    else:
        print("Несбалансированно")


balance_parentheses('}{}')

# Пример сбалансированных последовательностей скобок:
#
#     (((([{}]))))
#     [([])((([[[]]])))]{()}
#     {{[()]}}
#
# Несбалансированные последовательности:
#
#     }{}
#     {{[(])]}}
#     [[{())}]