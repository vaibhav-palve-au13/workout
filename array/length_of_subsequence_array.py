def subsequenceofarray( A ):
    maxlen = 1
    currenrlen = 1
    endIdex = 0
    
    for i in range(1, len(A)):

        if A[i] * A[i - 1] < 0:
            currenrlen += 1
            if currenrlen > maxlen:
                maxlen = currenrlen
                endIdex = i
        else:
            currenrlen = 1
    sublist = A[endIdex - maxlen + 1 : endIdex +1 ]
    print( sublist )
    print( maxlen )

if __name__ == "__main__":
    array =[1-2,3,4,-3,5,-2,6,7]
    subsequenceofarray(array)