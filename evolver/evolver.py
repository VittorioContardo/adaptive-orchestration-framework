from memory.retrieval import MemoryRetrieval


class Evolver:

    ERROR_THRESHOLD = 2

    @staticmethod
    def evaluate_system():

        frequency = (
            MemoryRetrieval.count_error_frequency(
                "ErrorCategory.MISSING_FIELDS"
            )
        )

        if frequency >= Evolver.ERROR_THRESHOLD:

            return {
                "action":
                    "CHANGE_CONFIGURATION",

                "new_configuration":
                    "enhanced_prompt_template"
            }

        return {
            "action":
                "KEEP_CONFIGURATION"
        }