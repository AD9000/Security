
# Coincidence Index

An interesting idea to find the language used in a monoalphabetic substitution cipher.

Shifting and aligning the ciphertext and the plaintext, the number of times the letters
line up would provide some clue into which language is used in the cipher. The formula
to calculate the coincidence index(CI) is:

$$
CI = \frac{\sum{a_i == b_i}}{N/c}
$$

where a_i and b_i are the i^th letters from the ciphertext and plaintext respectively, N is
the length of the aligned text, and c is the number of unique characters in the alphabet of
choice.

The method aims to relate the pattern of the language and
