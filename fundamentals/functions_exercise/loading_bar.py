def loading_status(percent):
    if percent == 100:
        print("100% Complete!")
        print("["+"%"*10+"]")
    else:
        # status = "%" * int((percent/10))
        print(f"{percent}% [{'%' * int(percent/10)}{'.' * (10 - int(percent/10))}]")
        print("Still loading...")
        # print(status)

percentage = int(input())
loading_status(percentage)
