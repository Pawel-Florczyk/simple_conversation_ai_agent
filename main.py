import os
import sqlite3
from datetime import datetime
from typing import List, Any
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, BaseMessage

load_dotenv()

os.environ["GOOGLE_API_KEY"] = "INSERT YOUR API KEY HERE"


class Agent:
    def __init__(self, model_name="gemini-2.5-flash", temperature=0.5):
        self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=temperature)
        self.system_instruction = SystemMessage(
            content="You have to give an answers on questions. "
                    "You can answer in Polish or English."
        )
        self.memory: List[BaseMessage] = [self.system_instruction]
        self.conn = sqlite3.connect("agent_db_memory.sqlite")
        self.cursor = self.conn.cursor()

    def save_to_db(self, role: str, content: str | list[Any]) -> None:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cursor.execute("INSERT INTO ai_agent_memory (role, content, timestamp) VALUES (?,?,?)", (role, content, timestamp))
        self.conn.commit()

    def ask(self, user_text: str) -> str | list[Any]:
        self.save_to_db("user", user_text)

        self.memory.append(HumanMessage(content=user_text))

        if len(self.memory) > 10:
            self.memory.pop(1)

        response = self.llm.invoke(self.memory)

        self.save_to_db("assistant", response.content)

        self.memory.append(AIMessage(content=response.content))
        return response.content


if __name__ == "__main__":
    agent = Agent()
    while True:
        txt = input("Ask Agent something: ")
        if txt.lower() in ["bye", "czesc", "do widzenia"]:
            break
        print(f"Agent: {agent.ask(txt)}")
