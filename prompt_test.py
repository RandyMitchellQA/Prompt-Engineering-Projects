import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

# Test prompt
prompt = "Write a blog post about AI's impact on healthcare."

# Send the prompt to GPT-3
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=150
)

# Print the result
print(response.choices[0].text)
