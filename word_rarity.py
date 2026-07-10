with open("American Oxford 5000 Sorted.txt", "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]

freqs = {}

for w in words:
    if len(w) > 4:
        for i in range(len(w) - 1):
            pair = w[i] + w[i+1]
            
            if pair not in freqs:
                freqs[pair] = 1
            else:
                freqs[pair] += 1

target = input("Please enter your target word: ")
common_score = 0

for i in range(len(target) - 1):
    pair = target[i] + target[i+1]

    if pair not in freqs:
        freqs[pair] = 1
    else:
        common_score = freqs[pair]

rarity = min((1/common_score) * len(target), 1)
print(f"{rarity * 100}%")
