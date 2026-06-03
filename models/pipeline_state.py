from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel


class PipelineStatus(str, Enum):
    INIT = "INIT"
    RUNNING = "RUNNING"
    VALIDATION = "VALIDATION"
    RETRY = "RETRY"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class PipelineState(BaseModel):

    # stato corrente della pipeline
    status: PipelineStatus = PipelineStatus.INIT

    # step corrente
    current_step: str = "START"

    # output prodotti dagli agenti
    outputs: Dict = {}

    # metriche raccolte
    metrics: Dict = {}

    # errori osservati
    errors: List[str] = []

    # numero retry
    retry_count: int = 0

    # numero totale azioni correttive
    corrective_actions: int = 0

    # configurazione attiva
    active_configuration: str = "default"

    # storico azioni
    history: List[str] = []

    # flag errore fatale
    fatal_error: bool = False

    # messaggio finale
    final_message: Optional[str] = None