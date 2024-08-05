from collections import defaultdict


class Twitter:

    def __init__(self):
        self.tweets = []
        self.followlist = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        ret = []
        c = len(self.tweets)-1

        while len(ret)<10 and c>=0:
            if self.tweets[c][0] == userId or self.tweets[c][0] in self.followlist[userId]:
                ret.append(self.tweets[c][1])
            c-=1
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        # follower: followee list
        # follower follows the following followees
        self.followlist[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followlist[followerId]: 
            self.followlist[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

sol = Twitter()

# sol.postTweet(1,5)
# print(sol.getNewsFeed(1))

# print(sol.tweets)

# sol.follow(1,2)
# sol.postTweet(2,6)
# print(sol.getNewsFeed(1))

# sol.unfollow(1,2)
# print(sol.getNewsFeed(1))



sol.postTweet(1,4)
sol.postTweet(2,5)
sol.unfollow(1,2)
print(sol.getNewsFeed(1))