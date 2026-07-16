class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            o = operations[i]
            if o == "+":
                a = stack[-1] + stack[-2]
                stack.append(a)
            elif o == "C":
                stack.pop()
            elif o == "D":
                stack.append(2 * stack[-1]) 
            else:
                stack.append(int(o))
        return sum(stack)
