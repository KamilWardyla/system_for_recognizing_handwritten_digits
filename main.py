from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pickle
from matplotlib import image as mp_image


def support_vector_machines_classifiers():
    digits = load_digits()
    plt.gray()
    plt.matshow(digits.images[0])
    plt.show()

    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))

    X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.5, shuffle=False)

    svm_classifier = svm.SVC(gamma=0.001)
    svm_classifier.fit(X_train, y_train)

    predicted = svm_classifier.predict(X_test)
    _, axes = plt.subplots(2, 4)
    images_and_labels = list(zip(digits.images, digits.target))
    for ax, (image, label) in zip(axes[0, :], images_and_labels[:4]):
        ax.set_axis_off()
        ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        ax.set_title('Training: %i' % label)
    images_and_prediction = list(zip(digits.images[n_samples // 2:], predicted))
    for ax, (image, prediction) in zip(axes[1, :], images_and_prediction[:4]):
        ax.set_axis_off()
        ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        ax.set_title('Prediction: %i' % prediction)
    print("\nClassification report for classifier %s:\n%s\n" % (
        svm_classifier, metrics.classification_report(y_test, predicted)))
    cm = metrics.confusion_matrix(y_test, predicted)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=digits.target_names)
    disp.plot()
    disp.figure_.suptitle("Confusion Matrix")
    print("\nConfusion matrix:\n%s" % cm)
    print("\nAccuracy of the Algorithm: ", svm_classifier.score(X_test, y_test))
    plt.show()
    return svm_classifier


def save_model_to_file():
    model = support_vector_machines_classifiers()
    filename = 'svm_model.pkl'
    pickle.dump(model, open(filename, "wb"))


def load_model_from_file():
    filename = 'svm_model.pkl'
    loaded_model = pickle.load(open(filename, "rb"))
    # img = mp_image.imread('six_number.png')
    return loaded_model


if __name__ == "__main__":
    # save_model_to_file()
    print(load_model_from_file())

"""
pygame
drawing_array = np.zeros((8, 8))

elif event.type == pygame.MOUSEMOTION and drawing:
            x, y = pygame.mouse.get_pos()
            if (x < 0 or x >= DRAW_WIDTH) or (y < 0 or y >= DRAW_HEIGHT): continue
            row, col = int(y / 20), int(x / 20)
            drawing_array[row][col] = 16
"""