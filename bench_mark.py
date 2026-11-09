import json
import platform
import statistics   # NEW (change 1)
import subprocess
import sys
import time

command = [sys.executable, "-c", "pass"]
runs = 10
times = []

for i in range(runs):
    start = time.perf_counter()
    subprocess.run(command, stdout=subprocess.DEVNULL)
    end = time.perf_counter()
    times.append(end - start)

mean = sum(times) / runs
spread = max(times) - min(times)
stdev = statistics.stdev(times)   # NEW (change 2)

result = {
    "machine": {
        "os": platform.system(),
        "cpu": platform.processor(),
        "python": platform.python_version(),
    },
    "command": "python -c pass",
    "runs": runs,
    "times_seconds": times,
    "mean_seconds": mean,
    "spread_seconds": spread,
    "stdev_seconds": stdev,   # NEW (change 3)
}

with open("result.json", "w") as f:
    json.dump(result, f, indent=4)

print("Mean:", mean)
print("Spread:", spread)
print("Stdev:", stdev)   # NEW (change 4)
print("Saved to result.json")