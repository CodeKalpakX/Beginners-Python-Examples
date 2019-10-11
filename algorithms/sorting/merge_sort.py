# this is the recursive mergesort algorithm
# just call "mergesort(xs)" with xs being a list

def mergesort(xs):
    if len(xs) < 2:
        return xs
    else:
        m = len(xs) // 2
        return merge(mergesort(xs[:m]), mergesort(xs[m:]))

def merge(low, high):
    res = []
    i, j = 0, 0
    while i < len(low) and j < len(high):
        if low[i] <= high[j]:
            res.append(low[i])
            i = i+1
        else:
            res.append(high[j])
            j = j+1
    res = res + low[i:]
    res = res + high[j:]
    return res