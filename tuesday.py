"""made by weduofficial/weduxox"""
"""Is It Tuesday? A question science has already answered."""

from datetime import datetime


def main():
    today = datetime.now()

    if today.weekday() == 1:
        print("🚨 IT IS TUESDAY.")
        print("Proceed accordingly.")
    else:
        print("❌ It is not Tuesday.")
        print(f"Today is {today.strftime('%A')}.")
        print("You may continue living.")


if __name__ == "__main__":
    main()
  
