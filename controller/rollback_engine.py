from memory.configuration_store import (
    ConfigurationStore
)


class RollbackEngine:

    @staticmethod
    def should_rollback(
        current_score: float
    ):

        configurations = (
            ConfigurationStore
            .load_configurations()
        )

        if len(configurations) == 0:
            return False

        last_configuration = (
            configurations[-1]
        )

        previous_score = (
            last_configuration[
                "global_score"
            ]
        )

        return current_score < previous_score

    @staticmethod
    def rollback():

        configurations = (
            ConfigurationStore
            .load_configurations()
        )

        if len(configurations) == 0:
            return None

        return configurations[-1]