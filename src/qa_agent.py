"""
Question-Answering Agent using LangGraph and OpenAI

This program creates a simple QA agent that:
1. Takes user input
2. Processes it through OpenAI's language model
3. Returns the model's response
4. Continues in a loop until user types "exit"
"""

import os
from typing import TypedDict, List
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langgraph.graph import StateGraph, START, END

load_dotenv()


class AgentState(TypedDict):
    messages: List[BaseMessage]


def create_qa_agent() -> StateGraph:
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.7,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    
    def process_message(state: AgentState) -> AgentState:
        messages = state["messages"]
        response = llm.invoke(messages)        
        updated_messages = messages + [response]

        return {"messages": updated_messages}
    
    workflow = StateGraph(AgentState)
    
    workflow.add_node("process_message", process_message)
    workflow.add_edge(START, "process_message")
    workflow.add_edge("process_message", END)
    
    app = workflow.compile()
    
    return app


def main():
    
    print("Welcome to the Question-Answering Agent!")
    print("Ask me anything, or type 'exit' to quit.\n")
    
    qa_agent = create_qa_agent()
    
    conversation_history = []
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("\n👋 Goodbye! Thanks for using the QA Agent.")
            break
        
        if not user_input:
            continue
        
        conversation_history.append(HumanMessage(content=user_input))
        
        initial_state = {"messages": conversation_history}
        
        try:
            result = qa_agent.invoke(initial_state)
            latest_message = result["messages"][-1]
            conversation_history = result["messages"]
            print(f"\nAssistant: {latest_message.content}\n")
            
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please check your OpenAI API key and try again.\n")


if __name__ == "__main__":
    main()
