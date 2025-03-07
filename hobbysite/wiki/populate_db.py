from datetime import datetime
from django.utils.timezone import make_aware
from wiki.models import Article, ArticleCategory

article_categories = [
    {
        "name": "Mechanics",
        "desc": "Advanced movement techniques used to effectively maneuver around a map"
    },
    {
        "name": "Categories",
        "desc": "Different limitations or requirements for a player to accomplish a speedrun"
    },
    {
        "name": "Exploits",
        "desc": "Non-intended developer strategies for faster completion times in various categories"
    }
]

articles = [
    {
        "title": "Wavedash",
        "category_type": "Mechanics",
        "created_on": datetime.now(),
        "updated_on": datetime.now(),
        "entry": "A wavedash is a commonly used tech that allows the player to perform a small but long jump and also regain a dash. It's introduced in Farewell, right after passing the heart gate, and is frequently required to pass a lot of rooms later in the chapter."
    },  
    {
        "title": "Neutral",
        "category_type": "Mechanics",
        "created_on": datetime.now(),
        "updated_on": datetime.now(),
        "entry": "Neutral Jumps, often shortened to Neutrals, are an untaught tech that can be used to climb even and uneven walls without using any stamina. They are technically not required in the base game, however they're highly recommended to learn for collecting the winged golden strawberry in Forsaken City."
    },  
    {
        "title": "Wallbounce",
        "category_type": "Mechanics",
        "created_on": datetime.now(),
        "updated_on": datetime.now(),
        "entry": "A wallbounce, sometimes abbreviated to wounce or known as Super Walljumps in the game files, is a tech introduced in The Summit B-Side, and used through Farewell and the C-Sides (3C through 7C). It is a special type of walljump that's done by dashing upwards next to a wall and jumping while Madeline still has the dash momentum. It allows the player to reach greater heights and jump over tall obstacles."
    },  
    {
        "title": "Any%",
        "category_type": "Categories",
        "created_on": datetime.now(),
        "updated_on": datetime.now(),
        "entry": "Any% is the most basic and fundamental category, wherein a run is timed using the in game speedrun category and a player is challenged to get from the beginning, the Prologue, to the end of the game, Chapter 7, without the use of game-breaking glitches or exploits."
    },  
    {
        "title": "True Ending",
        "category_type": "Categories",
        "created_on": datetime.now(),
        "updated_on": datetime.now(),
        "entry": "True ending requires the player to complete the Prologue up until Farewell, Chapter 9, which entails having to complete the base game, chapter 8, and collect an additional 8 secret Crystal Hearts in order to unlock and then accomplish Celeste's Final Frontier."
    },  
    {
        "title": "All Red Berries",
        "category_type": "Categories",
        "created_on": datetime.now(),
        "updated_on": datetime.now(),
        "entry": "All Red Berries is the category in which the runner is required to collect all 175 red collectible berries before completing the base game, Chapter 7."
    },  
    {
        "title": "Bubsdrop",
        "category_type": "Exploits",
        "created_on": datetime.now(),
        "updated_on": datetime.now(),
        "entry": "Bubsdrop is a well-known trick in Mirror Temple B-Side, allowing players to skip getting the first key by performing a precise jump. The trick is performed by going through the vertical screen transition in the long horizontal room in Central Chamber, then by performing a tiny jump (1 or 2 frames) you can fall back through. Then, by dying either by retrying or by falling, you will be respawned on the right side of the room, skipping the first key!"
    },  
    {
        "title": "Oil Skip",
        "category_type": "Exploits",
        "created_on": datetime.now(),
        "updated_on": datetime.now(),
        "entry": "Oil Skip is niche but RTA viable strategy in which the player can access two dashes at the beginning of Farewell. This is performed by starting the cutscene at the Prologue of Chapter 9 for 1 frame, then both letting go of the cutscene trigger button and jumping for at least 2 frames. This would allow the player to 'float' and bypass the cutscene triggers that would remove the player's second dash when finishing the dialogue."
    },  
    {
        "title": "Bubsdrop",
        "category_type": "Exploits",
        "created_on": datetime.now(),
        "updated_on": datetime.now(),
        "entry": "Bubsdrop is a well-known trick in Mirror Temple B-Side, allowing players to skip getting the first key by performing a precise jump. The trick is performed by going through the vertical screen transition in the long horizontal room in Central Chamber, then by performing a tiny jump (1 or 2 frames) you can fall back through. Then, by dying either by retrying or by falling, you will be respawned on the right side of the room, skipping the first key!"
    },  
    
]

for article_category in article_categories: 
    ac = ArticleCategory()
    ac.name = article_category["name"]
    ac.desc = article_category["desc"]
    ac.save()
    print(f"Successfully added {ac}")

for article in articles:
    a = Article()
    a.title = article["title"]
    a.entry = article["entry"]
    a.created_on = make_aware(article["created_on"])
    a.updated_on = make_aware(article["updated_on"])
    a.category_type = ArticleCategory.objects.filter(name=article["category_type"]).first()
    a.save()
    print(f"Successfully added {a}")

print("Successfully populated database.")
print(ArticleCategory.objects.all())
print(Article.objects.all())

# exec(open("wiki/populate.db.py").read())