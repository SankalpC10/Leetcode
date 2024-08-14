class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_list = []
        zero_index = -1
        zero_flag = False
        for i in range(len(nums)):
            if nums[i]!= 0:
                product *= nums[i]
                product_list.append(product)
            elif zero_flag is False and nums[i]==0:
                zero_index = i
                zero_flag = True
                product_list.append(product)
            else:
                return [j*0 for j in nums]
        for i in range(len(product_list)):
            if zero_flag and i != zero_index:
                product_list[i] = 0
            elif zero_flag and i== zero_index:
                product_list[i] = product_list[-1]
            else:
                product_list[i] = int(product_list[-1]/nums[i])
        return product_list
        
                




            
                