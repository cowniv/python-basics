"""GWA calculator using the PUP grading scale - practicing functions, lists and dicts."""


def to_pup_grade(score):
    """Convert a percentage to the PUP 1.00-5.00 scale."""
    scale = [
        (97, 1.00), (94, 1.25), (91, 1.50), (88, 1.75), (85, 2.00),
        (82, 2.25), (79, 2.50), (76, 2.75), (75, 3.00),
    ]
    for minimum, grade in scale:
        if score >= minimum:
            return grade
    return 5.00


def compute_gwa(subjects):
    total_units = sum(s["units"] for s in subjects)
    weighted = sum(s["grade"] * s["units"] for s in subjects)
    return weighted / total_units if total_units else 0


def main():
    subjects = []
    count = int(input("How many subjects? "))

    for i in range(count):
        print(f"\nSubject {i + 1}")
        name = input("  Name: ")
        units = int(input("  Units: "))
        score = float(input("  Final score (%): "))
        subjects.append({"name": name, "units": units, "grade": to_pup_grade(score)})
