# recidivism_proj

pipeline.py contains all of the helper methods. Runner.py contains all the models.
1. get_data() --> returns train_test_split values.

##Models
1. Model (orig) should return predictions and call calculate_metrics(y_pred, y_test)
2. model (adapted) need to call get_adapted_predictions(y_prob, confidence_threshold).
** y_prob (n x 2)




