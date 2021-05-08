class SnapshotArray:
    '''
    time O(length + #of snaps) | space O(length + #of snaps)
    '''

    def __init__(self, length: int):
        self.dic = {}
        self._snap = 1

        #loop to set all the keys with list value 0
        for i in range(length):
            self.dic[i] = [0]

    def set(self, index: int, val: int) -> None:
        #get the original key and it's size
        items = self.dic[index]
        size = len(items)

        #pointer to original element to append
        org = items[-1]

        #in snap has been changed, we populate the value array with last the element
        if size < self._snap:
            for i in range(self._snap-len(items)):
                self.dic[index].append(org)

        #set the new val in the end
        items[self._snap-1] = val

    def snap(self) -> int:
        val = self._snap-1
        self._snap += 1
        return val

    def get(self, index: int, snap_id: int) -> int:
        items = self.dic[index]

        #if snap_id is bigger, return the last amount
        if len(items)-1 < snap_id:
            return items[-1]

        return items[snap_id]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
