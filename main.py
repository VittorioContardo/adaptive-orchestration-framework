from experiments.experiments_runner import (
    ExperimentRunner
)

results = (
    ExperimentRunner
    .run_experiments(50)
)

successes = sum(
    1 for r in results
    if r["success"]
)

failures = len(results) - successes

average_retry = (
    sum(
        r["retry_count"]
        for r in results
    ) / len(results)
)

average_score = (
    sum(
        r["global_score"]
        for r in results
    ) / len(results)
)

print("\nRESULTS\n")

print(
    f"Runs: {len(results)}"
)

print(
    f"Successes: {successes}"
)

print(
    f"Failures: {failures}"
)

print(
    f"Average Retry: "
    f"{average_retry:.2f}"
)

print(
    f"Average Score: "
    f"{average_score:.2f}"
)