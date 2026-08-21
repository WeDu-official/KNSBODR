"""weduxox"""
"""Are You Sure? The deletion program that deletes absolutely nothing. and reminds me of amount of confirms yay/pacman want from you when you wanna goon to catgirls"""

import time


QUESTIONS = [
    "Are you sure? [y/n] ",
    "Are you REALLY sure? [y/n] ",
    "Are you sure you're sure? [y/n] ",
    "Please confirm that you have confirmed. [y/n] ",
    "This is your final opportunity to reconsider. [y/n] ",
    "Think carefully. The computer is judging you. [y/n] ",
    "Last confirmation. Probably. [y/n] ",
]


def ask(question: str) -> bool:
    while True:
        answer = input(question).strip().lower()

        if answer in {"y", "yes"}:
            return True

        if answer in {"n", "no"}:
            return False

        print("Please answer with 'y' or 'n'.")


def main():
    print("🗑️  DELETE SYSTEM")
    print("Target: Absolutely Nothing")
    print()

    for question in QUESTIONS:
        if not ask(question):
            print()
            print("❌ Operation cancelled.")
            print("Nothing was deleted.")
            return

    print()
    print("⚠️ Initiating deletion...")
    time.sleep(0.5)
    print("🔍 Searching for something to delete...")
    time.sleep(0.5)
    print("📦 Found: nothing.")
    time.sleep(0.5)
    print("🗑️ Deleting nothing...")
    time.sleep(0.5)
    print("✅ Nothing has been successfully deleted.")
    print()
    print("Congratulations. You have accomplished absolutely nothing.")


if __name__ == "__main__":
    main()

