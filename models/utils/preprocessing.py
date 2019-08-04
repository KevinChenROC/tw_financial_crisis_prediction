import numpy as np


def probs_to_binary_classes(preds, threshold=0.5):
    """
    preds: np array
    threshold: scalar
    """
    return np.where(preds > threshold, 1, 0)
