'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    result = []
    tempList = []

    for i in range( len(nums)- k + 1 ):
        max = nums[i]
        
        # tempList will containt k number of elements
        # for example if k = 3, templist will containt 3 elements
        tempList.extend(nums[i:k+i])

        # then we choose the largest element from tempList
        for number in tempList:
            if number > max:
                max = number

        # add max value to result
        result.append(max)
        # clear temp list that containt k number of elements
        tempList = []
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
