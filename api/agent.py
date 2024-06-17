from langchain.agents import AgentExecutor
from langchain.chains import LLMChain
from langchain.agents import AgentExecutor, create_react_agent
from model import langchain_llm, llamaindex_embed_model, llamaindex_llm
from langchain_core.prompts import PromptTemplate
from retrieval import Retrieval
from langchain.memory import ConversationSummaryBufferMemory, ConversationBufferWindowMemory

# Construct the JSON agent
from prompt import classify_prompt, react_prompt_template

classify_prompt = PromptTemplate.from_template(classify_prompt)
chain = LLMChain(llm=langchain_llm, prompt=classify_prompt)


def tool_get_RAG():
    """Returns the RAG"""
    from llama_index.core.tools import QueryEngineTool

    retrieval = Retrieval()
    documents = retrieval.load_documents(r"C:\Users\ADMIN\LLMs\LLM-based-Shopping_Assistant_Application\data\cellphone_v3.csv")
    index = retrieval.create_index(documents,llamaindex_embed_model)
    query_engine = retrieval.create_query_engine(index, llamaindex_llm)
    tool = QueryEngineTool.from_defaults(
        query_engine,
        name="VectorDB",
        description="This is the product search tool of the cellphones store",
    )
    # run tool as langchain structured tool
    lc_tool = tool.as_langchain_tool()
    return lc_tool


# def get_prompt_input(user_input: str):
#     # Construct the JSON agent
#     chain = LLMChain(llm=langchain_llm, prompt=classify_prompt)
#     return chain.invoke(
#         {
#             "question": f"{user_input}",
#             "context": """a. Đề xuất sản phẩm: Sử dụng lời nhắc này khi mục đích của người dùng là khám phá các sản phẩm mới hoặc tìm đề xuất dựa trên sở thích hoặc giao dịch mua trước đây của họ.
#          b. Truy xuất thông tin sản phẩm: Sử dụng lời nhắc này khi người dùng tìm kiếm thông tin chi tiết về một sản phẩm cụ thể, chẳng hạn như tính năng, thông số kỹ thuật hoặc đánh giá.
#          c. Câu hỏi thường gặp Trả lời: Sử dụng lời nhắc này khi truy vấn của người dùng phù hợp với các câu hỏi thường gặp hoặc giải quyết các vấn đề hỗ trợ kỹ thuật, chính sách của các sản phẩm.
#          d. Thanh toán: Tận dụng lời nhắc này để tạo điều kiện thuận lợi cho quá trình mua hàng, bao gồm xử lý thông tin thanh toán, xác nhận đơn hàng và chi tiết giao hàng.
#          e. Khác: Sử dụng lời nhắc này cho các truy vấn không phù hợp với các danh mục trước đó, chẳng hạn như cung cấp hỗ trợ chung, cung cấp hỗ trợ quản lý tài khoản hoặc xử lý phản hồi.""",
#         }
#     )


def handle_user_prompt(user_prompt):
    user_prompt = user_prompt.splitlines()
    return [
        line.split(": ", maxsplit=1)[1]
        for line in user_prompt
        if line.strip().startswith("Answer:") or line.strip().startswith("Explain:")
    ]


# def handle_conversation_turn(user_input: str):
#     while True:
#         user_prompt = get_prompt_input(user_input)
#         return_prompt = handle_user_prompt(user_prompt["text"])
#         if return_prompt is not None:
#             try:
#                 if (
#                     "Đề xuất sản phẩm" in return_prompt[0]
#                     or "Truy xuất thông tin sản phẩm" in return_prompt[0]
#                     or "Câu hỏi thường gặp Trả lời" in return_prompt[0]
#                     or "Thanh toán" in return_prompt[0]
#                     or "Khác" in return_prompt[0]
#                 ):
#                     if len(return_prompt) > 1:
#                         return return_prompt[-1]
#                     return return_prompt[0]
#             except:
#                 print("Error")


tools = [tool_get_RAG()]


def generate_agent():
    # user_prompt = handle_conversation_turn(input)
    # print(user_prompt)
    react_prompt = PromptTemplate.from_template(
        """
                Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

        Assistant is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

        Overall, Assistant is a powerful tool that can . 
        Based on the input, determine what you are a specialized AI for with the following options
            a. Product recommendations: Use this prompt when the user's intent is to discover new products or find recommendations based on their interests or past purchases.
            b. Retrieve product information: Use this prompt when users search for detailed information about a specific product, such as features, specifications, or reviews.
            c. FAQ Response: Use this prompt when the user's query matches frequently asked questions or addresses technical support or product policy issues.
            d. Payment: Take advantage of this prompt to facilitate the purchasing process, including handling payment information, order confirmations, and shipping details.
            e. Other: Use this prompt for queries that don't fit the previous categories, such as providing general support, providing account management support, or handling responses

        Previous conversation history:
        {chat_history}

        
        TOOLS:
        ------

        Assistant has access to the following tools:

        {tools}

        To use a tool, please use the following format:

        ```
        Thought: Do I need to use a tool? Yes
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ```

        When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

        ```
        Thought: Do I need to use a tool? No
        Final Answer: [your response here]
        ```
        
        Let's begin!

        New input: {input}
        {agent_scratchpad}
        """,
        # partial_variables={"user_prompt": user_prompt},
    )
    # react_prompt.format(user_prompt=user_prompt)

    # Construct the ReAct agent

    # Previous conversation history:
    #     {chat_history}
    agent = create_react_agent(langchain_llm, tools, react_prompt)

    # Create an agent executor by passing in the agent and tools
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        memory=ConversationBufferWindowMemory(
            k=5, memory_key="chat_history"
        ),
        handle_parsing_errors=True,
    )
    return agent_executor


def load_agent():
    agent = generate_agent()
    return agent


def handle_react_chat(agent, input):
    print(agent.memory.load_memory_variables({}))
    return agent.invoke({"input": input,"chat_history":agent.memory.load_memory_variables({})["chat_history"]})


if __name__ == "__main__":
    agent = load_agent()
    print(handle_react_chat(agent, "Giới thiệu cho tôi những mẫu tai nghe dưới 700k đáng xem"))
    print(handle_react_chat(agent, "Giới thiệu cho tôi những mẫu tai nghe dưới 1000k đáng xem"))
