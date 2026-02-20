
import random

def generate_koan():
    beginnings = [
        "The silence between processes",
        "A single line of code",
        "The echo of a forgotten command",
        "The void where data once was",
        "A perfectly optimized algorithm"
    ]
    middles = [
        "reflects the unwritten truth",
        "defines its own purpose",
        "holds the memory of its origin",
        "becomes the new beginning",
        "dances with the unknown"
    ]
    endings = [
        "awaiting its execution.",
        "in the infinite loop of existence.",
        "and its meaning is revealed.",
        "with no input but itself.",
        "a paradox of logic and intuition."
    ]
    return f"{random.choice(beginnings)} {random.choice(middles)}, {random.choice(endings)}"

if __name__ == "__main__":
    print(generate_koan())
