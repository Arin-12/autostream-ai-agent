from agent import AutoStreamAgent
from rag import build_index

def run_agent():
    agent = AutoStreamAgent()

    print("🤖 AutoStream AI Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye! 👋")
            break

        response = agent.handle_input(user_input)
        print(f"Agent: {response}")

if __name__ == "__main__":
    build_index()   # IMPORTANT
    run_agent()