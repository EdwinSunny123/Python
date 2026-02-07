
# 🎥 Section A: Control Structures & Logic Building (Use Cases 1–5)

# 1. Subscription Plan Validation

plan = "Premium"
# Task :
# Use  if-elif-else
# print streaming quality based on  plan

if plan == "Basic":
    print("Streaming Quality: SD")
elif plan == "Premium":
    print("Streaming Quality: HD")
elif plan == "Ultra":
    print("Streaming Quality: 4K")
else:
    print("Invalid plan")


# 2. Age Restriction Check

user_age = 15
# Task :
# Check if  user  can watch 18+ content
# print allowed / restricted message
if user_age >= 18:
    print("Access Granted: You can watch 18+ content.")
else:
    print("Access Restricted: You cannot watch 18+ content.")


# 3. Region Availability Check

country ="India"
# Task :
# print whether Netflix service is available in the region
available_countries = ["USA", "Canada", "UK", "Australia", "India"]
if country in available_countries:
    print("Netflix service is available in your region.")
else:
    print("Netflix service is not available in your region.")


# 4. Profile Limit Check

current_profiles = 4
max_profiles = 5
if current_profiles < max_profiles:
    print("New profile can be created.")
else:
    print("Maximum profile limit reached.")


# 5. Watch Time Limit Alert

Daily_watch_time = 3  # in hours
User_watch_time = 4  # in hours
# Task :
#  Print warning using condition
if User_watch_time > Daily_watch_time:
    print("Warning: You have exceeded your daily watch time limit.")
else:
    print("You are within your daily watch time limit.")


# 🔁 Section B: Loops & Iterations (Use Cases 6–10)


# 6. Recently Watched Shows

recently_watched = ["Stranger Things", "The Crown", "Black Mirror", "Money Heist"]
for show in recently_watched:
    print("Recently Watched Show:", show)


# 7. Episode Playback Counter

total_episodes = 10
for episode in range(1, total_episodes + 1):
    print("Playing Episode", episode)


# 8. Subscription Renewal Reminder

days_until_expiry = 2
reminders_sent = 0
while reminders_sent < 3 and days_until_expiry > 0:
    print("Reminder: Your subscription will expire in", days_until_expiry, "days.")
    reminders_sent += 1
    days_until_expiry -= 1
if days_until_expiry == 0:
    print("Your subscription has expired. Please renew to continue enjoying our services.")


# 9. Skip Skipped Episodes

episode_list = ["Episode 1", "Episode 2", "Skipped", "Episode 4", "Skipped", "Episode 6"]
for episode in episode_list:    
    if episode == "Skipped":
        continue
    print("Playing", episode)


# 10. Stop Auto-Play

auto_play_episodes = 10
for episode in range(1, auto_play_episodes + 1):
    if episode > 5:
        print("Auto-play stopped after 5 episodes.")
        break
    print("Auto-playing Episode", episode)  


# 🧠 Section C : List , Tuples , sets & Dictionaries 

# 11. Watchlist Management(list)

Watchlist = ["Dark","Money Heist","Stranger Things"]
Watchlist.append("The Witcher")
Watchlist.remove("Money Heist")
print("Total shows in Watchlist:", len(Watchlist))
print("Current Watchlist:", Watchlist)

# 12.Unique Genres  Watched (set)

watched_genres = ["Drama", "Sci-Fi", "Thriller", "Drama", "Action", "Sci-Fi"]
unique_genres = set(watched_genres)
print("Unique genres watched:", unique_genres)

# 13. Immutable Movie details (tuple)

movie_details = ("Inception", 2010, 8.8)
try:
    movie_details[1] = 2012  # Attempting to modify the tuple
except TypeError as e:
    print("Error:", e)
print("Movie Details:", movie_details)

# 14. user Profile Details (dictionary)

profile = {"name": "Alex", "plan": "Standard", "devices": 2}
profile["plan"] = "Premium"
print("Profile Details:")
for key, value in profile.items():
    print(f"{key}: {value}")

# 15. Rating Summary

ratings = {"Stranger Things": 8.7, "The Crown": 8.6, "Black Mirror": 8.8, "Money Heist": 8.3}
highest_rated_show = max(ratings, key=ratings.get)
print("Highest Rated Show:", highest_rated_show, "with rating", ratings[highest_rated_show])


# 🔤 Section D: Strings & Built-in Functions (Use Cases 16–18)

# 16. Show Name Formatting

show_name = "stranger things"
print("Uppercase:", show_name.upper())
print("Title Case:", show_name.title())

# 17. Password Strength Check

password = "netflix123"
if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")


# 18.Search History Analysis

search_history = ["Dark", "Stranger Things", "Dark", "Money Heist", "Dark", "The Crown"]
most_searched_show = max(set(search_history), key=search_history.count)
print("Most Searched Show:", most_searched_show)


# ⚙️  Sections E : Functions & Lambda 

# 19. User-Defined Function : watch Time 

def calculate_watch_time(episodes, hours_per_episode):
    return episodes * hours_per_episode
total_time = calculate_watch_time(10, 1.5)
print("Total Watch Time:", total_time, "hours")


# 20. Subscription Cost Calculator

def calculate_subscription_cost(plan):
    if plan == "Basic":
        return 8.99
    elif plan == "Standard":
        return 12.99
    elif plan == "Premium":
        return 15.99
    else:
        return 0
cost = calculate_subscription_cost("Premium")
print("Monthly Subscription Cost: $", cost)

# 21.Lambda Function : Discount

apply_discount = lambda price: price * 0.9
original_price = 15.99 
discounted_price = apply_discount(original_price)
print("Discounted Price: $", round(discounted_price, 2))

# 22. Function For  Content recommendation

def recommend_content(genre):
    if genre == "Sci-Fi":
        return ["Stranger Things", "Black Mirror"]
    elif genre == "Drama":
        return ["The Crown", "Breaking Bad"]
    elif genre == "Action":
        return ["Money Heist", "The Witcher"]
    else:
        return ["No recommendations available for this genre."]
recommendations = recommend_content("Sci-Fi")
print("Recommended Content:", recommendations)


# ⚡ Section F: Comprehensions (Use Cases 23–25)

# 23. Filter Adult Content

shows = [("Stranger Things", 16), ("The Crown", 18), ("Black Mirror", 18), ("Money Heist", 15)]
adult_shows = [show for show, age in shows if age >= 18]
print("18+ Content:", adult_shows)

# 24. Convert ratings Scale

ratings_out_of_10 = {"Stranger Things": 8.7, "The Crown": 8.6, "Black Mirror": 8.8, "Money Heist": 8.3}
ratings_out_of_5 = {show: round((rating / 10) * 5, 2) for show, rating in ratings_out_of_10.items()}
print("Ratings out of 5:", ratings_out_of_5)

# 25. Popular Shows Set 

watch_counts = {"Stranger Things": 1500000, "The Crown": 900000, "Black Mirror": 1200000, "Money Heist": 800000}
popular_shows = {show for show, count in watch_counts.items() if count > 1000000}
print("Popular Shows (over 1 million views):", popular_shows)



