## Made by: Joshwai Sharp
## My Social Network


class User:

    ##Constructor of class for Social Network Functions
    def __init__(self, firstName, lastName, username, bio, userID):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.bio = bio
        self.userID = userID
        self.friends = []
        self.posts = []

    ##Person has been added to your friendlist function
    def addFriend(self, username):
        self.friends.append(username)

    ##Person has been removed from your friendlist function
##    def unFriend():
##
    ##See all your friend's posts function
    def viewNewsFeed(self, friends):
        for friendPost in self.friends:
            print(friends.posts)

if __name__ == "__main__":

    ##Sharp account customizations
    firstName = "FredFred"
    lastName = "Burger"
    username = "ReaperMain1998"
    bio = "BlASTFOME"
    userID = "4279"

    ##Users/Friends
    sharp = User(firstName, lastName, username, bio, userID)
    radndy = User("Randndy", "Bonson", "FootMassages73", "I know KARATE!", "429")
    jericho = User("Jericho","Wanton","ChillyWillyHilly","Do you want a piece of candy?","720")

    ##Sharp stuff
    print(sharp.firstName)

    ##Radndy stuff
    print(radndy.firstName)
    sharp.addFriend(radndy)
    ##Radndy's Post
    radndy.posts.append("this is first post")
##    radndyPost = radndy.posts
##    print(radndyPost)


    ##Jericho stuff
    print(jericho.firstName)
    sharp.addFriend(jericho)
    ##Jericho's Post
    jericho.posts.append("Tell me story ;)")
##    jerichoPost = jericho.posts
##    print(jerichoPost)

##The Attempt to Show News Feed Thing
sharp.viewNewsFeed(username)
