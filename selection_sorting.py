#User function Template for python3

class Solution: 
    def select(self, arr, i):
        man=len(arr)
        selectionSort(arr,man)
    def selectionSort(self, arr,n):
        for i in range(n):
            min_value=i
            for j in range(i+1,n):
                if arr[j]<arr[min_value]:
                    min_value=j
            (arr[i], arr[min_value]) = (arr[min_value], arr[i])


            
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
