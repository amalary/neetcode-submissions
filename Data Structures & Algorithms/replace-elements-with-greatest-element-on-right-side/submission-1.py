class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # initially I'd start out with creating a variable for the greatest element on the right naned rightMax and set it = -1 
        #Next I'd create a for loop that would loop in reverse starting from the end of the array reason being I would only have to 
        #loop through the array once comparaing values and replacing them with each number that surpases the right max. 
        #When I find a number that surpases the right max I'd store it in a variable the is the newMax and update my array in the current position its in with the rightMax: newMax = rightMax 
        #then I would return the array 

        rightMax = -1 

        for i in range(len(arr) - 1, -1, -1): 

            newMax = max(rightMax, arr[i])

            arr[i] = rightMax 

            rightMax = newMax 

        return arr 
