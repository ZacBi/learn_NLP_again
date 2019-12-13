"""
Count n-grams in chapter 3.
"""

from collections import defaultdict
from typing import Iterable


class NGram:
    def __init__(self):
        self.punctuations = []

    def unigram(self, corpus: Iterable):
        """Count unigram.
        Corpus should be pre-processed with one setence a line ,
        and each line should be end with punctuation.
        """
        unigram_count = defaultdict(int)  # pylint: disable=unused-variable
