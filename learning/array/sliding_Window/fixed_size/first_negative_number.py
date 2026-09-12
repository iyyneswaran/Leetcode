# Uses a deque to track candidate indices — foundation for the advanced deque-window problems later.

# arr => array of elements
# k is the size of the window
from collections import deque

def first_negative_in_window(arr, k):
    dq = deque()
    res = []

    for i, val in enumerate(arr):
        if val < 0:
            dq.append(i)

        if dq and dq[0] <= i - k:
            dq.popleft()

        if i >= k - 1:
            res.append(arr[dq[0]] if dq else 0)
    return res

# or 
from collections import deque

def first_negative_in_window(arr, k):
    dq = deque()   # stores indices of negative numbers in current window
    res = []
    for i, val in enumerate(arr):
        if val < 0:
            dq.append(i)
        if i >= k - 1:
            if dq and dq[0] <= i - k:
                dq.popleft()
            res.append(arr[dq[0]] if dq else 0)
            if dq and dq[0] == i - k + 1:
                dq.popleft()
    return res