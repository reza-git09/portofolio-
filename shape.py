import time
import sys

lyrics = [
    "I'm looking back on things I've done",
    "Trying to understand who I've become",
    "I used to hide the person inside",
    "Behind every smile, behind every lie",

    "Now I don't wanna run anymore",
    "I won't hide behind that door",
    "I'll let you see the real me",
    "The person I was meant to be",

    "This is the shape of my heart",
    "The broken pieces, every part",
    "It's not perfect, but it's true",
    "This is who I am to you",

    "I don't need to hide away",
    "I can face myself today",
    "All the scars that made me strong",
    "They were with me all along"
]

for line in lyrics:

    # Menampilkan huruf satu per satu
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)

    # Jeda setelah satu baris selesai
    print()
    time.sleep(1.5)