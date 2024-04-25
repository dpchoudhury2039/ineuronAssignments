subjects = ["Americans", "Indians"]
verbs = ["play", "watch"]
objects = ["Baseball", "Cricket"]

sentences = []
for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = f"{subject} {verb} {obj}."
            sentences.append(sentence)


for sentence in sentences:
    print(sentence)
