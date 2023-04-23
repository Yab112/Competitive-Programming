class Solution(object):
    
    def evalRPN(self, tokens: List[str]) -> int:
        opstack = Stack()
        for token in tokens:
            if token.lstrip('-+').isdigit():
                opstack.Push(int(token))
                print("here")
            else:
                operand1 = opstack.Pop()
                operand2 = opstack.Pop()
                print(type(operand1))
                result = self.doMath(token,operand2,operand1)
                opstack.Push(int(result))
        return opstack.Pop() 
    def doMath(self,op,op1,op2):
            if op == '/':
                return op1 / op2
            elif op == '*':
                return op1 * op2
            elif op == '-':
                return op1 - op2
            elif op == '+':
                return op1 + op2
class Stack:
    def __init__(self):
        self.items = []
    def Push(self,item):
        self.items.append(item)
    def Pop(self):
        return self.items.pop()
    def Isempty(self):
        return (self.items == [])
    def __str__(self):
        return str(self.items)
  