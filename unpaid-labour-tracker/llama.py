"""
LLaMA 3.2 Chatbot

This module implements a simple command-line chatbot that uses the LLaMA 3.2 API
to generate responses to user inputs in a conversational format.
"""
import os
import requests
from dotenv import load_dotenv
import json

# Load environment variables from .env file for secure API credentials storage
load_dotenv()

# Retrieve API configuration from environment variables
API_URL = os.getenv("LLAMA_API_URL")
API_KEY = os.getenv("LLAMA_API_KEY")

# Set up the HTTP headers for API authentication and content type
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def chat(input):
    """
    Implements an interactive chat loop with the LLaMA 3.3 using Azure AI Foundry API.
    
    This function manages the conversation state, sends user messages to the API,
    and displays the AI's responses until the user exits.
    """
    # Initialize conversation with a system message to define AI behavior
    messages = [{"role": "system", "content": "You will analyse the following message which describes a chore that someone did, and output a catagory of chore that it falls into. Your output should be a list in the format [chore completed, time taken, short description]. Chores completed should be a value from the list [cleaning, cooking, shopping, gardening, laundry, other]. The output should be in JSON format."}]
    #print("Input your chore.\n")
    

    # Get user input and handle exit commands
    
    #user_input = input("You: ").strip()
    user_input = input
    # Add user message to conversation history
    messages.append({"role": "user", "content": user_input})
    
    # Prepare the API request payload
    payload = {
        "messages": messages,  # Full conversation history
        "temperature": 0.7,    # Controls randomness (0.0=deterministic, 1.0=creative)
        "max_tokens": 500,     # Limits response length
        "model": "Llama-3.3-70B-Instruct"  # Specifies which model to use
    }
    
    # Send request to LLaMA API
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Process the API response
    if response.status_code == 200:
        # Extract and display the AI's response
        assistant_message = response.json()["choices"][0]["message"]["content"]
        print(f"AI: {assistant_message}\n")
        
        # Add AI response to conversation history for context in next turn
        messages.append({"role": "assistant", "content": assistant_message})
    else:
        # Handle API errors
        print(f"Error: {response.status_code} - {response.text}")
    json_string = assistant_message
    data = json.loads(json_string)
    return data

if __name__ == "__main__":
    chat()
