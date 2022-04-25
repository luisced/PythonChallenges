satuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count(status):
    count = 0
    for i in status:
        if status[i] == "online":
            count += 1
    return count


print(online_count(satuses))
