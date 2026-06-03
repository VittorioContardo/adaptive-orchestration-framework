from models.pipeline_state import PipelineState, PipelineStatus


class StateManager:

    @staticmethod
    def set_status(state: PipelineState, status: PipelineStatus):

        state.status = status
        state.history.append(f"Status changed to {status}")

    @staticmethod
    def set_current_step(state: PipelineState, step: str):

        state.current_step = step
        state.history.append(f"Current step: {step}")

    @staticmethod
    def add_error(state: PipelineState, error):

        state.errors.append(str(error))

        state.history.append(
            f"Error detected: {error}"
        )

    @staticmethod
    def increment_retry(state: PipelineState):

        state.retry_count += 1
        state.corrective_actions += 1

        state.history.append(
            f"Retry incremented: {state.retry_count}"
        )

    @staticmethod
    def mark_completed(state: PipelineState):

        state.status = PipelineStatus.COMPLETED
        state.final_message = "Pipeline completed successfully"

        state.history.append("Pipeline completed")

    @staticmethod
    def mark_failed(state: PipelineState, message: str):

        state.status = PipelineStatus.FAILED
        state.fatal_error = True
        state.final_message = message

        state.history.append(f"Pipeline failed: {message}")