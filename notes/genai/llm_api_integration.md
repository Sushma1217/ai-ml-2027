1. What is an API?
   it stand for Application Programming Interface, a set of rules or protocols that allows two different application to communation like front end to backend, acts as bridge between.

2. How does Python communicate with an LLM?
   via http apis

3. What is an API key?
   an authentication code for api to prevent unauthorised usages.

4. Why should API keys be stored in environment variables?
   To keep sensitive credentials separate from source code and reduce the risk of accidentally exposing them in GitHub or other shared locations.

5. What is the difference between request and response?
   request - the instrcution or ask what we send
   reponse- answer to our request

6. What are common API errors?
   500- server side
   401- unauthrozed
   400- invalid request
   429 means the request exceeded the allowed rate limit or quot

7. Why do we create a reusable generate_response() function?
   when we create the reusable function it works for any promots, we dnt need to rewrite for each request which makes code optimized and avoids repetition

   # Interview practice
   1. What is an LLM API?
      Hide model answerMODEL ANSWER
      An LLM API provides an interface for an application to communicate with a language model. The application sends input, and the API returns the model's generated output.

8. What is the purpose of an API key?
   Hide model answerMODEL ANSWER
   An API key authenticates the application with the API provider and helps identify the project or account for access control and usage tracking.

9. What is the difference between an API request and response?
   Hide model answerMODEL ANSWER
   A request is the information sent by the client, such as the model name and prompt. A response is the information returned by the API, including generated content and potentially metadata or usage information.

10. Why should we not hardcode API keys?
    Hide model answerMODEL ANSWER
    Hardcoded keys can accidentally be exposed through source code, GitHub or logs. Environment variables or secret managers help keep credentials separate from application code.

11. Why do we create a reusable function to call an LLM?
    Hide model answerMODEL ANSWER
    It avoids duplicating API logic, makes the application easier to maintain and allows different parts of the application to call the same model integration.

12. What does HTTP 429 usually indicate?
    Hide model answerMODEL ANSWER
    HTTP 429 indicates that the request has exceeded a rate limit or quota. The application may need to wait, reduce request frequency or review its API limits.
