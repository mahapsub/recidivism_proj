import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def get_data(file_name="compass/propublica_data_for_fairml.csv"):
    rec_df = pd.read_csv(file_name)
    X = rec_df[['Number_of_Priors', 'score_factor', 'Age_Above_FourtyFive', 'Age_Below_TwentyFive', 'African_American', 'Asian', 'Hispanic', 'Native_American', 'Other', 'Female', 'Misdemeanor']].values
    y = rec_df['Two_yr_Recidivism'].values
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=42)
    return X_train, X_test, y_train, y_test


def get_adapted_predictions(y_prob, conf_thres):
    """
    Gets adapted predictions based on confidence thresholds.
    :param y_prob:
    :param conf_thres:
    :return:
    """
    preds = []
    for val in y_prob:
        if val[0] > conf_thres or val[1] > conf_thres:
            if val[1] > val[0]:
                preds.append(1)
            else:
                preds.append(0)
        else:
            preds.append(-1)
    return np.array(preds)


def calculate_metrics(y_pred, y_actual):
    """
    Gets false pos/neg for predictions vs actual data.
    :param y_pred:
    :param y_actual:
    :return:
    """
    print(y_pred)
    num_considered = 0
    false_positives = 0
    false_negatives = 0
    acc = 0
    for i in range(len(y_pred)):
        if y_pred[i] == -1:
            break
        if y_pred[i] != y_actual[i]:
            if y_pred[i]==1:
                false_positives +=1
            else:
                false_negatives +=1
        else:
            acc +=1
        num_considered += 1
    if num_considered == 0:
        print('Model confidence less than threshold')
    else:
        print('-----undecided rate {:.2f}'.format((1-(num_considered/len(y_pred)))*100))
        print('-----False Positive Rate: {:.2f}'.format(false_positives/num_considered*100))
        print('-----False Negative Rate: {:.2f}'.format(false_negatives/num_considered*100))
        print('-----Model Acc: {:.2f}'.format(acc/num_considered*100))


