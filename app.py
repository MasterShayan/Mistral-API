from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

def chat_completions(query, api_key):
    """
    Sends a request to the AIML API chat completions endpoint and returns the response.

    Args:
        query (str): The user query.
        api_key (str): Your AIML API key.

    Returns:
        str: JSON formatted response from the API or an error message.
    """
    url = 'https://api.aimlapi.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'mistralai/Mistral-7B-Instruct-v0.2',
        'messages': [{'role': 'user', 'content': query}],
        'temperature': 0.7,
        'max_tokens': 256
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json() # Returns JSON directly

    except requests.exceptions.RequestException as e:
        return {'error': str(e)} # Returns error as dictionary
    except json.JSONDecodeError as e:
        return {'error': 'Response is not valid JSON', 'response_text': response.text} # Returns error as dictionary


@app.route('/chat', methods=['GET'])
def chat_api():
    """
    API endpoint for chat completions.
    Receives a query via GET request and returns a JSON response from the AIML API.
    """
    query = request.args.get('q')
    api_key = "YOUR_API_KEY_HERE" # Replace with your actual API key

    if not api_key: # Removed placeholder check as API key is now provided
        return jsonify({"error": "API key is missing."}), 400 # Bad Request
    if not query:
        return jsonify({"error": "Parameter 'q' is missing. Please provide a query parameter 'q' in the URL."}), 400 # Bad Request

    response_data = chat_completions(query, api_key)
    response_data["created_by"] = "Master Shayan"
    return jsonify(response_data) # Returns JSON response using Flask jsonify


if __name__ == '__main__':
    app.run(debug=True) # Run the Flask app in debug mode
