class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums ==[]:
            return 0
        
        nums.sort()
        hash_1={}
        hash_2={}
        count = 1
        best = 1
        for i in range(len(nums)) :
            hash_1[nums[i]] = hash_1.get(nums[i], 0) + 1

        keys = list(hash_1.keys())

        for i in range(len(keys) - 1):
            if keys[i] + 1 == keys[i + 1]:
                count += 1
            else:
                best = max(best, count)
                count = 1

        best = max(best, count)
        return best     