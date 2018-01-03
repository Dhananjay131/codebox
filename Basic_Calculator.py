class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0;
        number = 0;
        sign = 1;
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                number = 10 * number + int(c)
            elif(c == '+'):
                result += sign * number
                number = 0
                sign = 1
            elif(c == '-'):
                result += sign * number
                number = 0
                sign = -1
            elif(c == '('):
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif(c == ')'):
                result += sign * number 
                number = 0
                result *= stack.pop()    
                result += stack.pop()   
            
     
        if(number != 0): result += sign * number
        return result