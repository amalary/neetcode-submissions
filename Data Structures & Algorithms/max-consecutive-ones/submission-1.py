class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        counter = 0 
        longeststreak = 0

        for num in nums: 

            if num == 1: 

                counter+= 1 

            elif num != 1: 

                if counter >  longeststreak: 

                    longeststreak = counter 

            
                counter = 0 
                
                longeststreak = max(longeststreak,counter)

        if counter > longeststreak:
            longeststreak = counter

        return longeststreak 