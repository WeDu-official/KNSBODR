"""wx-A weather forecast generated with questionable scientific methods."""

import random


CONDITIONS = [
    "Sunny",
    "Cloudy",
    "Suspiciously cloudy",
    "Extremely sunny",
    "Partly doing something",
    "Weather",
    "Probably hot",
    "Probably cold",
]

WINDS = [
    "Barely moving",
    "Doing its best",
    "Moderate-ish",
    "Aggressively horizontal",
    "Going somewhere",
    "Absolutely unnecessary",
]

ADVICE = [
    "Take an umbrella. Probably.",
    "Stay hydrated.",
    "Do not fight the weather.",
    "The sky appears to have plans.",
    "Wear clothes appropriate for being outside.",
    "Consider remaining indoors.",
    "Look out the window before making decisions.",
]


def main():
    temperature = random.randint(15, 48)
    humidity = random.randint(10, 95)

    print("🌦️ ADVANCED WEATHER ANALYSIS")
    print("=" * 35)

    print()
    print("📡 Connecting to atmospheric authorities...")
    print("☁️ Examining suspicious clouds...")
    print("🌬️ Interviewing the wind...")
    print("🔬 Performing extremely questionable meteorology...")

    print()
    print(f"🌡️ Temperature: {temperature}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁️ Conditions: {random.choice(CONDITIONS)}")
    print(f"💨 Wind: {random.choice(WINDS)}")

    print()
    print(f"📢 OFFICIAL ADVICE:")
    print(f"   {random.choice(ADVICE)}")

    print()
    print("⚠️ Forecast confidence: 37%")
    print("Weather department refuses to elaborate.")


if __name__ == "__main__":
    main()
