from models.pipeline_state import PipelineStatus
from controller.state_manager import StateManager


class RetryManager:

    @staticmethod
    def execute_decision(state, decision):

        if decision == "RETRY_WITH_FEEDBACK":

            StateManager.increment_retry(state)

            StateManager.set_status(
                state,
                PipelineStatus.RETRY
            )

            state.history.append(
                "Executing retry with feedback"
            )

        elif decision == "RETRY_WITH_HINTS":

            StateManager.increment_retry(state)

            StateManager.set_status(
                state,
                PipelineStatus.RETRY
            )

            state.history.append(
                "Executing retry with hints"
            )

        elif decision == "SWITCH_PROMPT":

            state.corrective_actions += 1

            state.active_configuration = (
                "alternative_prompt"
            )

            state.history.append(
                "Switching prompt template"
            )

        elif decision == "FAIL_PIPELINE":

            StateManager.mark_failed(
                state,
                "Maximum corrective actions reached"
            )

        elif decision == "CONTINUE":

            StateManager.mark_completed(state)