from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI

llm = OpenAI(temperature=0,openai_api_key= 'secret_key')

# Here it is by default set to "AI"
conversation = ConversationChain(
    llm=llm, verbose=True, memory=ConversationBufferMemory()
)



if __name__ == "__main__":
    while True:
        user_input = input(" ")
        print(conversation.predict(input=user_input))
        if user_input.lower() == 'exit':
            print("Exiting...")
            break