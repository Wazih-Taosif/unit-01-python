fruits = {
    "apples" : 10,
    "oranges" : 15,
}
fruits["oranges"] = 20
print(fruits["oranges"])
fruits["lemons"] = 15
print(fruits)
del fruits["oranges"]
print(fruits)