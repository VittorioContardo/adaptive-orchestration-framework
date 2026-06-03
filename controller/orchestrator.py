from models.pipeline_state import (
    PipelineState,
    PipelineStatus
)

from controller.state_manager import (
    StateManager
)

from controller.validator import Validator

from controller.decision_engine import (
    DecisionEngine
)

from controller.retry_manager import (
    RetryManager
)

from memory.memory_store import (
    MemoryStore
)

from agents.architect_agent import (
    ArchitectAgent
)

from agents.tradeoff_agent import (
    TradeoffAgent
)

from agents.documenter_agent import (
    DocumenterAgent
)


class Orchestrator:

    @staticmethod
    def execute_pipeline():

        state = PipelineState()

        StateManager.set_status(
            state,
            PipelineStatus.RUNNING
        )

        # loop pipeline
        while (
            state.status
            not in [
                PipelineStatus.FAILED,
                PipelineStatus.COMPLETED
            ]
        ):

            # STEP 1 — ARCHITECT
            StateManager.set_current_step(
                state,
                "ARCHITECT_AGENT"
            )

            architecture_output = (
                ArchitectAgent
                .generate_architecture()
            )

            validation_errors = (
                Validator
                .validate_architecture(
                    architecture_output
                )
            )

            # gestione errori
            if len(validation_errors) > 0:

                for error in validation_errors:

                    StateManager.add_error(
                        state,
                        error
                    )

                decision = (
                    DecisionEngine.decide(
                        state
                    )
                )

                RetryManager.execute_decision(
                    state,
                    decision
                )

                # restart loop
                continue

            # STEP 2 — TRADEOFF
            StateManager.set_current_step(
                state,
                "TRADEOFF_AGENT"
            )

            tradeoff_output = (
                TradeoffAgent
                .analyze_tradeoffs()
            )

            # STEP 3 — DOCUMENTER
            StateManager.set_current_step(
                state,
                "DOCUMENTER_AGENT"
            )

            documentation_output = (
                DocumenterAgent
                .generate_documentation()
            )

            # salvataggio output finali
            state.outputs = {

                "architecture":
                    architecture_output,

                "tradeoffs":
                    tradeoff_output,

                "documentation":
                    documentation_output
            }

            # pipeline completata
            StateManager.mark_completed(
                state
            )

        # persistenza memoria
        MemoryStore.save_execution({

            "status": str(state.status),

            "retry_count":
                state.retry_count,

            "corrective_actions":
                state.corrective_actions,

            "errors":
                state.errors,

            "history":
                state.history,

            "configuration":
                state.active_configuration
        })

        return state