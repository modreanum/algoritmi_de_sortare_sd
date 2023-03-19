def countingSort(v, p):
    l = len(v)
    r = [0] * l
    w = [0] * 10
    for i in range(0, l):
        w[(v[i] // p) % 10] += 1
    for i in range(1, 10):
        w[i] += w[i - 1]
    i = l - 1
    while i >= 0:
        r[w[(v[i] // p) % 10] - 1] = v[i]
        w[(v[i] // p) % 10] -= 1
        i -= 1
    for i in range(0, l):
        v[i] = r[i]

def radixSort(v):
    maxim = max(v)
    p = 1
    while maxim// p > 0:
        countingSort(v, p)
        p *= 10
#-----------------------------------------------------------------
def countingSortbin(v, p):
    l = len(v)
    r = [0] * l
    w = [0] * 10
    for i in range(0, l):
        w[(v[i] >> p) & 1] += 1
    for i in range(1, 10):
        w[i] += w[i - 1]
    i = l - 1
    while i >= 0:
        r[w[(v[i] >> p) &1] - 1] = v[i]
        w[(v[i] >> p) &1] -= 1
        i -= 1
    for i in range(0, l):
        v[i] = r[i]

def radixSortbin(v):
    maxim = max(v)
    p = 1
    while maxim>>p > 0:
        countingSortbin(v, p)
        p +=1
#--------------------------------------------------------
def interclasare(v, st, m, dr):
    i = st
    j = m+1
    aux = []
    while i <= m and j <= dr:
        if v[i] <= v[j]:
            aux.append(v[i])
            i += 1
        else:
            aux.append(v[j])
            j += 1
    aux.extend(v[i:m+1])
    aux.extend(v[j:dr+1])
    v[st:dr+1] = aux[:]

def mergeSort(v, st, dr):
    if st < dr:
        m = (dr+st) // 2
        mergeSort(v, st, m)
        mergeSort(v, m + 1, dr)
        interclasare(v, st, m, dr)
#-------------------------------------------------------------
def shellSort(v, n):
    dif = n // 2
    while dif > 0:
        j = dif
        while j < n:
            i = j - dif
            while i >= 0:
                if v[i + dif] > v[i]:
                    break
                else:
                    v[i + dif], v[i] = v[i], v[i + dif]
                i = i - dif
            j += 1
        dif = dif // 2


def partition(v, st, dr):
    pivot = v[dr]
    i = st - 1
    for j in range(st, dr):
        if v[j] <= pivot:
            i = i + 1
            (v[i], v[j]) = (v[j], v[i])
    (v[i + 1], v[dr]) = (v[dr], v[i + 1])
    return i + 1
#-------------------------------------------------------------------------------------
def f1(v, st, dr):
    pivot = v[dr]
    i = st - 1
    for j in range(st, dr):
        if v[j] <= pivot:
            i = i + 1
            (v[i], v[j]) = (v[j], v[i])
    (v[i + 1], v[dr]) = (v[dr], v[i + 1])
    return i + 1
def quickSort(v, st, dr):
    if st < dr:
        pi = f1(v, st, dr)
        quickSort(v, st, pi - 1)
        quickSort(v, pi + 1, dr)
#----------------------------------------------------------------------------------
def insertionSort(v):
    for i in range(1, len(v)):
        k = v[i]
        j = i - 1
        while j >= 0 and k < v[j]:
            v[j + 1] = v[j]
            j = j - 1
        v[j + 1] = k
#-------------------------------------------------------
def test(v):
    for i in range(0,len(v)-1):
        if(v[i]>v[i+1]):
            return False
    return True

import random
import time

f = open("test.txt", "r")

for linie in f:
    l=[int(x) for x in linie.split()]
    N=l[0]
    Max=l[1]
    randomlist = []
    for i in range(0, N):
        n = random.randint(1, Max)
        randomlist.append(n)
    r=randomlist.copy()

    print ("N=",N,"Max=",Max)


    timp_start =time.time()
    radixSort(randomlist)
    timp_end = time.time()
    print ("1 radix sort",timp_end-timp_start,test(randomlist))


    randomlist = r.copy()

    timp_start = time.time()
    mergeSort(randomlist, 0, N - 1)
    timp_end = time.time()
    print("2 radix binary sort", timp_end - timp_start,test(randomlist))


    randomlist=r.copy()

    timp_start = time.time()
    mergeSort(randomlist, 0, N - 1)
    timp_end = time.time()
    print("3 merge sort", timp_end - timp_start,test(randomlist))



    randomlist = r.copy()

    timp_start = time.time()
    shellSort(randomlist, N)
    timp_end = time.time()
    print("4 shell sort", timp_end - timp_start,test(randomlist))


    randomlist=r.copy()
    timp_start = time.time()
    quickSort(randomlist, 0, N - 1)
    timp_end = time.time()
    print("5 quick sort", timp_end - timp_start,test(randomlist))


    randomlist = r.copy()
    timp_start = time.time()
    insertionSort(randomlist)
    timp_end = time.time()
    print("6 insertion sort", timp_end - timp_start,test(randomlist))


    randomlist = r.copy()

    timp_start = time.time()
    randomlist.sort()
    timp_end = time.time()
    print("7 python sort", timp_end - timp_start,test(randomlist))
