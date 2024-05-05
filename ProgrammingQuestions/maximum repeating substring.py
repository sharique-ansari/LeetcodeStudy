"""
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.
"""


def maxRepeating(sequence: str, word: str) -> int:
    # wrong solution
    g_max = 0
    c_max = 0

    pointer_seq = 0
    pointer_word = 0

    while pointer_seq < len(sequence):
        w_,w_c, s_,s_c = pointer_word, word[pointer_word], pointer_seq,sequence[pointer_seq]
        if word[pointer_word] == sequence[pointer_seq]:
            if pointer_word == len(word) - 1:
                c_max += 1
                if c_max > g_max:
                    g_max = c_max
                pointer_word = 0
            else:
                pointer_word += 1
        else:
            pointer_word = 0
            c_max = 0
        pointer_seq += 1
    return g_max


maxRepeating(sequence="aaabaaaabaaabaaaabaaaabaaaabaaaaba", word="aaaba")
