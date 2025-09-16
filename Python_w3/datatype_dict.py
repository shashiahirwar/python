sentance = "python is fun and python is powerful and python is easy"

words = sentance.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) +1

print(word_count)


student = {
    "name": "Alice",
    "age": 25,
    "courses": ["Python", "Kubernetes"],
    "graduated": True
}

print(student["name"])     # Alice
print(student["courses"])  # ['Python', 'Kubernetes']

print(student["age"])          # 25
print(student.get("city", "Not Found"))  # Not Found (safe access)
