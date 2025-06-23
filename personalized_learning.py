# personalized_learning.py

import json

# Load learning resources from JSON
def load_resources():
    with open('resources.json', 'r') as file:
        return json.load(file)

# Recommend based on score and style
def recommend_resources(score, style, resources):
    if score < 40:
        level = "beginner"
    elif 40 <= score < 70:
        level = "intermediate"
    else:
        level = "advanced"

    print(f"\n📚 Based on your score and learning style, here are your recommended {level.capitalize()} resources:\n")

    for item in resources[level][style]:
        print(f"🔹 {item['title']}")
        print(f"   Link: {item['link']}\n")

# Main app
def main():
    print("🎓 Welcome to AI-Powered Personalized Learning System\n")

    try:
        score = int(input("📊 Enter your latest quiz/test score (out of 100): "))
    except ValueError:
        print("❌ Invalid score. Please enter a number.")
        return

    print("\n🧠 Choose your preferred learning style:")
    print("1. Video")
    print("2. Article")
    print("3. Quiz/Practice")

    choice = input("Enter 1/2/3: ").strip()
    style_map = {"1": "video", "2": "article", "3": "quiz"}
    style = style_map.get(choice)

    if not style:
        print("❌ Invalid choice.")
        return

    # Load and recommend
    resources = load_resources()
    recommend_resources(score, style, resources)

# Run
if __name__ == "__main__":
    main()
