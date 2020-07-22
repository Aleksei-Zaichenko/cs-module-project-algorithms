'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    numberOfAppearances = {}
    singleNumber = 0

    for item in range (len(arr)):
        number = arr[item]
        if number in numberOfAppearances:
            numberOfAppearances[number] = 2
        else:
            numberOfAppearances[number] = 1


    for x in numberOfAppearances:
        if numberOfAppearances[x] == 1:
            singleNumber = x
            
    return singleNumber


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
