"""
Default grading policy for a course run.
"""

default_grading_policy = {
    "GRADER": [
        {
            "type": "Homework",
            "min_count": 12,
            "drop_count": 2,
            "short_label": "HW",
            "weight": 0.15,
        },
        {
            "type": "Lab",
            "min_count": 12,
            "drop_count": 2,
            "weight": 0.15,
        },
        {
            "type": "Midterm Exam",
            "short_label": "Midterm",
            "min_count": 1,
            "drop_count": 0,
            "weight": 0.3,
        },
        {
            "type": "Final Exam",
            "short_label": "Final",
            "min_count": 1,
            "drop_count": 0,
            "weight": 0.4,
        }
    ],
    "GRADE_CUTOFFS": {
        "Pass": 0.5,
    },
}
