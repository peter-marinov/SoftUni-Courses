floors = int(input())
rooms = int(input())
room_type = ""
for f in range(floors, 0, -1):
    for r in range(0, rooms):   #0, 1, 2, 3
        # if f == floors:
        #     print(f"L{f}{r}", end=" ")
        # elif f % 2 == 0:
        #     print(f"0{f}{r}", end=" ")
        # else:
        #     print(f"A{f}{r}", end=" ")
        if f == floors:
            room_type = "L"
        elif f % 2 != 0:
            room_type = "A"
        elif f % 2 == 0:
            room_type = "O"
        print(f"{room_type}{f}{r}",  end=" ")
    print()