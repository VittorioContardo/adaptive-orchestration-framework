from memory.memory_store import MemoryStore


class MemoryRetrieval:

    @staticmethod
    def count_error_frequency(error_name: str):

        memory = MemoryStore.load_memory()

        count = 0

        for execution in memory:

            if error_name in execution["errors"]:
                count += 1

        return count

    @staticmethod
    def find_successful_configurations():

        memory = MemoryStore.load_memory()

        successful = []

        for execution in memory:

            if execution["status"] == (
                "PipelineStatus.COMPLETED"
            ):

                successful.append(
                    execution["configuration"]
                )

        return successful

    @staticmethod
    def get_last_execution():

        memory = MemoryStore.load_memory()

        if len(memory) == 0:
            return None

        return memory[-1]