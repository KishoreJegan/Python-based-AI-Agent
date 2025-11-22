import math
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv

# Load environment variables (GROQ_API_KEY)
load_dotenv()


@tool
def calculator(expression: str) -> str:
    """
    Calculates the result of a mathematical expression.
    Examples: "2 + 2", "3 * 5", "sqrt(16)", "sin(90)".
    """
    try:
        # We create a safe dictionary of allowed math functions
        allowed_names = {
            k: v for k, v in math.__dict__.items() if not k.startswith("__")
        }

        # Evaluate the string (e.g., "2 + 2") safely
        # We strictly limit what code can run to just math functions
        result = eval(expression, {"__builtins__": {}}, allowed_names)

        return str(result)
    except Exception as e:
        return f"Error calculating: {str(e)}"


def main():
    model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

    search_tool = DuckDuckGoSearchRun()
    tools = [search_tool, calculator]

    memory = MemorySaver()

    # Create the agent
    agent_executer = create_react_agent(model, tools, checkpointer=memory)
    print("Welcome to the AI Agent! (I can search the web).")
    print("Type 'quit' to exit.")
    config = {"configurable": {"thread_id": "1"}}
    while True:
        user_input = input("\nYou :").strip()

        if user_input.lower() in ["quit", "exit"]:
            break

        print("\nAssistant :", end="")

        try:
            # Stream the response
            for chunk in agent_executer.stream(
                {"messages": [HumanMessage(content=user_input)]}, config=config
            ):
                # We filter for the "agent" node to get the final text response
                if "agent" in chunk and "messages" in chunk["agent"]:
                    for message in chunk["agent"]["messages"]:
                        print(message.content, end="")
            print()

        except Exception as e:
            print(f"\n[Error]: {e}")


if __name__ == "__main__":
    main()
    
