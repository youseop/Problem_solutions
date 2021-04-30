#import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        dictionary = dict()
        for n in nums:
            if n not in dictionary:
                dictionary[n] = 1
            else:
                dictionary[n] += 1
        return sorted(dictionary, key=lambda x: -dictionary[x])[:k]
        #return heapq.nlargest(k, dictionary, key=dictionary.get)


        