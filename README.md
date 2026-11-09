# Mini Benchmark Harness

A small Python script that times a command several times and saves the results as JSON.

## Run
python bench_mark.py

## Output
result.json contains the machine details (OS, CPU, Python version), the command, every timing, the mean and the spread (max minus min).

## Why
I built this to understand how a benchmark harness and its noise floor work, inspired by the LFX project on benchmarking Duranta-OAI.
