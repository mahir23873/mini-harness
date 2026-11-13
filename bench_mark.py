import json
import platform
import statistics
import subprocess
import sys
import time

command = [sys.executable, "-c", "pass"]
runs = 10

if len(sys.argv) > 2:
    runs = int(sys.argv[1])
    command = sys.argv[2:]

times = []

subprocess.run(command, stdout=subprocess.DEVNULL)  # warm-up, not timed

for i in range(runs):
    start = time.perf_counter()
    subprocess.run(command, stdout=subprocess.DEVNULL)
    end = time.perf_counter()
    times.append(end - start)

mean = sum(times) / runs
spread = max(times) - min(times)
stdev = statistics.stdev(times)

result = {
    "machine": {
        "os": platform.system(),
        "cpu": platform.processor(),
        "python": platform.python_version(),
    },
    "command": " ".join(command),
    "runs": runs,
    "warmup_runs": 1,
    "times_seconds": times,
    "mean_seconds": mean,
    "spread_seconds": spread,
    "stdev_seconds": stdev,
}

with open("result.json", "w") as f:
    json.dump(result, f, indent=4)

print("Mean:", mean)
print("Spread:", spread)
print("Stdev:", stdev)
print("Saved to result.json")