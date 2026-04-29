def char_frequency(str):
    freq = {}
    for ch in str:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(char_frequency("hello"))
print(char_frequency("Apurbo"))
print(char_frequency("Kabbo"))
