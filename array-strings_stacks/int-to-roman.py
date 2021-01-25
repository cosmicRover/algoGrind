class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        this is a boring problem but a good use case for divmod()
        once gotten the quotient from remainder, append to ans as symbol * quotient
        
        time O(1) | space O(1) since the amount is very limited
        '''
        
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), 
          (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        
        translated_digits = []
        
        for val, sym in digits:
            quotient, remainder = divmod(num, val)
            num = remainder
            
            translated_digits.append(sym * quotient)
            
        return "".join(translated_digits)