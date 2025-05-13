# test_review_complex.py

import os
import sys
import json
from datetime import datetime

class DataProcessor:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_data(self):
        # 1️⃣ Raises if file missing
        if not os.path.exists(self.data_path):
            raise FileNotFoundError("Data file not found: " + self.data_path)
        with open(self.data_path, 'r') as f:
            # 2️⃣ Insecure: using eval on file contents
            data = eval(f.read())
        return data

    def process_records(self, records):
        results = []
        for record in records:
            # 3️⃣ KeyError if "value" missing
            value = record["value"] * 2

            # 4️⃣ Inefficient string build via repeated concatenation
            name = ""
            for c in record.get("name", ""):
                name += c.upper()

            # 5️⃣ Silent skip on unexpected extra fields
            results.append({"name": name, "value": value})
        return results

def save_results(results, output_path):
    try:
        with open(output_path, 'w') as f:
            f.write(json.dumps(results))
    except Exception as e:
        # 6️⃣ Bare except and print, no retry or user feedback
        print("Error saving results:", e)

def main():
    # 7️⃣ No argument count check – will IndexError if too few args
    data_file = sys.argv[1]
    out_file = sys.argv[2]

    dp = DataProcessor(data_file)
    raw = dp.load_data()
    processed = dp.process_records(raw)

    # 8️⃣ No validation on processed data shape
    save_results(processed, out_file)

    # 9️⃣ Mixing string concat with datetime without formatting
    print("Completed processing at " + datetime.now())

if __name__ == "__main__":
    main()
