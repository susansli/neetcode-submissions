class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # instatiate a dictionary to store keys: indices
        nums_dict = dict()
        for i, num in enumerate(nums):
            # do a lookup
            if (target - num) in nums_dict:
                return[nums_dict[target - num], i]
            # if not there, then add the num + indice
            else:
                nums_dict[num] = i
        return [None, None] # should never happen