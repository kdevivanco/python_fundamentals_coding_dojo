class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        addition = 0
        for number in nums:
            addition += number
        self.result += num + addition
        return self
    def subtract(self, num, *nums):
        addition = 0
        for number in nums:
            addition += number
        self.result -= num + addition
        return self
        
        
        
# crear una instancia:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)
