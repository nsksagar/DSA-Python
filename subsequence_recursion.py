def subSeq(nums, res, temp, ind, n):

    if ind >= n:
        res.append(temp[:])
        return 

    temp.append(nums[ind])
    subSeq(nums, res, temp, ind+1, n)
    temp.pop()
    subSeq(nums, res, temp, ind+1,n)



if __name__ == '__main__':
    nums = [1,2,3,4]
    res = []
    temp =  []
    n = len(nums) 
    ind = 0 
    print(f'result before performing the function : {res}')
    subSeq(nums, res, temp, ind, n)
    print(f'result after performing the function : {res}')
    