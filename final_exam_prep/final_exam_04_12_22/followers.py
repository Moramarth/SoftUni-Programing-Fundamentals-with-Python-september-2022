
followers = dict()

command = input()

while command != "Log out":
    data = command.split(": ")
    notification = data[0]
    username = data[1]
    if notification == "New follower":
        if username not in followers:
            # comments and likes can be split in a list to keep track of both
            followers[username] = 0
    elif notification == "Like":
        likes = int(data[2])
        if username not in followers:
            followers[username] = likes
        else:
            followers[username] += likes
    elif notification == "Comment":
        if username not in followers:
            followers[username] = 1
        else:
            followers[username] += 1
    elif notification == "Blocked":
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del followers[username]
    command = input()

print(f"{len(followers)} followers")
for user in followers:
    print(f"{user}: {followers[user]}")
