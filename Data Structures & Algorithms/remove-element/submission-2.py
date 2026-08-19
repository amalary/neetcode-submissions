class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 

        # k is a pointer goi to be positioned at the 0 index and increamented everytime two numbers are compared to the val. 
        # i is going to be the variable that'll keep track of the first pointer in the loop
        # I am going to write a for loop seeing if a number in a givien index is equal to the val if not ill replace the value in the k index 
        #in the end I'll return the value k. 

        k = 0 

        for i in range(len(nums)): 

            if nums[i] != val: 

                nums[k] = nums[i]

                k+=1 
                
        return k