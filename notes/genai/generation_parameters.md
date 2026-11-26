1. What is temperature?
   it controls the randomness or variation on the reponse

2. What happens at low versus high temperature?
   low- lower randomness, more focused and predictable reponse
   high- more randomness so more variations

3. What is max_completion_tokens?
   it limits the lenght of the guranteed reponse.

4. Does increasing the token limit guarantee a longer response?
   not exactly

5. What is the difference between prompt instructions and generation parameters?
   prompt instrcutions - giving a clear instruction about our question or ask to the model,well constrcuted, adding examples prompts can generate the better reponse.
   generation parameters - its about handling the controlling or managing the reponse that mmodel generates.

# interview

. What does temperature control in an LLM?
MODEL ANSWER
Temperature controls randomness during token selection. Lower values generally produce more focused and predictable responses, while higher values produce more varied responses.

2. Does temperature 0 guarantee identical responses every time?
   MODEL ANSWER
   No. It reduces randomness, but identical outputs are not guaranteed across requests or model changes.

3. What is max_completion_tokens?
   MODEL ANSWER
   It specifies the maximum number of tokens the model can generate in a completion. The model may generate fewer tokens.

4. Can we control response length using only prompt instructions?
   MODEL ANSWER
   We can ask the model to be concise or detailed through a prompt, but max_completion_tokens provides an API-level upper limit.
