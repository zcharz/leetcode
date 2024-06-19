class NumArray:
    def __init__(self, nums: list[int]):
        numbers = nums
        running_sum = ['']*len(numbers)
        for i in range(len(numbers)):
            if i == 0:
                running_sum[i] = numbers[i]
            else:
                running_sum[i] = running_sum[i-1] + numbers[i]
        
        self.running_sum = running_sum

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.running_sum[right]
        return self.running_sum[right] - self.running_sum[left-1]

        


if __name__ == '__main__':
    x = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)