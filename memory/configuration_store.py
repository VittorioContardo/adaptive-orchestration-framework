import json
import os


class ConfigurationStore:

    CONFIG_FILE = (
        "storage/configurations.json"
    )

    @staticmethod
    def initialize():

        if not os.path.exists(
            ConfigurationStore.CONFIG_FILE
        ):

            with open(
                ConfigurationStore.CONFIG_FILE,
                "w"
            ) as file:

                json.dump([], file)

    @staticmethod
    def save_configuration(data: dict):

        ConfigurationStore.initialize()

        with open(
            ConfigurationStore.CONFIG_FILE,
            "r"
        ) as file:

            configs = json.load(file)

        configs.append(data)

        with open(
            ConfigurationStore.CONFIG_FILE,
            "w"
        ) as file:

            json.dump(configs, file, indent=4)

    @staticmethod
    def load_configurations():

        ConfigurationStore.initialize()

        with open(
            ConfigurationStore.CONFIG_FILE,
            "r"
        ) as file:

            return json.load(file)