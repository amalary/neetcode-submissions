class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: 

        # I am going to create a counter for the consecutive 1's in the array 
        #Going to create a variable to keep track of the longeststreak of consecutive 1's 
        #If the number in the array is equal to 1 the counter will increament if it is not itll be skipped over 
        # Finally I'll return the value for the longeststreak for 1's 

        counter = 0 

        longeststreak = 0 

        for num in nums: 

            if num == 1: 

                counter+=1 

                longeststreak = max(longeststreak,counter)
            
            else: 

                counter = 0 

        return longeststreak 
        
        