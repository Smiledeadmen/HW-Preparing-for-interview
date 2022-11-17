some_stack = '(((([{}]))))'

class Stack:

    def __init__(self, stack):
        self.stack = [_ for _ in stack]

    def isEmpty(self) -> bool:
        '''Метод проверяет стек на пустоту'''
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element) -> None:
        '''Метод добавляет новый элемент на вершину стека'''
        self.stack.append(element)

    def pop(self):
        '''Метод удаляет верхний элемент стека. Стек изменяется'''
        return self.stack.pop()

    def peek(self):
        '''Метод возвращает верхний элемент стека, но не удаляет его'''
        return self.stack[-1]

    def size(self) -> int:
        '''Метод возвращает количество элементов в стеке'''
        return len(self.stack)

if __name__ == '__main__':
    st = Stack(some_stack)
    res1 = st.isEmpty()
    res2 = st.push('111')
    res3 = st.pop()
    res4 = st.peek()
    size = st.size()
