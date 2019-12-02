import re
from collections import defaultdict
from typing import Dict


def get_stats(vocab: Dict):
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = list(word)
        for i in range(len(symbols) - 1):
            pairs[symbols[i], symbols[i + 1]] += freq
    return pairs


def byte_pair_encoding(
        vocab: Dict[str, int],
        merge_iteration: int = 5,
):
    """Chapter 2.4.3
    BPE: Byte-Pair Encoding.

    BPE learns tokenization from training data and use learned method
    to tokenize training data.

    Args:
        merge_iteration: the number of iteration you want bpe to learn
            tokenization, defualt 5(int)

    Returns:
        vocab: final vocab with `merge_iteration` most frequent

    """
    vocab = vocab
    best_bigrams = []
    for iters in range(merge_iteration):
        # pairs is the collectiotn of two-symbol pair
        # e.g. (w, e_) or (e, ew_)
        pairs = defaultdict(int)
        for word, freq in vocab.items():
            symbols = word.split()
            for i in range(len(symbols) - 1):
                pairs[symbols[i], symbols[i + 1]] += freq

        # Use most frequent pair to substitue original two-symbols,
        # e.g. use 'new_' to replace ('n', 'ew_')
        most_frequent_pair = max(pairs, key=pairs.get)
        best_bigrams.append(''.join(most_frequent_pair))
        bigram = re.escape(' '.join(most_frequent_pair))
        pattern = re.compile(r'(?!<\S)' + bigram + r'(?!\S)')
        vocab_out = {}
        for word in vocab:
            # Create new symbol
            word_out = pattern.sub(''.join(most_frequent_pair), word)
            vocab_out[word_out] = vocab[word]
        vocab = vocab_out
    return vocab, best_bigrams
