class OllamaClient:
    def __init__(self, model_name):
        self.model_name = model_name

    def send_query(self, query):
        # Here you would implement the logic to send the query to the LLM
        # For example, using a local API call or direct interaction with the model
        response = self._mock_response(query)  # Replace with actual API call
        return response

    def _mock_response(self, query):
        # This is a mock response for demonstration purposes
        return f"Response to: {query}"