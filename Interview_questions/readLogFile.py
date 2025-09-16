from collections import Counter

with open("/Users/shashi/Documents/Project/python3/Interview_questions/app.log") as f:
    ips=[line.split()[0] for line in f if line.strip()]
    print(Counter(ips).most_common(5))