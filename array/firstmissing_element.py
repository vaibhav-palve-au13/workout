
def sol(arr):
    """
    given problem we find first missing positive element let think about problem
    we try to check how many no. are present in the array that is positive and negative 
    """
    n = len(arr)

    for i in range( n ):
        """
        we are try to range from 0 to len(array)
        """

        if arr[i] <= 0 or arr[i] >= n:
            arr[i] = 0
    """
    here we check bigger no, in array using boolean condition 
    an negative no. 
    and we are both no. to be make zero 
    """
    for i in range( n ):
        arr[ arr[i] % n] += n

    """
    in this array we try to convert no. zero no. into any other no.
    let do it
    arr[arr[i] % n] += n

    """

    print( arr )

    for i in range( n ):

        if arr[i] // n == 0:
            print( i )
    """
    here  we check len of array and no. become zero
    

    """

    print(arr[ i ])

if __name__ == "__main__":
    s = sol
    arr = [1,3]
    sol( arr )

