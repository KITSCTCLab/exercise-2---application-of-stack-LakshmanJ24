class stackADT:
    def _init_(self):
        self.size = 25
        self.l = [None] * 25
        self.top = -1

    def isFull(self):
        if self.top == self.size - 1:
            return 1
        else:
            return 0

    def isEmpty(self):
        if self.top == (-1):
            return 1
        else:
            return 0

    def Push(self,value):
        if self.isFull() == 1:
            print("The Stack is Full!!")
            print("\n")
        else:
            self.top += 1
            self.l[self.top] = value
            #print("Push operation is done!\n")

    def Pop(self):
        if self.isEmpty() == 1:
            print("The Stack is Empty!!")
            print("\n")
        else:
            k= self.l[self.top]
            self.l[self.top] = None
            self.top -= 1
            return k
            #print("Pop operation is done!\n")

    def Peek(self):
        if self.isEmpty() == 1:
            print("The Stack is Empty!!")
        else:
            print(self.l[self.top])

    def add(self):
        a1=self.Pop()
        a2=self.Pop()
        b=a2+a1
        self.Push(b)

    def sub(self):
        a1 = self.Pop()
        a2 = self.Pop()
        b = a2 - a1
        self.Push(b)

    def mul(self):
        a1 = self.Pop()
        a2 = self.Pop()
        b = a2 * a1
        self.Push(b)

    def div(self):
        a1 = self.Pop()
        a2 = self.Pop()
        b = a2 / a1
        self.Push(b)

stack = stackADT()
a=str(input())
a=a.split(" ")
operator=['*','^','/','-','+']
no_of_digits=0
no_of_op=0
for i in a:
    if i.isdigit():
        no_of_digits+=1
    elif i in operator:
        no_of_op+=1
    else:
        pass

if no_of_digits== (no_of_op+1):

    for i in a:
        if i.isdigit():
            stack.Push(int(i))
        elif i == '+':
            stack.add()
        elif i == '-':
            stack.sub()
        elif i == '*':
            stack.mul()

        elif i == '/':
            stack.div()

    print(int(stack.l[0]))
else:
    print('Invalid postfix expression')

# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
