import random


class ExperimentRunner:

    @staticmethod
    def run_experiments(num_runs=50):

        results = []

        for _ in range(num_runs):

            result = {
                "success": random.random() > 0.3,
                "retry_count": random.randint(0, 3),
                "global_score": round(
                    random.uniform(0.4, 0.95),
                    2
                )
            }

            results.append(result)

        return results