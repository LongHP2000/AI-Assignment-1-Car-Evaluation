# ============================================================
# AI ASSESSMENT 1
# PERFORMANCE COMPARISON GRAPHS
#
# Algorithm 1: Flat Rule-Based AI
# Algorithm 2: Hierarchical Rule-Based AI
#
# Dataset: Car Evaluation Dataset
#
# Purpose:
# Create three graphs comparing the two algorithms.
#
# Graph 1: Classification Accuracy
# Graph 2: Macro F1-Score
# Graph 3: Execution Time
#
# AI-assisted code: Review and understand before submission.
# ============================================================


# STEP 1: IMPORT LIBRARIES

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


# STEP 2: LOCATE THE RESULTS FILE

BASE = Path(__file__).resolve().parent

RESULTS = BASE / "results"

CSV_FILE = RESULTS / "summary.csv"


# STEP 3: CHECK THAT THE FILE EXISTS

if not CSV_FILE.exists():

    raise SystemExit(
        "Cannot find results/summary.csv. "
        "Run compare_algorithms.py first."
    )


# STEP 4: READ THE EXPERIMENTAL RESULTS

with CSV_FILE.open(
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    rows = list(reader)


# STEP 5: CHECK THE REQUIRED COLUMNS

required_columns = {
    "Algorithm",
    "Records",
    "Accuracy",
    "Macro_F1",
    "Execution_Time_ms"
}

if not rows or not required_columns.issubset(rows[0]):

    raise SystemExit(
        "summary.csv is empty or is missing required columns."
    )


# STEP 6: EXTRACT THE PERFORMANCE VALUES

try:

    algorithm_names = [
        row["Algorithm"] + " rules"
        for row in rows
    ]

    accuracy = [
        float(row["Accuracy"]) * 100
        for row in rows
    ]

    macro_f1 = [
        float(row["Macro_F1"])
        for row in rows
    ]

    execution_time = [
        float(row["Execution_Time_ms"])
        for row in rows
    ]

except ValueError as error:

    raise SystemExit(
        f"Cannot read a numerical result: {error}"
    )


# STEP 7: CREATE A REUSABLE GRAPH FUNCTION

def create_graph(
    values,
    title,
    ylabel,
    filename,
    maximum,
    number_format
):

    # Create the figure

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    # Create the bar chart

    bars = ax.bar(
        algorithm_names,
        values,
        width=0.55
    )

    # Add chart title

    ax.set_title(
        title,
        fontsize=13,
        fontweight="bold"
    )

    # Label the vertical axis

    ax.set_ylabel(ylabel)

    # Set the vertical axis range

    ax.set_ylim(0, maximum)

    # Add horizontal grid lines

    ax.grid(
        axis="y",
        alpha=0.2
    )

    ax.set_axisbelow(True)

    # Display the actual values above each bar

    for bar, value in zip(bars, values):

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + maximum * 0.025,
            number_format.format(value),
            ha="center",
            va="bottom",
            fontsize=11
        )

    # Add the source and evaluation limitation

    fig.text(
        0.5,
        0.02,
        "Source: Python experiment using the Car Evaluation Dataset; "
        "full-dataset evaluation, not held-out testing.",
        ha="center",
        fontsize=8
    )

    # Adjust the layout

    fig.tight_layout(
        rect=(0, 0.06, 1, 1)
    )

    # Save the graph

    output_path = RESULTS / filename

    fig.savefig(
        output_path,
        dpi=300
    )

    # Close the graph

    plt.close(fig)

    print(
        f"Saved: {output_path.name}"
    )


# ============================================================
# STEP 8: GRAPH 1 - CLASSIFICATION ACCURACY
# ============================================================

create_graph(
    accuracy,
    "Figure 1. Classification Accuracy Comparison",
    "Accuracy (%)",
    "figure_1_accuracy.png",
    100,
    "{:.2f}%"
)


# ============================================================
# STEP 9: GRAPH 2 - MACRO F1-SCORE
# ============================================================

create_graph(
    macro_f1,
    "Figure 2. Macro F1-Score Comparison",
    "Macro F1-score (0 to 1)",
    "figure_2_macro_f1.png",
    1,
    "{:.4f}"
)


# ============================================================
# STEP 10: GRAPH 3 - EXECUTION TIME
# ============================================================

create_graph(
    execution_time,
    "Figure 3. Execution Time Comparison",
    "Average time per full-dataset pass (ms)",
    "figure_3_execution_time.png",
    max(execution_time) * 1.25,
    "{:.3f} ms"
)


# ============================================================
# STEP 11: CONFIRM SUCCESS
# ============================================================

print("\nAll three comparison graphs created successfully!")