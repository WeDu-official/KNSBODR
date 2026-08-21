"""by you guessed it weduofficial or weduxox its same person but two names... god i gotta replace this"""
"""Excuse Generator with no AI: it gives you none AI generated excused to prevent AI slop and instead gives you human slop."""

import argparse
import random


EXCUSES = [
    "My alarm clock and I had a disagreement.",
    "I was ready, but my brain wasn't.",
    "The Wi-Fi was emotionally unavailable.",
    "I completely forgot that today was a day.",
    "My computer needed a moment to process existence.",
    "I was prevented from leaving by an extremely complicated door.",
    "I had everything under control until I actually had to do it.",
    "My schedule was attacked by unexpected mathematics.",
    "I started doing it and then somehow ended up staring at the wall.",
    "The file was there yesterday. I swear.",
    "I was going to do it, but future me seemed more qualified.",
    "My keyboard entered a period of personal reflection.",
    "I encountered a technical issue between my brain and reality.",
    "I had a perfectly reasonable explanation, but I forgot that too.",
    "The instructions were written in a suspiciously complicated way.",
    "I was busy solving a completely unrelated problem that suddenly became important.",
    "My computer decided today was maintenance day.",
    "I underestimated how much time doing nothing would take.",
    "There was an administrative incident involving my motivation.",
    "I was temporarily unavailable due to unforeseen circumstances.",
    "I thought I had more time. Time disagreed.",
    "My brain was still loading.",
    "I was distracted by an important thought that turned out to be completely useless.",
    "I accidentally entered productivity cooldown.",
    "The universe provided insufficient documentation.",
    "I had technical difficulties with the concept of starting.",
    "I was operating on a different timezone internally.",
    "I genuinely believed I had already done it.",
    "I was waiting for the optimal moment. It did not arrive.",
    "My productivity encountered an unexpected exception.",
]


def main():
    parser = argparse.ArgumentParser(
        description="Generate a completely questionable excuse."
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1,
        help="Number of excuses to generate (default: 1)",
    )
    args = parser.parse_args()

    if args.number <= 0:
        parser.error("Number of excuses must be positive.")

    for _ in range(args.number):
        print(f"📝 {random.choice(EXCUSES)}")


if __name__ == "__main__":
    main()

