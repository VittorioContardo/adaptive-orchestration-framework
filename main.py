from experiments.experiments_runner import (
    ExperimentRunner
)


def summarize(results):

    successes = sum(
        1 for r in results
        if r["success"]
    )

    failures = len(results) - successes

    avg_retry = (
        sum(
            r["retry_count"]
            for r in results
        ) / len(results)
    )

    avg_score = (
        sum(
            r["global_score"]
            for r in results
        ) / len(results)
    )

    return {

        "successes": successes,

        "failures": failures,

        "avg_retry": avg_retry,

        "avg_score": avg_score
    }


baseline = summarize(

    ExperimentRunner
    .simulate_baseline(100)

)

adaptive = summarize(

    ExperimentRunner
    .simulate_adaptive(100)

)

print("\nBASELINE\n")
print(baseline)

print("\nADAPTIVE\n")
print(adaptive)


print("\nERROR PROPAGATION\n")

error_stats = (
    ExperimentRunner
    .simulate_error_propagation(100)
)

print(error_stats)

reduction = (

    (
        error_stats["baseline_errors"]
        -
        error_stats["adaptive_errors"]
    )

    /

    error_stats["baseline_errors"]

) * 100

print(
    f"\nError Propagation Reduction: "
    f"{reduction:.2f}%"
)


print("\nRETRY RECOVERY\n")

retry_stats = (
    ExperimentRunner
    .simulate_retry_recovery(100)
)

print(retry_stats)

recovery_rate = (

    retry_stats["recovered_errors"]

    /

    retry_stats["retry_attempts"]

) * 100

print(
    f"\nRetry Recovery Rate: "
    f"{recovery_rate:.2f}%"
)


print("\nROLLBACK EFFECTIVENESS\n")

rollback_stats = (

    ExperimentRunner
    .simulate_rollback_effectiveness(100)

)

print(rollback_stats)

rollback_success_rate = (

    rollback_stats[
        "restored_configurations"
    ]

    /

    rollback_stats[
        "rollback_activated"
    ]

) * 100

print(

    f"\nRollback Success Rate: "
    f"{rollback_success_rate:.2f}%"

)