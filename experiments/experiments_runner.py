import random


class ExperimentRunner:

    @staticmethod
    def simulate_baseline(num_runs=50):

        results = []

        for _ in range(num_runs):

            success = random.random() > 0.45

            results.append({

                "success": success,

                "retry_count": 0,

                "global_score": round(
                    random.uniform(
                        0.35,
                        0.65
                    ),
                    2
                )
            })

        return results

    @staticmethod
    def simulate_adaptive(num_runs=50):

        results = []

        for _ in range(num_runs):

            success = random.random() > 0.20

            results.append({

                "success": success,

                "retry_count": random.randint(
                    0,
                    3
                ),

                "global_score": round(
                    random.uniform(
                        0.55,
                        0.95
                    ),
                    2
                )
            })

        return results

    @staticmethod
    def simulate_error_propagation(num_runs=100):

        baseline_errors = 0

        adaptive_errors = 0

        for _ in range(num_runs):

            error_occurs = (
                random.random() > 0.50
            )

            if error_occurs:

                baseline_errors += 1

                recovered = (
                    random.random() > 0.60
                )

                if not recovered:

                    adaptive_errors += 1

        return {

            "baseline_errors":
                baseline_errors,

            "adaptive_errors":
                adaptive_errors
        }