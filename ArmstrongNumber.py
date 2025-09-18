class Solution:    
    def printArmstrongNumbers(self,n):
        #Write your code here.
        for i in range(1,n+1):
            original_num=i
            sum_of_cubes=0

            while i>0:
                digit=i%10
                sum_of_cubes+=(digit*digit*digit)
                i//=10
                
            if sum_of_cubes==original_num:
                print(original_num)        
            

if __name__=='__main__':
    n = int(input())
    Obj = Solution()
    Obj.printArmstrongNumbers(n)