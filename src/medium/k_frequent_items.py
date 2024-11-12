import collections
import random

class SolutionKFrequent:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for i, count in counts.items():
            buckets[count].append(i)
        result = []
        for i in reversed(range(len(buckets))):
            for j in range(len(buckets[i])):
                result.append(buckets[i][j])
                if len(result) == k:
                    return result
        return result
    
    def topKFrequentSol2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        p = []
        for key, val in counts.items():
            p.append((-val, key))
        self.kthElement(p, k-1)
        result = []
        for i in range(k):
            result.append(p[i][1])
        return result
    
    def kthElement(self, nums, k):
        def PartitionAroundPivot(left, right, pivot_idx, nums):
            pivot_value = nums[pivot_idx]
            new_pivot_idx = left
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                    new_pivot_idx += 1
            nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
            return new_pivot_idx
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)
            new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums)
            if new_pivot_idx == k:
                return
            elif new_pivot_idx > k:
                right = new_pivot_idx - 1
            else: # new_pivot_idx < k.
                left = new_pivot_idx + 1
    
if __name__ == "__main__":
    data = SolutionKFrequent().topKFrequent([4,4,1,1,1,2,2,3], 2)
    print(data)
    data = SolutionKFrequent().topKFrequentSol2([4,4,1,1,1,2,2,3], 2)
    print(data)