# social_media_system.py

from user import User
from post import Post
from comment import Comment

# Create users
user1 = User(1, "Alice", "alice@example.com")
user2 = User(2, "Bob", "bob@example.com")

# Create posts
post1 = Post(101, user1, "Hello, World!")
post2 = Post(102, user2, "Python is awesome!")

# Create comments
comment1 = Comment(1001, post1, user2, "Great post!")
comment2 = Comment(1002, post2, user1, "I agree!")

# Display information
print("Social Media Information:")
post1.display_info()
print()
comment1.display_info()
print()
post2.display_info()
print()
comment2.display_info()
