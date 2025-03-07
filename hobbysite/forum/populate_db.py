from forum.models import Post, PostCategory

post_categories = [
    {
        "desc": "Best Drawing Tablets for Beginners",
        "name": "Digital Art",
    },
    {
        "desc": "What's Your Favorite Game of 2025 So Far?",
        "name": "Gaming",
    },
    {
        "desc": "Books You've Read and Recommend to Others",
        "name": "Literature",
    },
    {
        "desc": "Underrated Artists Worth Listening",
        "name": "Music",
    }
]

posts = [
    {
        "title": "Best Drawing Tablets for Beginners",
        "entry": "I'm looking to buy my first drawing tablet, but I'm overwhelmed by the choices! What's a good tablet for a beginner? Any recommendations?",
        "created_on": "2025-03-05 14:56:23",
        "updated_on": "2025-03-05 15:32:46",
        "post_category": "Digital Art"
    },
    {
        "title": "What's Your Favorite Game of 2025 So Far?",
        "entry": "We’re already a few months into 2025, and there have been some amazing game releases! What’s your top pick so far and why?",
        "created_on": "2025-03-04 18:23:45",
        "updated_on": "2025-03-04 18:24:56",
        "post_category": "Gaming"
    },
    {
        "title": "Books You've Read and Recommend to Others",
        "entry": "Share your favorite books, and tell us why they stood out to you. Would you recommend it to others?",
        "created_on": "2025-03-04 09:24:58",
        "updated_on": "2025-03-05 09:09:08",
        "post_category": "Literature"
    },
    {
        "title": "Underrated Artists Worth Listening",
        "entry": "Who are some underrated musicians or bands that deserve more recognition? Drop your recommendations and favorite tracks!",
        "created_on": "2025-03-01 12:20:36",
        "updated_on": "2025-03-01 12:25:04",
        "post_category": "Music"
    }
]

for post_category in post_categories:
    pc = PostCategory()
    pc.name = post_category["name"]
    pc.desc = post_category["desc"]
    pc.save()
    print(f"Successfully added {pc}")

for post in posts:
    po = Post()
    po.title = post["title"]
    po.title = post["entry"]
    po.created_on = post["created_on"]
    po.updated_on = post["updated_on"]
    po.post_category = PostCategory.objects.get(name=post["post_category"])
    po.save()
    print(f"Successfully added {po}")

print("Successfully populated database.")
print(PostCategory.objects.all())
print(Post.objects.all())

# exec(open("forum/populate_db.py").read())
