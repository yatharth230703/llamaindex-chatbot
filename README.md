# LlamaIndex Chatbot

This is a simple chatbot application built using LlamaIndex and Streamlit. The chatbot utilizes the OpenAI GPT model for generating responses. The application allows users to interact with the chatbot through a web interface.

## Requirements

Make sure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository or download the script:**

    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install the required Python libraries:**

    ```sh
    pip install streamlit llama-index openai
    ```

3. **Set up your OpenAI API key:**

    You need an OpenAI API key to use the GPT model. Set your API key in the environment variable `OPENAI_API_KEY`. Replace `your_openai_api_key` with your actual API key.

    ```sh
    export OPENAI_API_KEY="your_openai_api_key"
    ```

## Configuration

Update the `input_dir` in the `app.py` script to point to the directory containing your data. For example:

```python
data = SimpleDirectoryReader(input_dir="C:/Users/yatharth/Desktop/desktop1/AI/ComputerHub/CORPUS").load_data()
