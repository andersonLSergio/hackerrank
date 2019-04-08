def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        # Validation below causes Unit Tests to fail if a word has no vowels
        # But still, this is the correct answer, since no vowel should not considered as vowel pair
        if num_vowels > 0 and num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score
