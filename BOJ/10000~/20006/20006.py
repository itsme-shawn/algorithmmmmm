import sys
# sys.stdin = open("in.txt", "r")

read = sys.stdin.readline

p,m = map(int, read().split())
rooms = []
for _ in range(p):
    uid, name = read().split()
    if not rooms:
        rooms.append([(uid,name)])
    else:
        for room in rooms:
            room_master_id = int(room[0][0])
            if len(room) < m and room_master_id - 10 <= int(uid) <= room_master_id + 10:
                room.append((uid,name))
                break
        else:
            rooms.append([(uid,name)])


for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for uid,name in sorted(room, key=lambda x : x[1]):
        print(uid, name)