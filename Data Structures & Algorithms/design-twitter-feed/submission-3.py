class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.tweetCount = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:        
        self.tweetMap[userId].append([self.tweetCount, tweetId])
        self.tweetCount -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for fol in self.followMap[userId]:
            if fol in self.tweetMap:
                index = len(self.tweetMap[fol]) - 1
                count, tweetId = self.tweetMap[fol][index]
                heapq.heappush(minHeap, [count, tweetId, fol, index - 1])

        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, fol, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[fol][index]
                heapq.heappush(minHeap, [count, tweetId, fol, index - 1])
        return res


        #return None

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
