def isPossible(boards,k,barrier):
    painter=1
    boardsPainted=0
    for i in range(len(boards)):
        if boardsPainted+boards[i]<=barrier:
            boardsPainted+=boards[i]
        else:
            painter+=1
            if painter>k or boards[i]>barrier:
                return False
            else:
                boardsPainted=boards[i]
    return True            
    
    
    
def findLargestMinDistance(boards:list, k:int):
    # Write your code here
    # Return an integer
    start=0
    end=sum(boards)
    mid=start+(end-start)//2
    ans=-1
    while(start<=end):
        if isPossible(boards,k,mid):
            ans=mid
            end=mid-1
        else:
            start=mid+1
        mid=start+(end-start)//2
    return ans    