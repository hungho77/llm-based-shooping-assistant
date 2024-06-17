
# LLM based Shopping Assistant Application

## 1. Introduction
The increasing complexity and variety in online shopping have made it challenging for users to find what they need efficiently. To address this problem, we developed a conversational shopping assistant leveraging Large Language Models (LLM) and Retrieval-Augmented Generation (RAG) techniques. Our solution aims to simplify the online shopping experience by providing accurate and personalized product recommendations through natural, conversational interactions.

## 2. Project's Goal
The primary goal of this project is to create a shopping assistant chatbot that enhances user experience on e-commerce platforms by:
- Providing personalized product recommendations.
- Offering detailed product specifications upon request.
- Informing users about warranty policies.
- Assisting users in placing orders.
- Escalating complex queries to human assistants.

## 3. Methods and Techniques Used
Data Collection
Using Web crawling technique to get product information from CellphoneS as dataset for RAGs system
- website: https://cellphones.com.vn/thiet-bi-am-thanh/tai-nghe/tai-nghe-bluetooth.html?order=filter_price&dir=desc
- Descriptions: 

`PRODUCT_ID`: mã sản phẩm

`PRODUCT_NAME`: tên sản phẩm

`PRICE_REMAINING`: giá tiền còn lại (giảm giá)

`PRICE_INITIAL`: giá tiền ban đầu (nếu không có giảm giá thì giá trị là 0)

`PRICE_PERCENTAGE_REDUCE`: giảm bao nhiêu phần trăm

`PRODUCT_INFOMATION_DETAIL`: mô tả sản phẩm chi tiết

`PRODUCT_IMAGE`: link hình ảnh sản phẩm

`PRODUCT_LINK`: link sản phẩm 

`Review`: feedback sản phẩm

Technology and Techniques
- Core Technology: Google Gemini API that support Vietnamese.
- RAG Technique: To facilitate knowledge retrieval from a vast database of product information from crawled data.
- Additional NLP Techniques e.g ReAct prompting technique to help the model classify user input to pre-defined functionalities.

## 4. Results and Analysis
The development of the LLM-based shopping assistant was successful, achieving the following:
- Product Recommendations: The assistant effectively provided tailored product suggestions based on user preferences.
- Product Specifications: Users received detailed and accurate product information upon request.
- Policy Information: The assistant efficiently informed users about return and refund policies.
- Order Placement: Users were guided through the order placement process smoothly.
- Query Escalation: Complex queries were successfully classified and ready to be escalated to human assistants.

The RAG technique significantly enhanced the assistant's ability to retrieve relevant and accurate information from the product database. The integration of NLP techniques ensured that the assistant could understand and respond to user queries naturally and effectively.

## 5. Discussion and Conclusion
The project demonstrated the potential of combining LLM and RAG techniques to create a sophisticated and user-friendly shopping assistant. The assistant's performance in providing personalized recommendations and detailed product information contributed to a more streamlined and enjoyable shopping experience for users.

The LLM-based shopping assistant successfully addressed the challenges of overwhelming choices in online shopping. By leveraging advanced technologies, we created a tool that enhances user satisfaction and efficiency in navigating e-commerce platforms.

## 6. Difficulties and Future Development Directions
Difficulties
- User Queries Classification: Relying entirely on the model to classify user input posed challenges. The model occasionally struggled to accurately determine the user's intent, especially with ambiguous or complex queries.
- Exact Product Information Retrieval: Extracting precise product details using LLMs proved difficult. The multiple product attributes make it difficult for LLM to look for specific recommendations.
- Performance Issues: The need for the chatbot to classify user queries into predefined tasks caused performance bottlenecks. The additional processing required for classification led to slower response times.

Future Development Directions
- Integration with Traditional Databases: To enhance the accuracy of product information retrieval, integrating traditional databases with the LLM-based system will be beneficial. This hybrid approach can leverage the structured nature of databases to provide exact product details while using the LLM for more conversational and flexible interactions.
- Improved Query Classification Techniques: Developing more robust query classification mechanisms, possibly incorporating rule-based systems alongside the LLM, can help mitigate misclassification issues. 
- By addressing these future development directions, the shopping assistant can continue to evolve and provide even greater value to users in the e-commerce ecosystem.