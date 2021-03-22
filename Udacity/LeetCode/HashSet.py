class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numBuckets = 5
        self.buckets = [[] for i in range(self.numBuckets)]

    def hash_function(self, key):
        value = key % self.numBuckets
        print(value)
        return value

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = self.hash_function(key)
        if not key in self.buckets[i]:
            self.buckets[i].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = self.hash_function(key)
        if key in self.buckets[i]:
            self.buckets[i].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        i = self.hash_function(key)
        if key in self.buckets[i]:
            return True
        return False


hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
hashSet.contains(1)  #returns true
hashSet.contains(3) # returns false(not found)
hashSet.add(2)
hashSet.contains(2) # returns true
hashSet.remove(2)
hashSet.contains(2) # returns false(already removed)