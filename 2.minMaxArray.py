#https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1/#
#User function Template for python3

def getMinMax( a, n):
    ar=list(a)
    mn=min(ar)
    mx=max(ar)
    return mn,mx
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends