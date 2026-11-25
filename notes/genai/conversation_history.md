1. What is conversation history?
   keep a hold of the users previouse msg or conversation is conversation history, it helps to understand the right context of the message or request

2. Why does an LLM need previous messages to understand follow-up questions?
   it helps in understanding the user;s message context, analyze and answer in a right way by avoiding repetition

3. What is the purpose of the system role?
   it definse overall behaviour or instruction of the assistant

4. What is the purpose of the assistant role?
   it hepls to maintain the user;s conversation history

5. Who maintains conversation history in our implementation?
   python application

6. Why do we append the assistant response to the messages list?
   so the model can analyse the past converation and perform accordiglty

7. What happens if we send only the latest user message?
   the model asked for a reference, clear instructions or to define the request in a better way

8. Why can sending too much conversation history become a problem?
   leads to performance, storage and more time in execution which can make model too slow

   # interview

   Does an LLM automatically remember previous API requests?
   Hide model answerMODEL ANSWER
   Not necessarily. In a typical stateless chat-completion request, the application must include relevant previous messages in the next request. Some APIs provide stateful conversation features, but that depends on the provider and endpoint.

9. What is the purpose of a system message?
   Hide model answerMODEL ANSWER
   A system message provides high-level instructions about the assistant's behavior, role and constraints.

10. Why do we send previous assistant messages along with user messages?
    Hide model answerMODEL ANSWER
    Previous assistant messages provide conversational context. They help the model understand what it has already answered and respond appropriately to follow-up questions.

11. Who maintains conversation history in our implementation?
    Hide model answerMODEL ANSWER
    Our Python application maintains it in the messages list and sends that history with each API request.

12. What happens if conversation history becomes too large?
    Hide model answerMODEL ANSWER
    The request may exceed the model's context window. Applications can manage this by trimming older messages, summarizing them or retrieving only relevant information.

13. What is the difference between a prompt and conversation history?
    Hide model answerMODEL ANSWER
    A prompt is the instruction or input given to the model. Conversation history is the sequence of previous user and assistant messages that provides context for the current request.
