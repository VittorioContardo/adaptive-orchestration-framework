from datetime import datetime

from memory.configuration_store import (
    ConfigurationStore
)

from controller.rollback_engine import (
    RollbackEngine
)


# salvataggio configurazione precedente
ConfigurationStore.save_configuration({

    "configuration_name":
        "default_prompt",

    "version_id":
        "v1",

    "global_score":
        0.8,

    "timestamp":
        str(datetime.now())
})


# score corrente peggiore
current_score = 0.5


print("\nCURRENT SCORE:\n")
print(current_score)


rollback_needed = (
    RollbackEngine.should_rollback(
        current_score
    )
)

print("\nROLLBACK NEEDED:\n")
print(rollback_needed)


if rollback_needed:

    previous = (
        RollbackEngine.rollback()
    )

    print("\nROLLBACK CONFIGURATION:\n")

    print(previous)