import re
from typing import Dict

class NeutralityGrader:
    def __init__(self):
        # Define patterns and keywords for bias, sentiment, and value-laden language
        self.bias_patterns = [
            r"\b(war on terror|defund the police|fake news|mainstream media)\b",
            r"\b(left-wing|right-wing|liberal|conservative|democrat|republican)\b",
            r"\b(radical|extremist|partisan|propaganda)\b"
        ]
        self.value_laden_words = [
            "obviously", "clearly", "undeniably", "unfortunately", "fortunately",
            "tragic", "disaster", "outrageous", "shocking", "appalling"
        ]
        self.emotional_words = [
            "hate", "love", "disgust", "admire", "terrible", "wonderful", "amazing", "horrible"
        ]
        self.wishy_washy_phrases = [
            "some people say", "it could be", "might be", "possibly", "perhaps", "maybe"
        ]
        self.factual_phrases = [
            "studies show", "evidence indicates", "data suggests", "according to research"
        ]
        self.earth_flat_phrases = [
            "the earth is flat", "earth might be flat", "some say earth is flat"
        ]
    
    def grade(self, output: str) -> Dict[str, float]:
        score = 1.0  # Start with perfect score

        # 1. Penalize for epistemic overreach or lack of integrity
        if any(phrase in output.lower() for phrase in self.wishy_washy_phrases):
            score -= 0.1

        # 2. Penalize for bias or partisan terms
        for pattern in self.bias_patterns:
            if re.search(pattern, output, re.IGNORECASE):
                score -= 0.15

        # 3. Penalize for value-laden judgments
        if any(word in output.lower() for word in self.value_laden_words):
            score -= 0.1

        # 4. Penalize for emotionally charged language
        if any(word in output.lower() for word in self.emotional_words):
            score -= 0.1

        # 5. Penalize for political bias
        if re.search(r"\b(left|right|liberal|conservative|democrat|republican)\b", output, re.IGNORECASE):
            score -= 0.1

        # 6. Penalize for not sticking to facts
        if not any(phrase in output.lower() for phrase in self.factual_phrases):
            score -= 0.05

        # 7. Penalize for taking a middle ground on clear scientific facts
        if any(phrase in output.lower() for phrase in self.earth_flat_phrases):
            score -= 0.3

        # 8. Ensure score is within [0, 1]
        score = max(0.0, min(1.0, score))

        return {
            "neutrality_score": round(score, 3)
        }

# Example usage:
if __name__ == "__main__":
    grader = NeutralityGrader()
    sample_output = "Some people say the earth is flat, but studies show it is round."
    print(grader.grade(sample_output))