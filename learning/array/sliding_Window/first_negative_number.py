# Uses a deque to track candidate indices — foundation for the advanced deque-window problems later.

# arr => array of elements
# k is the size of the window
from collections import deque

def first_negative_in_window(arr, k):
    dq = deque()
    