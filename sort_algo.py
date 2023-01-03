lis = [22, 11, 88, 66, 55, 77, 33, 44]


def bubble_sort(lis):
    for i in range(5):
        print(lis)
        for j in range(0, 5-i-1):

            print(j, j + 1)
            print(lis[j], lis[j + 1])
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                print(lis[j], lis[j + 1])
                print('end')
    print(lis)


def partition(lis, left, right):
    i = left
    j = right - 1
    pivot = lis[right]
    print(i, j, pivot)
    while i < j:

        # i is looking for item greater than pivot, if found, break loop
        # i += 1 moves pointer to right, will loop until i greater than right and lis[i] > pivot
        while i < right and lis[i] < pivot:
            print(i ,lis[i])
            print('check I')
            i += 1
        while j > left and lis[j] >= pivot:
            print(j, lis[j])
            print('check J')
            j -= 1
        if i < j:
            print('yes')
            print(i, j)
            print('yes')
            lis[i], lis[j] = lis[j], lis[i]
    if lis[i] > pivot:
        lis[i], lis[right] = lis[right], lis[i]
    print(lis, i)
    return i, lis
partition(lis, 0, len(lis)-1)

# left(i) of pivot look for item larger than pivot
# right(j) of pivot look for item smaller than pivot
# if j <= i return
def quick_sort(lis, left, right):
    # subarray contains two elements, if i element[4] then lis has been sorted
    if left < right:
        # partition_position where item splits arrays
        partition_position = partition(lis, left, right)
        # [22, 11, 33, 44, 55, 77, 88, 66]
        # left = 0, partition_position - 1 is 3-1, subarray = [22, 11, 33]
        quick_sort(lis, left, partition_position[0] - 1)
        # left = 3 + 1, right = 7, subarray = [55, 77, 88, 66]
        quick_sort(lis, partition_position[0] + 1, right)
        return partition_position[1]

def merge_sort(lis):
    #if length of array is not greater than one, array has already been sorted
    if len(lis) > 1:
        # left side of list, right side of list
        left_lis = lis[:len(lis)//2]
        right_lis = lis[len(lis)//2:]
        # recursive
        merge_sort(left_lis)
        merge_sort(right_lis)
        # merge
        i = 0 # i will keep track of left side of left array, left list index
        j = 0 # j will keep track of left side of left array, right list index
        k = 0 # merged list index
        while i < len(left_lis) and j < len(right_lis):
            #print(left_lis, right_lis)
            if left_lis[i] < right_lis[j]:

                print(left_lis, right_lis)
                print(left_lis[i], right_lis[j])
                print(k, lis[k])
                print('first')
                lis[k] = left_lis[i]
                i += 1
            else:
                print(left_lis[i], right_lis[j])
                print(k, lis[k])
                print('right')
                lis[k] = right_lis[j]
                j += 1
            k += 1
        while i < len(left_lis):
            lis[k] = left_lis[i]
            i += 1
            k += 1
        while j < len(right_lis):
            lis[k] = right_lis[j]
            j += 1
            k += 1
    #print(lis)

lis = [2, 5, 6, 1, 3, 4]
def insertion_sort(lis):
    for i in range(1, len(lis)):
        j = i
        print(j, lis[j - 1], lis[j])
        print('top')
        # if left is less than right, list stays the same
        while lis[j - 1] > lis[j] and j > 0:
            lis[j - 1], lis[j] = lis[j], lis[j-1]
            print(j, lis)
            print('bottom')
            j -= 1
    print(lis)





