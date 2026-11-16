from pathlib import Path

print("=== My AI Study Planner ===")
name = input("Your name: ").strip()
goal = input("Your AI learning goal: ").strip()
days_text = input("Study days each week: ").strip()
hours_text = input("Study hours per day: ").strip()

days = int(days_text)
hours = float(hours_text)
weekly_hours = days * hours

print(f"{name}, you can study "
      f"{weekly_hours:g} hours per week.")

plan = f"""MY AI STUDY PLAN
Student: {name}
Learning goal: {goal}
Study days: {days}
Hours per day: {hours:g}
Weekly total: {weekly_hours:g} hours

SUGGESTED ACTIVITIES
1. Learn Python concepts
2. Practice short programs
3. Explore a Generative AI tool
4. Build one small Python project
5. Review and update GitHub
"""

print(plan)

Path("study_plan.txt").write_text(
    plan, encoding="utf-8"
)
print("Saved: study_plan.txt")

readme = f"""# My AI Study Planner

A Python project by {name}.

Goal: {goal}

Run: python planner.py

Output: study_plan.txt
"""

Path("README.md").write_text(
    readme, encoding="utf-8"
)
print("Saved: README.md")
