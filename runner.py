from pipeline import *

def model_A_orig():
    print('\n\n\n')
    print('Running Random Forest Classifier_Orig')
    from sklearn.ensemble import RandomForestClassifier
    X_train, X_test, y_train, y_test = get_data()
    clf = RandomForestClassifier(n_estimators=100, max_depth=3,random_state=0)
    model = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    y_prob = clf.predict_proba(X_test)
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








def main():
    model_A_orig(); #Random Forest untouched
    model_A_adapted(.60); # Random Forest iwth threshold





if __name__=="__main__":
    main();