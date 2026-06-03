from models.errors import ErrorCategory


class DecisionEngine:

    MAX_RETRY = 3
    MAX_CORRECTIVE_ACTIONS = 5

    @staticmethod
    def decide(state):

        # controllo budget globale
        if (
            state.corrective_actions
            >= DecisionEngine.MAX_CORRECTIVE_ACTIONS
        ):

            return "FAIL_PIPELINE"

        # controllo retry massimi
        if (
            state.retry_count
            >= DecisionEngine.MAX_RETRY
        ):

            return "SWITCH_PROMPT"

        # controllo errori presenti
        if len(state.errors) > 0:

            if (
                "ErrorCategory.INVALID_STRUCTURE"
                in state.errors
            ):

                return "RETRY_WITH_FEEDBACK"

            if (
                "ErrorCategory.MISSING_FIELDS"
                in state.errors
            ):

                return "RETRY_WITH_HINTS"

        return "CONTINUE"