# Mistral API 🚀

[![License: CC BY-NC-ND 4.0](about:sanitized)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

Welcome to the Mistral API repository\! This project provides a simple and efficient API built with Flask in Python, allowing you to interact with the powerful Mistral-7B-Instruct-v0.2 model from AIML API.

This API is designed to be easy to use and deploy, making it perfect for developers looking to integrate a cutting-edge language model into their applications.

## ✨ Features

  * **Effortless Integration:**  Quickly integrate the Mistral-7B-Instruct-v0.2 model into your projects.
  * **Flask-Powered:** Built with Flask, a lightweight and flexible Python web framework.
  * **JSON Output:**  Provides clean and structured JSON responses, ideal for API consumption.
  * **Error Handling:**  Includes robust error handling to manage API request issues gracefully.
  * **Customizable Parameters:**  Easily adjustable temperature and max\_tokens for response generation.
  * **Attribution:**  Clearly marked with "Created by Master Shayan" in the JSON output.

## 🛠️ Getting Started

Follow these simple steps to get your own instance of the Mistral API up and running.

### Prerequisites

Make sure you have Python and pip installed on your system. You will also need an API key from [https://api.aimlapi.com](https://api.aimlapi.com).

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/MasterShayan/Mistral-API.git
    cd Mistral-API
    ```

2.  **Install dependencies:**

    ```bash
    pip install flask requests
    ```

3.  **Set your API Key:**

    Open the `app.py` file and replace the placeholder API key with your actual API key from [https://api.aimlapi.com](https://api.aimlapi.com) in this line:

    ```python
    api_key = "YOUR_API_KEY_HERE" # Replace with your actual API key
    ```

    **Important:**  For security in production environments, consider using environment variables to manage your API key instead of hardcoding it directly in the script.

4.  **Run the Flask application:**

    ```bash
    python app.py
    ```

    The API will be accessible at `http://127.0.0.1:5000/` or `http://localhost:5000/`.

### Usage

Send a GET request to the `/chat` endpoint with your query as a parameter `q`.

**Example Request:**

```
http://127.0.0.1:5000/chat?q=Hello, how are you today?
```

**Example JSON Response:**

```json
{
    "id": "...",
    "object": "chat.completion",
    "choices": [
        {
            "index": 0,
            "finish_reason": "eos",
            "logprobs": null,
            "message": {
                "role": "assistant",
                "content": " Hello there! I'm just here to help answer your questions and provide information. How can I assist you today?",
                "tool_calls": []
            }
        }
    ],
    "created": 1740499793,
    "model": "mistralai/Mistral-7B-Instruct-v0.2",
    "usage": {
        "prompt_tokens": 5,
        "completion_tokens": 11,
        "total_tokens": 16
    },
    "created_by": "Master Shayan"
}
```

## ✍️ Author

This API was created with ❤️ by **Master Shayan**.

## ⭐️ Show Your Support

If you find this project helpful or interesting, please consider giving it a ⭐️ star on GitHub\! It helps to show appreciation and supports the project's visibility.

[https://github.com/MasterShayan/Mistral-API](https://github.com/MasterShayan/Mistral-API)

## 📜 License

This project is licensed under the Attribution-NonCommercial-NoDerivatives 4.0 International License.

[![CC BY-NC-ND 4.0 License](about:sanitized)]([https://creativecommons.org/licenses/by-nc-nd/4.0/](https://www.google.com/url?sa=E&source=gmail&q=https://creativecommons.org/licenses/by-nc-nd/4.0/))

-----

Thank you for checking out the Mistral API\! If you have any questions or suggestions, feel free to open an issue or contribute. Happy coding\! 🚀

```
```
