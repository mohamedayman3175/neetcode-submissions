class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        out = []

        for key in range(len(nums)):
            if nums[key] not in groups:
                groups[nums[key]] = []
    
            groups[nums[key]].append(key)
        
        sorted_groups = sorted(groups.items(), key=lambda item: len(item[1]), reverse=True)
            
        return [key for key , value in sorted_groups[:k]] 