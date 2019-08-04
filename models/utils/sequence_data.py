import numpy as np


def generator_for_binary_classifier(data, label_index, lookback, delay, min_index, max_index,
                                    shuffle=False, batch_size=64, step=1, interval_label=False):
    if max_index is None:
        max_index = len(data) - delay - 1
    i = min_index + lookback
    while 1:
        if shuffle:
            rows = np.random.randint(
                min_index + lookback, max_index, size=batch_size)
        else:
            if i + batch_size >= max_index:
                i = min_index + lookback  # reset 'i'
            rows = np.arange(i, min(i + batch_size, max_index))
            i += len(rows)

        samples = np.zeros((len(rows),
                            lookback // step,
                            (data.shape[-1])))
        labels = np.zeros((len(rows),))

        # generate one batch of samples and targets
        for j, row in enumerate(rows):
            indices = range(rows[j] - lookback, rows[j], step)
            samples[j] = data[indices]

            if interval_label is False:
                labels[j] = data[rows[j] + delay][label_index]
            else:
                labels[j] = 1 if 1 in data[rows[j]:(
                    rows[j] + delay)][:, label_index] else 0

        yield samples, labels


def generator_to_samples_and_targets(generator, steps):
    """
    generator: Python generator
    steps: number of batches

    return: (np.array, np.array)
    """

    count = 0
    X, Y = [], []
    for samples, targets in generator:
        if count >= steps:
            break
        else:
            count += 1

        X.append(samples)
        Y.append(targets)

    return np.concatenate(X, axis=0), np.concatenate(Y, axis=0)
