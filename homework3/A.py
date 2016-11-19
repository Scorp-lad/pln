from main import replace_accented
from sklearn import svm
from sklearn import neighbors
import collections
import nltk

# don't change the window size
window_size = 10

# A.1
def build_s(data):
    '''
    Compute the context vector for each lexelt
    :param data: dic with the following structure:
        {
			lexelt: [(instance_id, left_context, head, right_context, sense_id), ...],
			...
        }
    :return: dic s with the following structure:
        {
			lexelt: [w1,w2,w3, ...],
			...
        }

    '''
    s = {}

    # implement your code here
    for lexelt in data:
        _set = set()
        for instance in data[lexelt]:
            left_tokens = nltk.word_tokenize(instance[1])[-window_size:]
            right_tokens = nltk.word_tokenize(instance[3])[:window_size]
            for word in left_tokens:
                _set.add(word)
            for word in right_tokens:
                _set.add(word)
        s[lexelt] = list(_set)
    
    return s


# A.1
def vectorize(data, s):
    '''
    :param data: list of instances for a given lexelt with the following structure:
        {
			[(instance_id, left_context, head, right_context, sense_id), ...]
        }
    :param s: list of words (features) for a given lexelt: [w1,w2,w3, ...]
    :return: vectors: A dictionary with the following structure
            { instance_id: [w_1 count, w_2 count, ...],
            ...
            }
            labels: A dictionary with the following structure
            { instance_id : sense_id }

    '''
    vectors = {}
    labels = {}

    # implement your code here
    """
        Since we just consider the lexelt which in in the sample list,
        thus we discard the other word and not to statistic
    """
    for instance in data:
        _vec = [0]*len(s)
        for word in nltk.word_tokenize(instance[1]):
            try:
                _vec[s.index(word)] += 1
            except:
                pass
        for word in nltk.word_tokenize(instance[3]):
            try:
                _vec[s.index(word)] += 1
            except:
                pass
        vectors[instance[0]] = _vec
        if ( not instance[4] == 'U') and ( not instance[4] == ''):
            labels[instance[0]] = instance[4]

    return vectors, labels


# A.2
def classify(X_train, X_test, y_train):
    '''
    Train two classifiers on (X_train, and y_train) then predict X_test labels

    :param X_train: A dictionary with the following structure
            { instance_id: [w_1 count, w_2 count, ...],
            ...
            }

    :param X_test: A dictionary with the following structure
            { instance_id: [w_1 count, w_2 count, ...],
            ...
            }

    :param y_train: A dictionary with the following structure
            { instance_id : sense_id }

    :return: svm_results: a list of tuples (instance_id, label) where labels are predicted by LinearSVC
             knn_results: a list of tuples (instance_id, label) where labels are predicted by KNeighborsClassifier
    '''

    svm_results = []
    knn_results = []

    svm_clf = svm.LinearSVC()
    knn_clf = neighbors.KNeighborsClassifier()

    
    # implement your code here
    _x = []
    _y = []
    for instance_id in y_train:
        _x.append(X_train[instance_id])
        _y.append(y_train[instance_id])
    #print _x
    print "----- Train -----"
    svm_clf.fit(_x, _y)
    knn_clf.fit(_x, _y)

    for instance_id in X_test:
        svm_results.append((instance_id, svm_clf.predict(X_test[instance_id])))
        knn_results.append((instance_id, knn_clf.predict(X_test[instance_id])))

    return svm_results, knn_results

# A.3, A.4 output
def print_results(results ,output_file):
    '''

    :param results: A dictionary with key = lexelt and value = a list of tuples (instance_id, label)
    :param output_file: file to write output

    '''

    # implement your code here
    # don't forget to remove the accent of characters using main.replace_accented(input_str)
    # you should sort results on instance_id before printing
    with open(output_file, 'w') as f:
        for lexelt in sorted(results):
            for (instance_id, label) in sorted(results[lexelt]):
                _str = str(replace_accented(lexelt)) + ' ' + str(replace_accented(instance_id)) + ' ' + str(replace_accented(unicode(label[0]))) + '\n'
                print _str
                f.write(_str)

# run part A
def run(train, test, language, knn_file, svm_file):
    s = build_s(train)
    svm_results = {}
    knn_results = {}
    for lexelt in s:
        X_train, y_train = vectorize(train[lexelt], s[lexelt])
        X_test, _ = vectorize(test[lexelt], s[lexelt])
        svm_results[lexelt], knn_results[lexelt] = classify(X_train, X_test, y_train)

    print_results(svm_results, svm_file)
    print_results(knn_results, knn_file)



