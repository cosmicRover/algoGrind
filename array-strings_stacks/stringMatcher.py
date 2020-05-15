class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        #loop to go through each elements
        for x in ransomNote:

            #if the element exist in the other string, find the index of the element and
            #re organize the elments so it deletes the found element
            if x in magazine:
                index = magazine.index(x)
                magazine = magazine[:index] + magazine[index+1:]

                index = ransomNote.index(x)
                ransomNote = ransomNote[:index] + ransomNote[index+1:]

            else:
                return False

        print(magazine)
        print(ransomNote)

        return True if len(ransomNote) == 0 else False
