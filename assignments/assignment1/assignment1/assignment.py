
import math
import random

with open("words.txt", 'r') as f:
    WORDS = [word for word in f.read().splitlines() if len(word) >= 3]

def estimate_pi(precision):
    in_square = 10**precision
    in_circle = 0

    for i in range(in_square):
        if i%1000000 == 0:
            print(f"{i/in_square:.0%}")
        # Check that the random point falls within the circle
        x, y = random.random(), random.random()
        if math.sqrt((x-0.5)**2 + (y-0.5)**2) <= 0.5:
            in_circle += 1

    # Come back to this so you can calculate to fixed points
    return (4*in_circle)/in_square

def caesar_cipher(txt):
    all_sentences = []
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Generate all 25 other combinations of the caesar cipher
    for offset in range(1, 26):
        current_sentence = ''
        for letter in txt:
            if letter.upper() in ALPHABET:
                current_sentence += ALPHABET[(ALPHABET.index(letter)+offset) % 26]
            else:
                current_sentence += letter
        all_sentences.append({"decrypted text": current_sentence, "offset": offset})

    # Start ranking the outputs based on how many english words they contain
    for idx, sentence in enumerate(all_sentences):
        score = 0
        for word in WORDS:
            if word in sentence["decrypted text"].lower():
                score += 1
        all_sentences[idx]["score"] = score

    all_sentences.sort(key=lambda x: x["score"], reverse=True)
    
    most_likely = all_sentences[0]
    print(f"I think {txt} decrypts to {most_likely['decrypted text']} (offset of {most_likely['offset']})")

def main():
    print("Question 4")
    print(estimate_pi(8))

    print("Question 5")
    caesar_cipher("AOLPTWVZAVYPZZBZ")

if __name__ == '__main__':
    main()