import os
from typing import List, Any
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, BaseMessage

load_dotenv()

os.environ["GOOGLE_API_KEY"] = "INSERT YOUR GOOGLE API KEY HERE"


class Agent:
    def __init__(self, model_name="gemini-2.5-flash", temperature=0.5):
        self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=temperature)
        self.system_instruction = SystemMessage(
            content="You have to give an answers on questions. You can answer in Polish or English.")
        self.memory: List[BaseMessage] = [self.system_instruction]

    def ask(self, user_text: str) -> str | list[Any]:
        self.memory.append(HumanMessage(content=user_text))
        response = self.llm.invoke(self.memory)
        self.memory.append(AIMessage(content=response.content))
        return response.content


if __name__ == "__main__":
    agent = Agent()
    while True:
        txt = input("Ask Agent something: ")
        if txt.lower() in ["bye", "czesc", "do widzenia"]:
            break
        print(f"Agent: {agent.ask(txt)}")
