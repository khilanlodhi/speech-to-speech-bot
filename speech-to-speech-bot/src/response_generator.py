from transformers import pipeline
from src.utils import log_error


generator = pipeline(
    "text-generation",
    model="gpt2",
    max_length=50,  
    top_p=0.9,      
    temperature=0.7 
)

def generate_response(prompt):
    try:
        
        predefined_responses = {
            "hello": "Hi there! How can I assist you?",
            "hi": "Hello! How are you today?",
            "thanks": "You're welcome!",
            "bye": "Goodbye! Have a nice day!"
        }

        prompt_lower = prompt.strip().lower()
        if prompt_lower in predefined_responses:
            return predefined_responses[prompt_lower]

      
        response = generator(prompt, max_length=40, num_return_sequences=1)
        return response[0]["generated_text"].strip()
    except Exception as e:
        log_error(f"Error generating response: {e}")
        return "I'm sorry, I couldn't process your request."
