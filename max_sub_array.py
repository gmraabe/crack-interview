def max_subarray(A):
    """ just playing around with some code trying to understand it.
    """
    # This works because we are starting with our max sum being zero, 
    # otherwise we would have to slide our starting position as well, but
    # in this case if what we have so far is less than zero, there is no
    # way that including it will make our max bigger. However, if the 
    # numbers were all negative, this would return zero, even though this 
    # may not really be the max.
    max_ending_here = max_so_far = 0
    for x in A:
        print('x',x)
        max_ending_here = max(0, max_ending_here + x)
        print('max',max_ending_here)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
