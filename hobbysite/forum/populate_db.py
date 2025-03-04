from forum.models import Post, PostCategory

post_categories = [
    {
        "title": " ",
        "entry": " ",
    },
]

posts = [
    {
        "title": " ",
        "entry": " ",
        "created_on": " ",
        "updated_on": " ",
        "post_category":" "
    },
]

for post_category in post_categories:
    pc = PostCategory()
    pc.title = post_category["title"]
    pc.entry = post_category["entry"]
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