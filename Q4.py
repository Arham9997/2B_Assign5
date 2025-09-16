class Solution:
    def infixtoPostfix(self, s):
        ans =""
        stack=[]
        dic={'^':3  , '*':2, '/':2, '+':1, '-':1}
        
        for i in  exp :
            if i.isalnum():
                ans += i  
            
            elif i =='(':
                stack.append(i)
            
            elif i == ')': 
                while stack and stack[-1] != '(':
                    ans+= stack.pop()
                stack.pop()
            else : 
                while stack and dic.get(stack[-1], 0) >= dic[i]:
                    ans += stack.pop()
                stack.append(i)
            
        while stack :
            ans += stack.pop()
            
        return ans
