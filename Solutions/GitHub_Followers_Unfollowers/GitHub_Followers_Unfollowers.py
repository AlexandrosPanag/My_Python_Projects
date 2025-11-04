#Copyright (c) 2025 Alexandros Panagiotakopoulos
#All Rights Reserved
#DATE: 4/11/2025
#alexandrospanag.github.io


import requests

username = "your_github_username_here" # Replace with your GitHub username

followers = requests.get(f"https://api.github.com/users/{username}/followers").json()
following = requests.get(f"https://api.github.com/users/{username}/following").json()

followers_set = {f["login"] for f in followers}
following_set = {f["login"] for f in following}

not_following_back = following_set - followers_set

print("Users who don't follow you back:")
for user in not_following_back:
    print(user)
