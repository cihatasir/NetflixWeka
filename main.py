import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier
from weka.classifiers import Evaluation
import os
import weka.core.converters as conv
from weka.classifiers import PredictionOutput
# from weka.flow.transformer import ClassSelector
from weka.attribute_selection import ASSearch, ASEvaluation, AttributeSelection
from xml.etree import ElementTree
from xml.etree.ElementTree import parse
from xml.dom import minidom
import shutil
import xml.etree.ElementTree as ET
import re
import weka.plot as plot
from weka.classifiers import GridSearch
import time
import jpype
import django

if plot.matplotlib_available:
    import matplotlib.pyplot as plt

"//////////////////////////////////////////"


def loadDataSet():


    data_dir = "C:\\Users\\casir\\Desktop\\netflix.arff"

    loader = Loader(classname="weka.core.converters.ArffLoader")

    data = loader.load_file(data_dir)  # dataset upload
    data.class_is_first()

    classifier = Classifier(classname="weka.classifiers.bayes.NaiveBayes")

    classifier.build_classifier(data)

    "/////////////////////////////////////////////////////////////////"

    new_data_dir = r'C:\Users\casir\PycharmProjects\django-weka\yeni.arff'

    testData = loader.load_file(new_data_dir)

    testData.class_is_first()

    pred_output = PredictionOutput(classname="weka.classifiers.evaluation.output.prediction.XML")

    evl = Evaluation(testData)

    evl.test_model(classifier, testData, output=pred_output)

    textResults = str(pred_output)

    root = ET.fromstring(textResults)

    for i in root.iter('predicted_label'):
        result = i.text

    os.remove(r'C:\Users\casir\PycharmProjects\django-weka\yeni.arff')

    return result

"////////////////////////////////////////////////////////////////////////////////////////////"


def cloneData(country, rating, duration, genre):

    original = r'C:\Users\casir\Desktop\testing.txt'
    target = r'C:\Users\casir\PycharmProjects\django-weka\yeni.txt'

    shutil.copyfile(original, target)

    file = open(r'C:\Users\casir\PycharmProjects\django-weka\yeni.txt', "a")

    file.write("?" + ",")
    file.write("'" + country + "'" + "," + rating + "," + duration + "," + "'" + genre + "'")

    file.close()

    my_file = r'C:\Users\casir\PycharmProjects\django-weka\yeni.txt'
    base = os.path.splitext(my_file)[0]
    os.rename(my_file, base + '.arff')

"//////////////////////////////////////////////////////////////////////////////////////////////"

