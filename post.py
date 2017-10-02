class Post:

    def __init__(self, likes=0):
        self.likes = likes
        self.post = input("Whats on your mind: ")
        self.comments = []

    def delete(self):
        # TODO: find a way to destroy object
        pass

    def like(self):
        self.likes = self.likes + 1

    def unlike(self):
        self.likes = self.likes - 1 if self.likes >= 1 else 0

    def comment(self):
        c = input("Comment: ")
        self.comments.append(c)

# TEST: Uncomment the block of code below to test the class above and associated methods
my_post = Post()
while True:
    what_to_do = input('like/unlike/comment l/u/c: ')
    if what_to_do == 'l' or what_to_do == 'like':
        my_post.like()
    elif what_to_do == 'u' or what_to_do == 'unlike':
        my_post.unlike()
    elif what_to_do == 'c' or what_to_do == 'comment':
        my_post.comment()
    print(my_post.post, 'likes: {} * comments: {}'.format(my_post.likes, my_post.comments))
