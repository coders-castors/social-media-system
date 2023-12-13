# post.py

class Post:
    def __init__(self, post_id, user, content):
        self.post_id = post_id
        self.user = user
        self.content = content

    def display_info(self):
        print(f"Post ID: {self.post_id}")
        self.user.display_info()
        print(f"Content: {self.content}")
