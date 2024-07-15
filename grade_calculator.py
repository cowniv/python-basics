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
