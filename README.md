# Mini Benchmark Harness

A small Python script that times a command several times and saves the results as JSON.

## Run
python bench_mark.py

## Output
result.json contains the machine details (OS, CPU, Python version), the command, every timing, the mean and the spread (max minus min).

## Why
I built this to understand how a benchmark harness and its noise floor work.

## Usage
    python bench_mark.py
    python bench_mark.py 50 python -c pass

The first number is how many runs. The rest is the command to time. One warm-up run is done first and not counted.

## Example results
Results vary with what the laptop is doing in the background:
- Quiet moment: mean about 25.7 ms, stdev about 1.4 ms (noise floor about 5%).
- Busier moment: mean about 28.3 ms, stdev about 3.0 ms (noise floor about 10%).

Lesson: the noise floor is not a fixed number. It changes with system load, so it has to be measured on every machine.

## Status
Complete. Possible future work: median and percentiles, and comparing results across machines.

