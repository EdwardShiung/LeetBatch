def two_sum(nums, target):
    """
    Finds two numbers in a list that add up to a given target.

    Args:
      nums: A list of integers.
      target: The target sum.

    Returns:
      A list containing the indices of the two numbers that add up to the target, 
      or None if no such pair exists.
    """

    seen = {}  # Store numbers and their indices

    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index

    return None  # No solution found


# Examples
nums1 = [2, 7, 11, 15]
target1 = 9
print(f"Indices for {nums1} and {target1}: {two_sum(nums1, target1)}")

nums2 = [3, 2, 4]
target2 = 6
print(f"Indices for {nums2} and {target2}: {two_sum(nums2, target2)}")

nums3 = [3, 3]
target3 = 6
print(f"Indices for {nums3} and {target3}: {two_sum(nums3, target3)}")