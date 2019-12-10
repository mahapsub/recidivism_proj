from pipeline import *
import torch
import torch.nn as nn
import torch.nn.functional as F
from model_B_helper import *
def model_A_orig():
    print('\n\n\n')
    print('Running Random Forest Classifier_Orig')
    from sklearn.ensemble import RandomForestClassifier
    X_train, X_test, y_train, y_test = get_data()
    clf = RandomForestClassifier(n_estimators=100, max_depth=3,random_state=0)
    model = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    y_prob = clf.predict_proba(X_test)
    np.savetxt("saved_results/random_forest_classifier.csv", y_prob, delimiter=",")
    calculate_metrics(y_pred, y_test)
def model_A_adapted(confidence_threshold=.75):
    print('\n\n\n')
    print('Running Random Forest Classifier Adapted')
    print('Confidence Threshold: {}'.format(confidence_threshold))
    from sklearn.ensemble import RandomForestClassifier
    X_train, X_test, y_train, y_test = get_data()
    clf = RandomForestClassifier(n_estimators=100, max_depth=3,random_state=0)
    model = clf.fit(X_train, y_train)
    y_prob = clf.predict_proba(X_test)
    y_pred = get_adapted_predictions(y_prob, confidence_threshold)
    calculate_metrics(y_pred, y_test)
def get_model_B_adapted(confidence_threshold=.75):
    print('NN Adapted')
    print('Confidence Threshold: {}'.format(confidence_threshold))
    X_train, X_test, y_train, y_test = pipeline.get_data()
    X = torch.from_numpy(X_train).type(torch.FloatTensor)
    y = torch.from_numpy(y_train).type(torch.LongTensor)

    model = MyClassifier()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    #Number of epochs
    epochs = 10000
    #List to store losses
    losses = []
    for i in range(epochs):
        #Precit the output for Given input
        y_pred = model.forward(X)
        #Compute Cross entropy loss
        loss = criterion(y_pred,y)
        #Add loss to the list
        losses.append(loss.item())
        # print(loss.item())
        #Clear the previous gradients
        optimizer.zero_grad()
        #Compute gradients
        loss.backward()
        #Adjust weights
        optimizer.step()

    y_probs = model.predict(torch.from_numpy(X_test).type(torch.FloatTensor))
    y_preds = get_adapted_predictions(y_probs, confidence_threshold)
    print(y_probs)
    calculate_metrics(y_preds, y_test)
def get_model_B():
    print('NN')
    print('Confidence Threshold: {}'.format(0))
    X_train, X_test, y_train, y_test = pipeline.get_data()
    X = torch.from_numpy(X_train).type(torch.FloatTensor)
    y = torch.from_numpy(y_train).type(torch.LongTensor)

    model = MyClassifier()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    #Number of epochs
    epochs = 10000
    #List to store losses
    losses = []
    for i in range(epochs):
        #Precit the output for Given input
        y_pred = model.forward(X)
        #Compute Cross entropy loss
        loss = criterion(y_pred,y)
        #Add loss to the list
        losses.append(loss.item())
        # print(loss.item())
        #Clear the previous gradients
        optimizer.zero_grad()
        #Compute gradients
        loss.backward()
        #Adjust weights
        optimizer.step()
    y_probs = model.predict(torch.from_numpy(X_test).type(torch.FloatTensor))
    np.savetxt("saved_results/basic_nn_probs.csv", y_probs, delimiter=",")
    y_preds = get_predictions(y_probs)
    calculate_metrics(y_preds, y_test)
def main():
    # print('hello')
    # model_A_orig(); #Random Forest untouched
    # model_A_adapted(.60); # Random Forest iwth threshold
    get_model_B_adapted(.51)
if __name__=="__main__":
    main();