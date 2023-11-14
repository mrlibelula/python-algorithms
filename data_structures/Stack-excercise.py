from collections import deque

class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]  # doesn't remove the item from the stack

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
    
def reverse_string(string):
    reversed_string = ''
    
    s = Stack()
    for char in string:
        s.push(char)
        
    while s.size():
        reversed_string += s.pop()
        
    return reversed_string

def is_balanced(string):
    # checks if parenthesis in the string are balanced
    parenthesis = [['(', ')'], ['[', ']'], ['{', '}'], ['<', '>']]
    opened = []
    closed = []
    for group in parenthesis:
        opened.append(group[0])
        closed.append(group[1])
    
    s = Stack()
    for character in string:
        if character in opened:
            s.push(character)
        if character in closed:
            if s.size() == 0 or not is_match(character, s.pop(), parenthesis):
                return False
    return s.size() == 0
    
def is_match(char1, char2, group_symbols):
    match = {}
    for symbols in group_symbols:
        match[symbols[1]] = symbols[0]
    return match[char1] == char2

if __name__ == '__main__':
    print(reverse_string('We will conquer COVID-19'))
    
    print(is_balanced('({a+b})'))               # True
    print(is_balanced('))((a+b}{'))             # False
    print(is_balanced('((a+b))'))               # True
    print(is_balanced('))'))                    # False
    print(is_balanced('[a+b]*(x+2y)*{gg+kk}'))  # True
    print(is_balanced('(a+b) + c]'))            # False