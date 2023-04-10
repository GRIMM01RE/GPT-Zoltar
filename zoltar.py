import openai
import os

# Function to request API key from the user and save it to an environment variable
def request_and_save_api_key():
    api_key = input("Please enter your OpenAI API key: ").strip()
    os.environ["OPENAI_API_KEY"] = api_key
    return api_key

# Function to load API key from environment variable or request it from the user
def load_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("API key not found in environment variables.")
        api_key = request_and_save_api_key()
    return api_key

# Function to generate a fortune or greeting using GPT API
def generate_text(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating text: {e}")
        return "An unknown error occurred."

# Main script
try:
    openai.api_key = load_api_key()
    greeting_prompt = "The Great Haunted Zoltar greets the user with a random, eerie statement:"
    greeting = generate_text(greeting_prompt)
    print(greeting)
    print("Do you dare to uncover the secrets of your fortune? (y/n)")

    answer = input().lower()

    if answer == "y":
        fortune_prompt = "The Great Haunted Zoltar reveals the user's eerie and mystic fortune:"
        fortune = generate_text(fortune_prompt)
        print(f"\nThe shadows whisper... Your fortune: {fortune}\n")
    else:
        print("\nVery well... The Great Haunted Zoltar fades back into the darkness...\n")

except Exception as e:
    print(f"An error occurred: {e}")
