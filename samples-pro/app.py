import openai  # Import OpenAI library

# Import the API key from an external file
from apikey import api_data

# Set your OpenAI API key
openai.api_key = api_data

# Function to generate a reply
def Reply(question):
    try:
        # Use the updated API method for chat completions
        completion = openai.ChatCompletion.create(
            model="gpt-4",  # Correct model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=200
        )
        # Extract and return the response content
        answer = completion["choices"][0]["message"]["content"]
        return answer
    except Exception as e:
        # Print any errors for debugging
        print(f"Error: {e}")
        return None

# Define the question
question = "In simple terms explain to me about Rolls-Royce."

# Get the answer using the Reply function
ans = Reply(question)

# Print the answer
if ans:
    print(ans)
