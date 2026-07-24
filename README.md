# lab1_aubin-karaha

# Grade Evaluator and File Organizer

In this program, we have 2 scripts: one calculates GPA and shows a pass/fail depending on a grades CSV file, the other archives that CSV and creates a new one.

## Files

- `grade-evaluator.py` - reads grades.csv, prints GPA, pass/fail, and if a student failed determines which formatives to resubmit
- `organizer.sh` - archives grades.csv and creates a new empty one

## Running grade-evaluator.py

```
python3 grade-evaluator.py
```

When asked for a filename, type `grades.csv`.

**CSV format:**

```
assignment,group,score,weight
```

- `group` is either `Formative` or `Summative`
- Formative weights must total 60, Summative weights must total 40 and total weight must be 100

**Rules:**

- Score must be between 0 and 100,or the script stops with an error
- Passing requires at least 50% of possible points in both Formative and Summative groups
- Resubmission applies only to Formative assignments scoring below 50; if more than one shares the highest weight, all are listed
- Missing or empty `grades.csv` is handled with a message instead of crashing

## Running organizer.sh

```
chmod +x organizer.sh
./organizer.sh
```

What happens:
- Creates an `archive` folder if missing
- Renames `grades.csv` with a timestamp and moves it into `archive`
- Creates a new empty `grades.csv`
- Adds a line to `organizer.log` (old entries are kept)

## Workflow

1. Fill in `grades.csv`
2. Run `grade-evaluator.py` to check GPA and status
3. Run `organizer.sh` to archive and reset
