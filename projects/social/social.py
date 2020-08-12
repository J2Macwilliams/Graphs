import random

from util import Stack

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create friendships
        # generate all possible friendship combinations
        possible_friendships = []

        # avoid duplicates by ensuring first num < second num
        for user_id in self.users:
            # increment range to avoid duplicates
            for friend_id in range(user_id + 1, self.last_id + 1):
                # append friendship as tuple of user_id and friend_id
                possible_friendships.append((user_id, friend_id))

        # shuffle friendships
        random.shuffle(possible_friendships)

        # create friendships from the first N pairs of the list
        # N -> num_users * avg_friendships // 2
        N = num_users * avg_friendships // 2

        # loop the range of N to create friendships
        for i in range(N):
            friendship = possible_friendships[i]
            # abstract out user and friend from the stored tuple 
            user_id, friend_id = friendship
            self.add_friendship(user_id, friend_id)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # use a DFS -> for shortest path
        # key is the visited, value is the path to get to visited
        s = Stack()
        s.push([user_id])
        visited = {}  # Note that this is a dictionary, not a set
        # Create a loop to check stack size
        while s.size() > 0:
            # pop the first Path
            path = s.pop()
            # grab the last vertex from the Path
            key = path[-1]

            # check if the key is in visited
            if key not in visited:
                visited[key] = path

                # loop thru to get neighbors
                for friend in self.friendships[key]:
                    # make a copy of the path
                    path_copy = list(path)
                    # append the friend to the copy
                    path_copy.append(friend)
                    # push the copy onto the Stack
                    s.push(path_copy)

        return visited

def my_sum(*my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    # logic for answering questions
    # v = connections.values()
    # len_v = [len(x) for x in v]
    # print(len_v)
    # sum_avglen = my_sum(*len_v)
    # print( sum_avglen // 10)

    
    
