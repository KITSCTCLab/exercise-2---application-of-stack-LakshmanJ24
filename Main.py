class Evaluate:
  def __init__(self, size):
    self.items = [None]*size
    self.size = size
    self.top = -1  

  def isEmpty(self):
    if self.top == -1 :
      return 1
    else :
      return 0
    
  def isFull(self):
    if self.top==(self.size-1):
      return 1
    else:
      return 0

  def pop(self):
    if not self.isEmpty():
      t=self.lst[self.top]
      del self.lst[self.top]
      self.top-=1
      return t

  def push(self, operand):
    if not self.is_full():
      self.top+=1
      self.items[self.top]= operand

  def validate_postfix_expression(self, expression):
    c1=0
    c2=0
    for i in expression:
      if i.isdigit():
        c1+=1
      else:
          c2+=1
    if c1>c2 and expression[0].isdigit() and expression[1].isdigit():
      return 1
    else:
      return 0

  def evaluate_postfix_expression(self, expression):
    for i in expression:
      if i.isdigit():
        self.push(i)
      else:
        v1 = self.pop()
        v2 = self.pop()
    if i=='/':
      self.push(str(eval(v2 + i*2 + v1)))
    else:
      self.push(str(eval(v2 + i + v1)))
      return self.pop()

# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
