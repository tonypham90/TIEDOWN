# utils.py
import json


def save_job_config(job_data, filename):
    with open(filename, "w") as f:
        json.dump(job_data, f)


def load_job_config(filename):
    with open(filename, "r") as f:
        return json.load(f)
