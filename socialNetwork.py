## Made by: Joshwai Sharp
## My Social Network(RUSSIAN NETWORK)


class User:

    ##Constructor of class for Social Network Functions
    def __init__(self, username):
        self.firstName = ""
        self.lastName = ""
        self.username = username
        self.bio = ""
        self.friends = []
        self.posts = []

    ##function to add in a first name
    def addFirstName(self, firstName):
        self.firstName = firstName

    ##function to add in a last name
    def addLastName(self, lastName):
        self.lastName = lastName

    ##function to add in a bio
    def addBio(self, bio):
        self.bio = bio
    
    ##Person has been added to your friendlist function
    def addFriend(self, obj):
        self.friends.append(obj)

    ##Person has been removed from your friendlist function
    def unFriend(self, obj):
        for theDeletees in self.friends:
            if theDeletees.username == obj.username:
                self.friends.remove(obj)

    ##function to add in a post
    def addPost(self, posts):
        self.posts = posts
        
    ##See all your friend's posts function
    def viewNewsFeed(self):
        for friendPost in self.friends:
            print(friendPost.posts)

    ##See your Friend List
    def viewFriends(self):
        for friendParty in self.friends:
            print(friendParty.username)

##MAIN FUNCTION
if __name__ == "__main__":

    ##Users/Friends
    sharp = User("ReaperMain1998")
    radndy = User("FootMassages73")
    jericho = User("ChillyWillyHilly")

    ##Sharp stuff
    sharp.addFirstName("FredFred")
    sharp.addBio("BlASTFOME")
    sharp.addLastName("Burger")

    ##Radndy stuff
    radndy.addFirstName("Randndy")
    radndy.addBio("I know KARATE!")
    radndy.addLastName("Bonson")

    ##Add Radndy to Friend List
    sharp.addFriend(radndy)

    ##Radndy's Post
    radndy.addPost("this is first pot")

    ##Jericho stuff
    jericho.addFirstName("Jericho")
    jericho.addBio("Do you want a piece of candy?")
    jericho.addLastName("Wanton")
    
    ##Add Jericho to Friends List
    sharp.addFriend(jericho)

    ##Jericho's Post
    jericho.addPost("Tell me story ;)")


##RUSSIAN NETWORK FUNCTIONS

##The Attempt to Show Friend List Thing
print("This is your Friend List: ")
sharp.viewFriends()

##The Attempt to Show News Feed Thing
print("This is your News Feed: ")
sharp.viewNewsFeed()

##The Attempt to delete a friend Thing
sharp.unFriend(jericho)

##The supposively updated Friend List
print("This is your *UPDATED* Friend List: ")
sharp.viewFriends()

