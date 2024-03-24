# Vote tally by candidate


votes = ["Kim", "Kang", "Choi", "Kim", "Kang", "Choi", "Kim", "Choi", "Kang", "Choi", "Choi", "Kim", "Kang", "Kim", "Kim", "Kang", "Kang", "Kim", "Choi", "Kang", "Kim"]

vote_counter = {}

for name in votes:
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

print(vote_counter)