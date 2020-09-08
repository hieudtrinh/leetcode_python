class ThreeSumClosest:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)) :
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi) :
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1

            if diff == 0:
                break
        return target - diff

nums: List[int] = [-1,2,1,-4]
target = 1
solution = ThreeSumClosest()
print(solution.threeSumClosest(nums,target))
