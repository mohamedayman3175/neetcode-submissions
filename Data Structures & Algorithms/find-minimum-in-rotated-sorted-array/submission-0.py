class Solution:
    def findMin(self, nums: List[int]) -> int:
        begin_index=0
        end_index=len(nums)-1
        while(end_index>begin_index):
            midpoint_index=begin_index + (end_index - begin_index)//2
            if nums[midpoint_index]>nums[end_index]:
                begin_index=midpoint_index+1
            else:
                end_index=midpoint_index
        return nums[begin_index]