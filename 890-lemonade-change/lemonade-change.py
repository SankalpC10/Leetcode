class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_5 = 0
        bill_10 =0
        if bills[0]>5:
           return False
        for i in bills:
            if i ==5:
                bill_5 += 1
            elif i == 10:
                if bill_5<1:
                    return False
                else:
                    bill_10 +=1
                    bill_5 -=1
            else:
                if bill_10>=1 and bill_5>=1:
                    bill_10 -= 1
                    bill_5 -= 1
                elif bill_5 >=3:
                    bill_5 -=3
                else:
                    return False
        return True
                
                

            
                
            
