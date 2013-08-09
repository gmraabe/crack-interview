import sys

""" 
Write a program to read a multiple line text file and write the 'N' longest 
lines to stdout. Where the file to be read is specified on the command line.
The first line contains the value of the number 'N' followed by multiple lines.
"""

def insert_line(lines, newline):
    """Insert the newline in the list of lines, according to the length of
    the lines, from largest to smallest. Lines is already sorted by length"""
    hi = len(lines)
    lo = 0
    while lo < hi:
        mid = (lo+hi)//2
        if len(lines[mid]) > len(newline): lo = mid+1
        else: hi = mid
    lines.insert(lo, newline)
        
def add_line(lines, newline, n):
    """
    Assumes all previous lines are sorted. Checks if newline is longer than 
    shortest line, if it is, put it where it needs to be. If not, append to 
    the end, then check If length is longer than n, gets rid of shortest line.
    """
    if len(newline) > len(lines[-1]):
        insert_line(lines, newline)
    else:
        lines.append(newline)

    if len(lines) > n:
        del lines[-1]
    
test_cases = open(sys.argv[1], 'r')
lines = []
count = 0 # number of lines seen
for test in test_cases:
    ntest = test.strip()
    if not ntest == "":
        if count == 0:
            n = int(ntest)
            count += 1
        elif count == 1:
            lines.append(ntest)
            count += 1
        else:
            add_line(lines, ntest, n)
for i in lines:
    print i

test_cases.close()



