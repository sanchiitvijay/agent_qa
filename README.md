# Question-Answering Agent with LangGraph and OpenAI

This project implements a simple Question-Answering agent using LangGraph and OpenAI's language models.

## Features

- 🤖 Interactive Q&A agent powered by OpenAI (GPT-4 or GPT-3.5)
- 🔄 Conversation history tracking using LangGraph StateGraph
- 💬 Simple command-line interface
- 🔧 Easy configuration via environment variables

## Project Structure

```
question_answer/
├── src/
│   └── qa_agent.py          # Main QA agent implementation
├── .env                     # Environment variables (API keys)
├── requirements.txt         # Python dependencies
├── context.txt             # Project requirements
└── README.md               # This file
```

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure OpenAI API Key:**
   - Edit the `.env` file
   - Replace `your-openai-api-key-here` with your actual OpenAI API key
   - You can get an API key from: https://platform.openai.com/api-keys

3. **Run the agent:**
   ```bash
   python src/qa_agent.py
   ```

## Usage

1. Start the program
2. Ask any question when prompted
3. The agent will respond using OpenAI's language model
4. Continue the conversation - the agent remembers previous messages
5. Type `exit` to quit

## Example Interaction

```
🤖 Welcome to the Question-Answering Agent!
💡 Ask me anything, or type 'exit' to quit.

You: What is the capital of France?

🤖 Assistant: The capital of France is Paris.

You: How many people live there?

🤖 Assistant: Paris has a population of approximately 2.1 million people within the city proper, and about 12 million people in the greater Paris metropolitan area (Île-de-France region).

You: exit

👋 Goodbye! Thanks for using the QA Agent.
```

## How It Works

1. **Agent State**: Uses `TypedDict` to define state containing conversation messages
2. **LangGraph**: Creates a `StateGraph` with START → process_message → END flow
3. **OpenAI Integration**: Uses `ChatOpenAI` from `langchain_openai` for LLM responses
4. **Message History**: Maintains conversation context across interactions

## Configuration

- **Model**: Change `model="gpt-4"` to `model="gpt-3.5-turbo"` in `qa_agent.py` for a cheaper option
- **Temperature**: Adjust the `temperature` parameter to control response creativity (0.0 = deterministic, 1.0 = creative)

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection
# agent_qa
# agent_qa
