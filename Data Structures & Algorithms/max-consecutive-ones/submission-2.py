class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        counter = 0 
        longeststreak = 0

        for num in nums: 

            if num == 1: 

                counter+= 1 

                longeststreak = max(longeststreak, counter)

            else: 
        
                counter = 0 
                
        return longeststreak 