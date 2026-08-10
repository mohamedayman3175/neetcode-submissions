class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # skip duplicate first elements
            if nums[i] > 0:
                break  # smallest is positive, no triplet possible
            target = -nums[i]
            left = i+1
            right= n - 1
            while left < right :
                summ = nums[left] + nums[right]
                if summ == target :
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif target > summ :
                    left+=1
                else:
                    right -=1
        return res