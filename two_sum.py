class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_lst = []
        for i in range(0,len(nums)-1):
	        for j in range(i+1,len(nums)):
		        if nums[i] + nums[j] == target:
			        new_lst.append(i)
			        new_lst.append(j)
			        break
		        else:
			        continue
        return new_lst
