mountain_in_japan = {
    "fuji": 3776,
    "kitadake": 3193,
    "okuhodakadake": 3190,
    "dummy": 0,
}
print(sorted(mountain_in_japan.items(), key=lambda x: x[1], reverse=True))
