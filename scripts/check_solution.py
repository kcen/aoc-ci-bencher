import os
import sys
import json

solution_file = os.getenv("SOLUTION_FILE")
input_name = os.getenv("INPUT_NAME")

assert solution_file is not None, "Missing SOLUTION_FILE"
assert input_name is not None, "Missing INPUT_NAME"

with open(solution_file, "r") as f:
    data = json.load(f)

if input_name not in data:
    print(f"No solution for {input_name}, skipping check")

solution = json.load(sys.stdin)
p1 = solution['part_one']
p2 = solution['part_two']

e1 = data[input_name]['part_one']
e2 = data[input_name]['part_two']

assert p1 == e1, f"Mismatched solution for part 1 using input {input_name}. Expected `{e1}` but got `{p1}`"
assert p2 == e2, f"Mismatched solution for part 2 using input {input_name}. Expected `{e2}` but got `{p2}`"

print("solutions match, OK")