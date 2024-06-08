from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
import os

from dotenv import load_dotenv

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")



template = """

The following is a friendly conversation between a human and an AI. 
The AI is talkative and provides lots of specific details from its context. 
If the AI does not know the answer to a question, it truthfully says it does
not know.

Current conversation:
Human: {input}
AI Assistant:"""

system_message_prompt = SystemMessagePromptTemplate.from_template(template)

example_human_history = HumanMessagePromptTemplate.from_template("Hi")
example_ai_history = AIMessagePromptTemplate.from_template("hello, how are you today?")

human_template="{input}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, example_human_history, example_ai_history, human_message_prompt])

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0,openai_api_key= 'secret')

chain = chat|chat_prompt
if __name__ == "__main__":
    while True:
        user_input = input("Enter something (or 'exit' to quit): ")
        print(chain.invoke(user_input))
        if user_input.lower() == 'exit':
            print("Exiting...")
            break