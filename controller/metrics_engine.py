class MetricsEngine:

    REQUIRED_FIELDS = [
        "architecture",
        "components",
        "scalability"
    ]

    @staticmethod
    def compute_coverage(output: dict):

        covered = 0

        for field in (
            MetricsEngine.REQUIRED_FIELDS
        ):

            if field in output:
                covered += 1

        return covered / len(
            MetricsEngine.REQUIRED_FIELDS
        )

    @staticmethod
    def compute_retry_efficiency(
        retry_count: int
    ):

        if retry_count == 0:
            return 1.0

        return 1 / retry_count

    @staticmethod
    def compute_error_frequency(
        error_count: int
    ):

        return min(error_count / 10, 1.0)

    @staticmethod
    def compute_validity(
        validation_errors: list
    ):

        if len(validation_errors) == 0:
            return 1.0

        return 0.0

    @staticmethod
    def compute_global_score(

        coverage: float,

        retry_efficiency: float,

        error_frequency: float,

        validity: float
    ):

        return (

            (coverage * 0.4)

            +

            (retry_efficiency * 0.2)

            +

            ((1 - error_frequency) * 0.2)

            +

            (validity * 0.2)
        )