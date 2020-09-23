class Solution:
    def subdomainVisits(self, cpdomains: [str]) -> [str]:
        dic = {}

        for x in cpdomains:
            #seperate count from words
            words = x.split(" ")
            count = int(words[0])

            #join the s and record it
            s = ""
            s = s.join(words[1:])

            if s not in dic:  # need to make sure the key exists first
                dic[s] = 0
            dic[s] += count  # record the hit count

            #now we disect rest of the words by splitting them
            new = words[1].split(".")[1:]

            # need to go in reverse so that "." can be joined
            for i in reversed(range(len(new))):
                # since we need a ".", we join them with one
                s = ".".join(new[i:])

                #add to their count
                if s not in dic:
                    dic[s] = 0
                dic[s] += count

        #format the values and return them
        ans = []
        for k, v in dic.items():
            ans.append(str(v)+" "+k)

        return ans
