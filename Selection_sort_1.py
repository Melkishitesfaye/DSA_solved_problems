#User function Template for python3

class Solution: 
    def select(self, arr, i):
        mini = arr[i]
        ind = i
        while i < len(arr):
            if mini > arr[i]:
                mini = arr[i]
                ind = i
            i+=1
        return ind
        
        # code here 
    
    def selectionSort(self, arr,n):
        for i in range(n):
            ind = self.select(arr,i)
            arr[i] , arr[ind] = arr[ind] , arr[i]
        #code here
        return 0  
