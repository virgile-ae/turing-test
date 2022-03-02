# Contains functions which could be used when our robot doesn't have an answer
import openai

openai.api_key = "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"

def format_response(res):
    """Formats the response of the GPT-3 API."""
    if len(res) == 0:
        return res
    final = res
    while not final[0].isalnum():
        final = final[1:]
    punc = False
    for i in ".?!":
        if i in final:
            punc = True
    if not punc:
        return final
    while not final[-1] in ".?!":
        final = final[:-1]
    return final

def get_response_gpt3(prompt):
    """Gets the response from the GPT-3 API using the prompt."""
    response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, temperature=0.7, max_tokens=64, top_p=1, frequency_penalty=0, presence_penalty=0)
    return format_response(response["choices"][0]["text"].strip())