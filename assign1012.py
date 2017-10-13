#!usr/bin/python3
#function to find max of a subarray
def find_maximum_subarray_bf(a):        #bf for brute force
    p1 = 0
    l = 0           # l for left
    r = 0           # r for right
    max_sum = 0
    for p1 in xrange(len(a)):
        sub_sum = 0
        for p2 in xrange(p1, len(a)):
            sub_sum += a[p2]
            if sub_sum > max_sum:
                max_sum  = sub_sum
                l = p1
                r = p2
    return l, r, max_sum

def find_maximum_subarray_dc(a):        #dc for divide and conquer

    # subfunction
    # given an arrary and three indices which can split the array into a[l:m]
    # and a[m+1:r], find out a subarray a[i:j] where l \leq i \less m \less j \leq r".
    # according to the definition above, the target subarray must
    # be combined by two subarray, a[i:m] and a[m+1:j]
    # Growing Rate: theta(n)

    def find_crossing_max(a, l, r, m):

        # left side
        # ls_r and ls_l indicate the right and left bound of the left subarray.
        # l_max_sum indicates the max sum of the left subarray
        # sub_sum indicates the sum of the current computing subarray      
        ls_l = m+1
        ls_r = m
        l_max_sum = None
        sub_sum = 0
        for j in xrange(m,l-1,-1):      # adding elements from right to left
            sub_sum += a[j]
            if sub_sum > l_max_sum:
                l_max_sum = sub_sum
                ls_l = j

        # right side
        # rs_r and rs_l indicate the right and left bound of the left subarray.
        # r_max_sum indicates the max sum of the left subarray
        # sub_sum indicates the sum of the current computing subarray                
        rs_l = m+1
        rs_r = m
        r_max_sum = 0
        sub_sum = 0
        for j in range(m+1,r+1):
            sub_sum += a[j]
            if sub_sum > r_max_sum:
                r_max_sum = sub_sum
                rs_r = j

        #combine
        return (ls_l, rs_r, l_max_sum+r_max_sum)

    # subfunction
    # Growing Rate:  theta(nlgn)
    def recursion(a,l,r):           # T(n)
        if r == l:
            return (l,r,a[l])
        else:
            m = (l+r)//2                    # theta(1)
            left = recursion(a,l,m)         # T(n/2)
            right = recursion(a,m+1,r)      # T(n/2)
            crossing = find_crossing_max(a,l,r,m)   # theta(r-l+1)

            if left[2]>=right[2] and left[2]>=crossing[2]:
                return left
            elif right[2]>=left[2] and right[2]>=crossing[2]:
                return right
            else:
                return crossing

    #back to master function
    l = 0
    r = len(a)-1
    return recursion(a,l,r)

if __name__ == "__main__":

    from time import time
    from sys import argv
    from random import randint
    alen = 100
    if len(argv) > 1:
        alen = int(argv[1])
    a = [randint(-100,100) for i in xrange(alen)]

    time0 = time()
    print find_maximum_subarray_bf(a)
    time1 = time()
    print find_maximum_subarray_dc(a)
    time2 = time()
    print "function 1:", time1-time0
    print "function 2:", time2-time1 
    print "ratio:", (time1-time0)/(time2-time1)
