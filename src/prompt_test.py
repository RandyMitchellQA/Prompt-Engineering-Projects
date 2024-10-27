import openai

# Set your OpenAI API key (replace with your actual key)
openai.api_key = 'your-api-key-here'

def generate_response(prompt):
    """
    This function sends a prompt to the OpenAI GPT-3 model and returns the response.
    """
    try:
        # Send the prompt to the GPT-3 model
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can change this to another engine (e.g., 'gpt-3.5-turbo') if available
            prompt=prompt,
            max_tokens=150,  # Limit the length of the response
            temperature=0.7  # Controls randomness: 0.0 = deterministic, 1.0 = maximum randomness
        )

        # Extract and return the text of the response
        return response.choices[0].text.strip()

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Define your prompt here
   
