# ============================================================
# AI ASSESSMENT 1
# COMPARISON OF TWO RULE-BASED AI ALGORITHMS
#
# Algorithm 1: Flat Rule-Based AI
# Algorithm 2: Hierarchical Rule-Based AI
#
# Dataset: Car Evaluation Dataset
#
# AI-assisted code: Review and understand before submission.
# ============================================================


# STEP 1: IMPORT PYTHON LIBRARIES

import csv
from pathlib import Path
from time import perf_counter


# STEP 2: IMPORT BOTH AI ALGORITHMS

from flat_rules import classify_car as classify_flat
from hierarchical_rules import classify_car as classify_hierarchical


# STEP 3: DEFINE CLASSIFICATIONS

CLASSES = ("unacc", "acc", "good", "vgood")

BASE = Path(__file__).resolve().parent


# STEP 4: LOAD THE CAR EVALUATION DATASET

def load_dataset():

    file_path = BASE / "data" / "car.data"

    with file_path.open(
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.reader(file)

        records = [
            row for row in reader
            if row
        ]

    # Check that every record contains seven columns

    for row in records:

        if len(row) != 7:

            raise ValueError(
                "Each record must contain six attributes "
                "and one classification."
            )

    return records


# STEP 5: EVALUATE AN AI ALGORITHM

def evaluate(classifier, records):

    # Create an empty confusion matrix

    matrix = {
        actual: {
            predicted: 0
            for predicted in CLASSES
        }
        for actual in CLASSES
    }

    # Test every vehicle

    for row in records:

        car = row[:6]

        actual = row[6]

        prediction = classifier(car)

        if actual not in CLASSES or prediction not in CLASSES:

            raise ValueError(
                f"Unexpected classification: "
                f"{actual}, {prediction}"
            )

        matrix[actual][prediction] += 1

    # Calculate classification accuracy

    correct = sum(
        matrix[label][label]
        for label in CLASSES
    )

    accuracy = correct / len(records)

    # Calculate precision, recall and F1-score

    details = []

    for label in CLASSES:

        true_positive = matrix[label][label]

        predicted_total = sum(
            matrix[actual][label]
            for actual in CLASSES
        )

        actual_total = sum(
            matrix[label].values()
        )

        if predicted_total > 0:

            precision = true_positive / predicted_total

        else:

            precision = 0.0

        if actual_total > 0:

            recall = true_positive / actual_total

        else:

            recall = 0.0

        if precision + recall > 0:

            f1 = (
                2 * precision * recall
                / (precision + recall)
            )

        else:

            f1 = 0.0

        details.append(
            (label, precision, recall, f1)
        )

    # Calculate macro F1-score

    macro_f1 = sum(
        result[3]
        for result in details
    ) / len(CLASSES)

    # STEP 6: MEASURE EXECUTION TIME

    repetitions = 100

    start = perf_counter()

    for _ in range(repetitions):

        for row in records:

            classifier(row[:6])

    end = perf_counter()

    elapsed_ms = (
        (end - start) * 1000 / repetitions
    )

    return (
        accuracy,
        macro_f1,
        elapsed_ms,
        matrix,
        details
    )


# STEP 7: SAVE CONFUSION MATRIX

def save_confusion_matrix(filename, matrix):

    file_path = BASE / "results" / filename

    with file_path.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Actual / Predicted", *CLASSES]
        )

        for actual in CLASSES:

            writer.writerow(
                [
                    actual,
                    *(
                        matrix[actual][predicted]
                        for predicted in CLASSES
                    )
                ]
            )


# STEP 8: RUN BOTH ALGORITHMS

def main():

    print("=" * 55)

    print("AI ASSESSMENT 1")

    print("FLAT VS HIERARCHICAL RULE-BASED AI")

    print("=" * 55)

    # Load dataset

    records = load_dataset()

    print(
        f"\nTotal vehicle records: {len(records)}"
    )

    # Create results folder

    results_folder = BASE / "results"

    results_folder.mkdir(exist_ok=True)

    summary = []

    # Compare both algorithms

    algorithms = [
        ("Flat", classify_flat),
        ("Hierarchical", classify_hierarchical)
    ]

    for name, classifier in algorithms:

        (
            accuracy,
            macro_f1,
            elapsed_ms,
            matrix,
            details
        ) = evaluate(classifier, records)

        print("\n" + "=" * 55)

        print(
            f"ALGORITHM: {name.upper()} RULE-BASED AI"
        )

        print("=" * 55)

        print(
            f"Accuracy: {accuracy:.2%}"
        )

        print(
            f"Macro F1-score: {macro_f1:.4f}"
        )

        print(
            f"Execution time: {elapsed_ms:.3f} ms"
        )

        print("\nCLASSIFICATION PERFORMANCE")

        print("-" * 55)

        for label, precision, recall, f1 in details:

            print(
                f"{label:6} | "
                f"Precision: {precision:.3f} | "
                f"Recall: {recall:.3f} | "
                f"F1: {f1:.3f}"
            )

        # Save confusion matrix

        save_confusion_matrix(
            f"confusion_{name.lower()}.csv",
            matrix
        )

        # Store results

        summary.append(
            [
                name,
                len(records),
                accuracy,
                macro_f1,
                elapsed_ms
            ]
        )

    # STEP 9: SAVE COMPARISON RESULTS

    summary_path = results_folder / "summary.csv"

    with summary_path.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Algorithm",
                "Records",
                "Accuracy",
                "Macro_F1",
                "Execution_Time_ms"
            ]
        )

        writer.writerows(summary)

    print("\n" + "=" * 55)

    print("EXPERIMENT COMPLETED SUCCESSFULLY!")

    print("Results saved in the results folder.")

    print("=" * 55)


# STEP 10: START PROGRAMME

if __name__ == "__main__":

    main()