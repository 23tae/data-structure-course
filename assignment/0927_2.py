class MyStack:
    def __init__(self):
        self.top = []

    def is_empty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.is_empty():
            return self.top.pop(-1)

    def peek(self):
        if not self.is_empty():
            return self.top[-1]


def eval_postfix(expr):
    s = MyStack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if (token == '+'):
                s.push(val1 + val2)
            elif (token == '-'):
                s.push(val1 - val2)
            elif (token == '*'):
                s.push(val1 * val2)
            elif (token == '/'):
                s.push(val1 / val2)
        else:
            s.push(float(token))
    return s.pop()


precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}


def infix_to_postfix(expression):
    stack = MyStack()  # 연산자를 저장할 스택
    postfix = []  # 후위식을 저장할 리스트

    for token in expression:
        if token.isalnum():  # 피연산자일 경우 (숫자나 변수)
            postfix.append(token)
        elif token == '(':  # 여는 괄호일 경우
            stack.push(token)
        elif token == ')':  # 닫는 괄호일 경우
            while stack.is_empty() == False and stack.peek() != '(':
                postfix.append(stack.pop())  # 여는 괄호를 만날 때까지 연산자 추가
            stack.pop()  # 여는 괄호 제거
        else:  # 연산자일 경우
            while stack.is_empty() == False and precedence[stack.peek()] >= precedence[token]:
                postfix.append(stack.pop())  # 우선순위가 낮은 연산자를 만날 때까지 스택에서 팝
            stack.push(token)  # 현재 연산자를 스택에 넣음

    # 스택에 남아있는 모든 연산자를 후위식에 추가
    while stack.is_empty() == False:
        postfix.append(stack.pop())

    return ''.join(postfix)


infix_expressions = ["(2+3)*4", "5*2+3*(3+4)"]
for infix_expression in infix_expressions:
    print(f"중위표기: {infix_expression}")
    postfix_expression = infix_to_postfix(infix_expression)
    print(f"후위표기: {postfix_expression}")
    calculations = eval_postfix(postfix_expression)
    print(f"계산결과: {calculations}\n")
