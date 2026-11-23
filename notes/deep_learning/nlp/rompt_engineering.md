1. What is prompt engineering?
   its the user ask, message that describes user's questions or ask. its about giving clear instrucions, explaining the right context so the model can understand and give better reposes

2. What is zero-shot prompting?
   giving the insttruction with no examples

3. What is few-shot prompting?
   giving the insttruction with few examples

4. Does few-shot prompting train the model?
   no it dnt train the model. examples are provided in the context of particular request.

5. Difference between system and user messages.
   user message - is user ask, their request
   system msg- overall behaviour of the assisance or model

6. What is temperature?
   temp constrols how much variation is introduced in selecting the next token.
   lower temp - more predictable output
   highter temp - produces more varied output

7. What is structured prompting?
   gving the clear instruction about the task, context and expected reponse to the model.

8. Why are reusable prompt templates useful?
   because it saves time, avoids re work and can be used at anytime.

# interview

1. What is prompt engineering?
   Hide model answerMODEL ANSWER
   Prompt engineering is the practice of designing instructions and providing relevant context to an LLM to improve the usefulness, relevance and format of its responses.

2. What is the difference between zero-shot and few-shot prompting?
   Hide model answerMODEL ANSWER
   Zero-shot prompting asks the model to perform a task without examples. Few-shot prompting includes a small number of examples to demonstrate the expected task or output pattern.

3. Does few-shot prompting fine-tune the LLM?
   Hide model answerMODEL ANSWER
   No. Few-shot prompting provides examples in the input context. It does not update the model's learned weights.

4. What is the purpose of a system message?
   Hide model answerMODEL ANSWER
   A system message provides high-level instructions about the assistant's behavior, role and constraints. The user message contains the user's actual request.

5. How does temperature affect LLM responses?
   Hide model answerMODEL ANSWER
   Temperature affects the probability distribution used during token selection. Lower values generally produce more predictable outputs, while higher values allow more variation.

6. Why should we use structured prompts?
   Hide model answerMODEL ANSWER
   Structured prompts clearly define the role, task, context, constraints and expected output. This makes instructions easier to understand and responses easier to use in applications.

7. Can prompt engineering completely prevent hallucinations?
   Hide model answerMODEL ANSWER
   No. Clear instructions and relevant context can reduce some errors, but they cannot guarantee factual correctness. Applications need grounding, validation and evaluation as well.
