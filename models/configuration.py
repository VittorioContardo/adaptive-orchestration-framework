from pydantic import BaseModel
from datetime import datetime


class ConfigurationVersion(BaseModel):

    configuration_name: str

    version_id: str

    global_score: float

    timestamp: str

    rollback_enabled: bool = True

    metadata: dict = {}