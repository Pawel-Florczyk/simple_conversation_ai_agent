import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

os.environ["GOOGLE_API_KEY"] = "PASTE YOUR API KEY"

def run_simple_agent():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not set.")
        return

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.5
        )

        history = []

        print("Simple agent powered by Google Gemini has already started.")
        system_instruction = SystemMessage(
            content="You are simple AI assistant. "
                    "Your name is Simple Agent. "
                    "You have to answer in English or Polish,"
                    "and remember the context of conversation."
        )

        while True:
            user_text = input("Ask Agent something: ")

            if user_text.lower() in ["bye", "czesc", "do widzenia"]:
                print("Agent: Bye!")
                break

            if not user_text.strip():
                continue

            history.append(HumanMessage(content=user_text))

            response = llm.invoke([
                system_instruction,
                HumanMessage(content=user_text)
            ])

            history.append(AIMessage(content=response.content))

            print(f"\nAgent: {response.content}\n")

    except Exception as e:
        print(f"Unexpected error: {e}")
        print("Make sure that your API is correct "
              "and you have connection with internet.")

if __name__ == "__main__":
    run_simple_agent()
