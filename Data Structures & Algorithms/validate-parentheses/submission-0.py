class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = { ")" : "(", "]" : "[", "}" : "{" }
        if s and len(s) % 2 == 0:
            for i in s:
                if i in check:
                    if stack and stack[-1] == check[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(i)
            return len(stack) == 0
        return False