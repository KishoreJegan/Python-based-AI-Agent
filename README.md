<h1>Python-BasedAI-Agent</h1>
<h2>🧠 Smart AI Agent (with Memory & Tools)</h2>
Unlike a standard LLM that only knows what it was trained on, this agent has access to "tools" (Web Search and a Calculator) and possesses "memory" to remember your conversation history. It runs locally in your terminal but uses the powerful Llama 3.3 70B model via the Groq Cloud.

<h2>⚡ Why uv instead of pip?</h2>
You will notice I used uv for this project. If you haven't used it before: uv is a modern, extremely fast Python package manager (written in Rust).

It's Fast: It installs packages almost instantly compared to standard pip.

It's Clean: It handles virtual environments automatically.

It's Simple: No more python -m venv ... or pip freeze.

<h2>Install the uv</h2>

Windows (Recommended)
Open PowerShell and run:

PowerShell

powershell -ExecutionPolicy ByPass -c
```
"irm https://astral.sh/uv/install.ps1 | iex"
```

<h2>🛠️ Tech Stack & Libraries Used</h2>
Here is what makes this agent tick:

<h3>Python 3.12+:</h3> The core language.

<h3>LangGraph:</h3> The "brain" logic. It allows the AI to decide: "Should I answer directly, or do I need to use a tool first?"

<h3>LangChain:</h3> The framework that connects the AI to the tools.

<h3>Groq API (Llama 3.3 70B):</h3> The intelligence engine. We use the 70B model because it is significantly better at following tool instructions than smaller models.

<h3>DuckDuckGo Search:</h3> The "Eyes." Lets the agent search the live internet for real-time info (like stock prices or news).

<h3>Custom Calculator:</h3> The "Brain Extension." A specific Python tool I wrote because LLMs are notoriously bad at math. It uses Python's math library for precision.

<h3>MemorySaver:</h3> The RAM. Keeps track of the conversation so you don't have to repeat yourself.

<h2>🚀 How to Run This Project</h2>
<h3>1. Clone the Repository</h3>

```Bash

git clone <your-repo-url-here>
```
```
cd <your-repo-name>
```
<h3>2. Install Dependencies (Using uv)</h3>
If you don't have uv installed, get it first: pip install uv (ironic, I know) or via their official guide.

Then, simply run:

```Bash

uv sync
```
This will read the pyproject.toml (or you can manually add the packages below):

```Bash

uv add langchain-groq langgraph langchain-community duckduckgo-search python-dotenv
```
<h3>3. Set Up Your API Key</h3>
This project requires a Groq API Key (it's free to get).

Create a file named .env in the root folder.

Add your key inside it:

```Plaintext

GROQ_API_KEY="gsk_your_key_here..."
```
<h3>4. Run the Agent</h3>
Since uv manages the virtual environment for you, just run:

```Bash

uv run main.py
```
<h2>🤖 What Can It Do?</h2>
Once the agent is running, you can try these commands:

Test Memory:

You: "Hi, my name is Alice."

Agent: "Hello Alice."

You: "What is my name?"

Agent: "Your name is Alice."

Test Web Search:

You: "Who won the Cricket World Cup in 2023?"

Agent: (Searches DuckDuckGo) "Australia won..."

Test Math:

You: "Calculate the square root of 144 * 5."

Agent: (Uses Calculator Tool) "The answer is 60."

<h2>📂 Code Structure</h2>
<h3>main.py:</h3> The heart of the project.

<h3>@tool decorator:</h3> Converts my Python math function into a format the AI understands.

<h3>thread_id:</h3> This acts like a "Session ID." If you change this ID in the code, the AI forgets the previous conversation.

<h3>ChatGroq:</h3> The connection to the Llama 3.3 model.
