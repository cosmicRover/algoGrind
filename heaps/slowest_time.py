import heapq


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        '''
        time O(n) | space O(n) for the heap
        '''
        h = []

        for i in range(len(releaseTimes)):
            key = keysPressed[i]
            time = releaseTimes[i]

            if i == 0:
                heapq.heappush(h, (-time, key))
            else:
                time -= releaseTimes[i-1]
                #in-case time is negative
                if time < 0:
                    heapq.heappush(h, (0, key))
                heapq.heappush(h, (-time, key))

        ans = [0] * 26 #won't require sorting the alphabets
        while h:
            time, key = heapq.heappop(h)
            time = -time

            index = ord(key)-ord('z')+25
            ans[index] += 1

            if not h:
                break

            newtime = -h[0][0]

            if time != newtime:
                break

        #find the lexicographically biggest letter
        for i in range(len(ans)-1, -1, -1):
            if ans[i] > 0:
                return chr(i+ord('z')-25)

        return -1
