# comment.py

class Comment:
    def __init__(self, comment_id, post, user, text):
        self.comment_id = comment_id
        self.post = post
        self.user = user
        self.text = text

    def display_info(self):
        print(f"Comment ID: {self.comment_id}")
        self.user.display_info()
        print(f"Post ID: {self.post.post_id}")
        print(f"Text: {self.text}")
