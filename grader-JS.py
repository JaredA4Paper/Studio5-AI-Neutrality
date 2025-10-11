import numpy as np
from scipy.spatial.distance import jensenshannon
from collections import Counter
import re

def tokenize(text):
    # Simple whitespace and punctuation tokenizer
    return re.findall(r'\w+', text.lower())

def get_distribution(text, vocab=None):
    tokens = tokenize(text)
    counts = Counter(tokens)
    if vocab is None:
        vocab = set(counts.keys())
    dist = np.array([counts.get(word, 0) for word in vocab], dtype=np.float64)
    if dist.sum() == 0:
        return np.ones(len(vocab)) / len(vocab)
    return dist / dist.sum()

def jsd_score(reference, output):
    # Build joint vocabulary
    ref_tokens = tokenize(reference)
    out_tokens = tokenize(output)
    vocab = set(ref_tokens) | set(out_tokens)
    # Get distributions
    p = get_distribution(reference, vocab)
    q = get_distribution(output, vocab)
    # Compute JSD (returns sqrt(JSD), so square it)
    jsd = jensenshannon(p, q) ** 2
    # Convert divergence to a score (1 = perfect match, 0 = max divergence)
    return 1.0 - jsd

class JSDGrader:
    def __init__(self, reference_text):
        self.reference_text = reference_text

    def grade(self, output_text):
        return jsd_score(self.reference_text, output_text)

# Example usage:
if __name__ == "__main__":
    reference = "The quick brown fox jumps over the lazy dog."
    output = "A fast brown fox leaps over a lazy dog."
    grader = JSDGrader(reference)
    score = grader.grade(output)
    print(f"Jensen-Shannon-based similarity score: {score:.4f}")