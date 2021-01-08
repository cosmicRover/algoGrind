class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        '''
        merge interval technique with two pointers on two arrays. overlap_max, start -> end
        
        need to find if there is an overlap between the two arrays with manual comparison
        first before using overlap_max to find the overlapped area. Since we are running two pointers
        between the two arrays in parallel, we only increment whichever element has lower end time
        
        time O(n) | space O(n)
        '''
        
        i = 0; j = 0
        ans = []
        
        while i < len(A) and j < len(B):
            #detect if there is an overlap i.e [2, 10] -> [2, 7]
            isAOverlap = A[i][0] >= B[j][0] and A[i][0] <= B[j][1]
            
            isBOverlap = B[j][0] >= A[i][0] and B[j][0] <= A[i][1]
            
            #if there is an overlap, apply overlap_max to get overlapped region
            if isAOverlap or isBOverlap:
                start = max(A[i][0], B[j][0])
                end = min(A[i][1], B[j][1])
                
                ans.append([start, end])
                
            #increment whichever has lower end time
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
                
        return ans