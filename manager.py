"""wx"""
"""A corporate performance review nobody requested."""

import random


REVIEWS = [
    "You have demonstrated an impressive ability to continue existing.",
    "Your performance is difficult to measure, but we have decided to measure it anyway.",
    "You occasionally accomplish tasks. This is encouraging.",
    "Management has noticed your presence.",
    "Your productivity remains theoretically possible.",
    "You have shown leadership qualities, mostly by telling other people what to do.",
]

STRENGTHS = [
    "Existing",
    "Opening applications",
    "Closing applications",
    "Finding the power button",
    "Occasionally being productive",
    "Successfully completing this program",
]

WEAKNESSES = [
    "Everything else",
    "Time management",
    "Making decisions",
    "Starting tasks",
    "Finishing tasks",
    "Remembering why you opened the application",
]


def main():
    print("🏢 HUMAN RESOURCES PERFORMANCE EVALUATION")
    print("=" * 45)

    print()
    print("👤 Employee: You")
    print("📅 Review period: Since the beginning of time")

    print()
    print("📊 ANALYZING PERFORMANCE...")
    print("🧠 Reviewing questionable decisions...")
    print("📁 Consulting management archives...")

    score = random.uniform(4.0, 9.9)

    print()
    print("💪 STRENGTH:")
    print(f"   • {random.choice(STRENGTHS)}")

    print()
    print("📉 AREA FOR IMPROVEMENT:")
    print(f"   • {random.choice(WEAKNESSES)}")

    print()
    print("📝 MANAGEMENT COMMENT:")
    print(f'   "{random.choice(REVIEWS)}"')

    print()
    print(f"⭐ OVERALL SCORE: {score:.1f}/10")

    print()
    print("💰 SALARY INCREASE: No.")
    print("📈 PROMOTION: Also no.")
    print("🎁 COMPANY BENEFIT:")
    print("   You get to keep your job.")

    print()
    print("🏢 Thank you for participating in this completely pointless review.")


if __name__ == "__main__":
    main()
