country = input()
type_tool = input()

max_score = 20
total_score = 0
if country == "Russia":
    if type_tool == "ribbon":
        total_score = 9.1 + 9.4
    elif type_tool == "hoop":
        total_score = 9.3 + 9.8
    elif type_tool == "rope":
        total_score = 9.6 + 9
elif country == "Bulgaria":
    if type_tool == "ribbon":
        total_score = 9.6 + 9.4
    elif type_tool == "hoop":
        total_score = 9.55 + 9.75
    elif type_tool == "rope":
        total_score = 9.5 + 9.4
elif country == "Italy":
    if type_tool == "ribbon":
        total_score = 9.2 + 9.5
    elif type_tool == "hoop":
        total_score = 9.45 + 9.35
    elif type_tool == "rope":
        total_score = 9.7 + 9.15

percent_to_max = (1 - total_score / max_score) * 100
print(f"The team of {country} get {total_score:.3f} on {type_tool}.")
print(f"{percent_to_max:.2f}%")
