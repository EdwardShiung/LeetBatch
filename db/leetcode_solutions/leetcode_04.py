def find_median_sorted_arrays(nums1, nums2):
    """
    Finds the median of two sorted arrays.

    Args:
      nums1: The first sorted array.
      nums2: The second sorted array.

    Returns:
      The median of the two sorted arrays.
    """

    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m  # Ensure nums1 is shorter

    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and nums2[j - 1] > nums1[i]:
            # i is too small, increase it
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            # i is too big, decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_left = nums2[j - 1]
            elif j == 0: max_left = nums1[i - 1]
            else: max_left = max(nums1[i - 1], nums2[j - 1])

            if (m + n) % 2 == 1:
                return max_left

            if i == m: min_right = nums2[j]
            elif j == n: min_right = nums1[i]
            else: min_right = min(nums1[i], nums2[j])

            return (max_left + min_right) / 2.0

# Example usage:
nums1 = [1, 3]
nums2 = [2]
median = find_median_sorted_arrays(nums1, nums2)
print(f"The median of the arrays is: {median}") 

nums1 = [1, 2]
nums2 = [3, 4]   
median = find_median_sorted_arrays(nums1, nums2)
print(f"The median of the arrays is: {median}")