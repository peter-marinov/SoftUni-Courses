tabs = int(input())
salary = float(input())

facebook_cnt = 0
instagram_cnt = 0
reddit_cnt = 0
for i in range(1, tabs + 1):
    tab_name = input()
    if tab_name == "Facebook":
        facebook_cnt += 1
    elif tab_name == "Instagram":
        instagram_cnt += 1
    elif tab_name == "Reddit":
        reddit_cnt += 1

facebook_penalty = facebook_cnt * 150
instagram_penalty = instagram_cnt * 100
reddit_penalty = reddit_cnt * 50
# print(f"{facebook_penalty} {instagram_penalty} {reddit_penalty}")
total_penalty = facebook_penalty + instagram_penalty + reddit_penalty
# print(total_penalty)

if total_penalty >= salary:
    print("You have lost your salary.")
else:
    money_left = int(salary - total_penalty)
    print(f"{money_left}")
