## Made by: Joshwai Sharp
## My Social Network(RUSSIAN NETWORK)


class User:

    ##Constructor of class for Social Network Functions
    def __init__(self, username, userID):
        self.firstName = ""
        self.lastName = ""
        self.username = username
        self.bio = ""
        self.friends = []
        self.posts = []
        self.userID = userID

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

    ##Create a post function
    def createPost(self, content):
        myPost = Post(content)
        self.posts.append(myPost)
        myPost.createPostID(len(posts))

    ##Function to give a new user a unique ID Number
    def createUserID(self, num):
        self.userID = num

        
##This A Class for Post
class Post:
    def __init__(self, content):

        self.content = content
        self.postID = ""
        self.comments = []

    ##Function to give a new post a unique ID Number
    def createPostID(self, num):
        self.postID = num


##This A Class for Network
class Network:
    def __init__(self):
        self.users = []

    ##Function to make a new user
    def createUser(self, username):
        mySize = int(len(self.users)) + 1
        myUser = User(username)
        self.users.append(myUser)
        print(len(self.users))

    ##Function to make the things work
    def addConnection(self, user1, user2):
        user1OBJ = self.getOBJ(user1)
        user1OBJ = self.getOBJ(user2)

        user1OBJ.addFriend(user2OBJ)
        user2OBJ.addFriend(user1OBJ)

    ##Function to make your users into objects
    def getOBJ(self, username):
        userID = self.getUserID(username)
        userOBJ = self.users[userID - 1]
        print(userOBJ.username)
        return userOBJ

    ##Function to get the ID of an user
    def getUserID(self, username):
        for i in self.users:
            if i.username == username:
                return i.userID



##MAIN FUNCTION
if __name__ == "__main__":


    ##Creation of a network
    russia = Network()
    
    ##Users/Friends
    russia.createUser("Sharp")
    print("kakke")
    russia.createUser("Radndy")
    print("akke")
    russia.createUser("Jericho")
    print("kake")

    print(len(russia.users))

##    ##Sharp stuff
    sharp = russia.getOBJ("Sharp")
    sharp.addFirstName("FredFred")
    sharp.addBio("BlASTFOME")
    sharp.addLastName("Burger")

##    ##Radndy stuff
    radndy = russia.getOBJ("Radndy")
    radndy.addFirstName("Randndy")
    radndy.addBio("I know KARATE!")
    radndy.addLastName("Bonson")

    ##Add Radndy to Friend List
    sharp.addFriend(radndy)

##    ##Radndy's Post
##    radndy.createPost("this is first pot")

    ##Jericho stuff
    jericho = russia.getOBJ("Jericho")
    jericho.addFirstName("Jericho")
    jericho.addBio("Do you want a piece of candy?")
    jericho.addLastName("Wanton")
    
    ##Add Jericho to Friends List
    sharp.addFriend(jericho)

    ##Jericho's Post
##    jericho.createPost("Tell me story ;)")


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


