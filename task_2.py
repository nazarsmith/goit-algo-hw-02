from collections import deque
import re


def check_palindrome(data: str = "tenet"):
    word = re.sub("[\!\?'\",.:;\-\ ]", "", data)
    dq = deque([letter for letter in word.lower()])

    while True:
        if dq.pop() == dq.popleft():
            if len(dq) <= 1:
                return f'"{data}" is palindrome: {True}'
        else:
            return f'"{data}" is palindrome: {False}'


if __name__ == "__main__":
    palindromes = [
        "level",
        "radar",
        "civic",
        "rotor",
        "kayak",
        "madam",
        "racecar",
        "deed",
        "refer",
        "civic",
        "rotor",
        "noon",
        "stats",
        "redder",
        "tenet",
        "A man, a plan, a canal, Panama!",
        "Was it a car or a cat I saw?",
        "No lemon, no melon.",
        "Evil is a name of a foeman, as I live.",
        "Step on no pets.",
        "Do geese see God?",
        "Mr. Awl ate my metal worm.",
        "Madam, in Eden I'm Adam.",
        "A Santa lived as a devil at NASA.",
        "Murder for a jar of red rum.",
        "level",
        "radar",
        "sivic",
        "rotor",
        "kayaks",
        "madame",
        "racecar",
        "deeds",
        "refler",
        "civic",
        "rotok",
        "nosdon",
        "stats",
        "redder",
        "tenat",
        "the man, a plan, a canal, Panama!",
        "Was et a car or a cat I saw?",
        "No lemon, no melon.",
        "Evil is a name of a foeman, as I live.",
        "Step on no pets.",
        "Do geese see God?",
        "Mr. Owl ate my metal worm.",
        "Madam, in Edem I'm Adam.",
        "A Santa lived as a devil at NASA.",
        "Murder for a jar ol red rum.",
    ]
    for pali in palindromes:
        print(check_palindrome(pali))
