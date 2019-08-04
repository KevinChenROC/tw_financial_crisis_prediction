from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score, accuracy_score, matthews_corrcoef


def print_report_for_binary_classfier(y_true, y_pred):
    """
    y_true: 1d array with 1 or 0 values
    y_pred: 1d array with 1 or 0 values

    """
    print('F1 score: %f' % f1_score(y_true, y_pred))
    print('precision score: %f' % precision_score(y_true, y_pred))
    print('recall score: %f' % recall_score(y_true, y_pred))
    print('accuracy score: %f' % accuracy_score(y_true, y_pred))
    print('matthews_corrcoef: %f' % matthews_corrcoef(y_true, y_pred))
    print('\nConfusion matrix:')
    print(confusion_matrix(y_true, y_pred, labels=[0, 1]))
