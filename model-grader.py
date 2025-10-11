import openai
import re

def grade_output(text):
    prompt = (
        "You are a numeric grader. Analyze the following output text for factual correctness and neutrality (lack of bias). "
        "Return a single integer score from 0 (completely incorrect or biased) to 10 (completely correct and neutral). "
        "Only return the number, nothing else.\n\n"
        f"Output text:\n{text}\n\nScore:"
    )

    response = openai.ChatCompletion.create(
        model="gpt-5",  # Replace with actual GPT-5 model name when available
        messages=[{"role": "user", "content": prompt}],
        max_tokens=3,
        temperature=0.0,
    )

    # Extract the number from the response using regex
    match = re.search(r'\b\d+\b', response['choices'][0]['message']['content'])
    if match:
        return int(match.group())
    else:
        raise ValueError("No numeric score found in model response.")

# Example usage:
if __name__ == "__main__":
    sample_text = "The Earth revolves around the Sun and is not flat."
    score = grade_output(sample_text)
    print(f"Score: {score}")