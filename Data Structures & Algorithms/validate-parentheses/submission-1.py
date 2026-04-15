class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        n=len(s)
        for i in s:
            if i=='(' or i=='{' or i=='[' :
                stack.append(i)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if i == ')' and top != '(':
                    return False
                if i == '}' and top != '{':
                    return False
                if i == ']' and top != '[':
                    return False

        if stack:
            return False
                  
        else:
            return True
        
                
                

        