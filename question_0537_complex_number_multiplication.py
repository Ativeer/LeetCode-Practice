class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        n1 = num1.split("+")
        n2 = num2.split("+")
        
        n1_real = int(n1[0])
        n2_real = int(n2[0])
        
        n1_complex = int(n1[1][:-1])
        n2_complex = int(n2[1][:-1])
        
        final_real = n1_real*n2_real - (n1_complex*n2_complex)
        final_complex = n1_real*n2_complex + n2_real*n1_complex
        
        return str(final_real) + "+" + str(final_complex) +"i"
    