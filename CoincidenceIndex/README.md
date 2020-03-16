
# Coincidence Index

An interesting idea to find the language used in a monoalphabetic substitution cipher.

Shifting and aligning the ciphertext and the plaintext, the number of times the letters
line up would provide some clue into which language is used in the cipher. The formula
to calculate the coincidence index(CI) is:

<a href="https://www.codecogs.com/eqnedit.php?latex=CI&space;=&space;\frac{\sum{a_i&space;==&space;b_i}}{N/c}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?CI&space;=&space;\frac{\sum{a_i&space;==&space;b_i}}{N/c}" title="CI = \frac{\sum{a_i == b_i}}{N/c}" /></a>

where a<sub>i</sub> and b<sub>i</sub> are the i<sup>th</sup> letters from the ciphertext and plaintext respectively, N is
the length of the aligned text, and c is the number of unique characters in the alphabet of
choice.

The method aims to relate the pattern of the language and
