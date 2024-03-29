class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_num1 = 0
        for i in range(len(num1)):
            int_num1 += (ord(num1[len(num1) - 1 - i]) - 48) * (10 ** i)
        int_num2 = 0
        for i in range(len(num2)):
            int_num2 += (ord(num2[len(num2) - 1 - i]) - 48) * (10 ** i)
        
        return str(int_num1 * int_num2)
