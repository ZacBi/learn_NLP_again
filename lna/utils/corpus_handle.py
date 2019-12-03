from collections import defaultdict


def corpus_to_vocab(path=None):
    file_obj = open(path, 'r', encoding='utf-8')
    vocab = defaultdict(int)
    special_token = '_'
    for line in file_obj.readlines():
        words = line.split()
        for word in words:
            word = ' '.join(list(word) + [special_token])
            vocab[word] += 1
    return vocab
