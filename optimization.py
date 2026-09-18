"""Optimization functions for selecting the most important patient based on their features.
"""
from minizinc import Instance, Solver

# TODO: Need to be explained by the Teacher.
MODEL = """
int: n;
array[1..n, 1..5] of 0..100: features;
array[1..5] of int: weights = [35, 25, 20, 10, 10];

var 1..n: patient;

solve maximize
    sum(j in 1..5)(weights[j] * features[patient, j]);
"""

PRIORITY_FEATURES = [
    "number_inpatient",
    "number_emergency",
    "number_diagnoses",
    "time_in_hospital",
    "num_medications",
]


def choose_patient(features: list[list[int]]) -> int:
    """Choose a patient based on their features using MiniZinc optimization.
    """
    instance = Instance(Solver.lookup("gecode"))
    instance.add_string(MODEL)

    instance["n"] = len(features)
    instance["features"] = features

    # MiniZinc counts from 1; pandas positions count from 0.
    return instance.solve()["patient"] - 1
