class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        nums=heights.copy()
        nums.sort()
        i=0
        c=0
        for i in range(len(nums)):
            if heights[i]!=nums[i]:
                c+=1
        return c
                
        """
        target = sorted(heights)
        i = 0
        for j in range(len(heights)):
            if target[j] != heights[j]:
                i += 1

        return i
        """