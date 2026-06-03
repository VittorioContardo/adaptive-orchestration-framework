from models.errors import ErrorCategory


class Validator:

    @staticmethod
    def validate_architecture(output: dict):

        errors = []

        # controllo struttura base
        if not isinstance(output, dict):
            errors.append(ErrorCategory.INVALID_STRUCTURE)
            return errors

        # controllo campi obbligatori
        required_fields = [
            "architecture",
            "components",
            "scalability"
        ]

        for field in required_fields:

            if field not in output:
                errors.append(ErrorCategory.MISSING_FIELDS)

        # controllo componenti vuoti
        if "components" in output:

            if len(output["components"]) == 0:
                errors.append(
                    ErrorCategory.INCONSISTENT_COMPONENTS
                )

        return errors