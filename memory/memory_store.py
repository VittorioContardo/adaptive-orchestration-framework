import json
import os


class MemoryStore:

    MEMORY_FILE = "storage/memory.json"

    @staticmethod
    def initialize_memory():

        if not os.path.exists(
            MemoryStore.MEMORY_FILE
        ):

            with open(
                MemoryStore.MEMORY_FILE,
                "w"
            ) as file:

                json.dump([], file)

    @staticmethod
    def save_execution(data: dict):

        MemoryStore.initialize_memory()

        with open(
            MemoryStore.MEMORY_FILE,
            "r"
        ) as file:

            memory = json.load(file)

        memory.append(data)

        with open(
            MemoryStore.MEMORY_FILE,
            "w"
        ) as file:

            json.dump(memory, file, indent=4)

    @staticmethod
    def load_memory():

        MemoryStore.initialize_memory()

        with open(
            MemoryStore.MEMORY_FILE,
            "r"
        ) as file:

            return json.load(file)