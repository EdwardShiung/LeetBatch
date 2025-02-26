class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for k, v in enumerate(nums):
            if (target - v) in m:
                return [m[target - v], k]
            m[v] = k
        return []