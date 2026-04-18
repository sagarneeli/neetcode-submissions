class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operators:
                element1 = int(stack.pop())
                element2 = int(stack.pop())
                result = 0
                if token == "+":
                    result = element1 + element2
                elif token == "-":
                    result = element2 - element1
                elif token == "*":
                    result = element1 * element2
                elif token == "/":
                    result = int(float(element2) / element1)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()
        