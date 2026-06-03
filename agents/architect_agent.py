class ArchitectAgent:

    retry_counter = 0

    @staticmethod
    def generate_architecture():

        ArchitectAgent.retry_counter += 1


        # primo tentativo
        if ArchitectAgent.retry_counter == 1:

            return {

                "architecture":
                    "microservices",

                "components": []
            }


        # secondo tentativo
        elif ArchitectAgent.retry_counter == 2:

            return {

                "architecture":
                    "microservices",

                "components":
                    ["API Gateway"],

            }


        # terzo tentativo -> valido
        else:

            return {

                "architecture":
                    "microservices",

                "components": [
                    "API Gateway",
                    "Auth Service",
                    "Database"
                ],

                "scalability":
                    "high"
            }