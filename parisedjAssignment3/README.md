#
# Dom Parise 3/20/14
# assignment3 readme
#

For my implementation, I've used an object-oriented model, creating 2 classes:
	Classifier:
		Exposes the Classifier.train(dictOfDocsByClass) and Classifier.test(doc) methods.
		.train() takes a dictionary with class names as keys and an arbitrary list of documents as values and has no output
		.test() takes a document as input and returns the calculated classification

	Classification:
		Internal class used by the Classifier that performs probability calculations based on the dataset.
		i.e. each list of documents labelled as a classification as input to Classifier.train()
			is used in producing the probability of finding a word given the classification
		The classification is constructed with all variables necessary to perform these calculations

To run the code in order to perform the calculations:
open assignment3.py
point lines {14, 15, 55, 58, 61, 68, 72} to the proper data directories
save and exit the file
run:
python assignment3.py
the precision calculations will be output to stdout

My calculated percentages are:

1. 0.553846153846

2. 0.986666666667
