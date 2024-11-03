from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import roc_curve, auc, precision_recall_curve
from sklearn.base import BaseEstimator
import matplotlib.pyplot as plt
from joblib import dump
import pandas as pd
import os

class ModelUser:
    def __init__(self, model):
        """
        Initalise traintest class with model. Takes in sklearn model.
        """
        if not isinstance(model, BaseEstimator):
            raise TypeError("The model should be a scikit-learn estimator.")
        self.model = model
        os.makedirs("./savedModels", exist_ok=True)
    
    def train_test_model(self, data):
        """
        Trains model and get accuracy scores.
        Output:
        None
        """
        train_data, train_labels, test_data, test_labels = self.split_data(data)
        self.model.fit(train_data, train_labels)
        self.get_scores(test_data, test_labels)
        y_probs = self.model.predict_proba(test_data)[:, 1]
        self.get_auc_curve(test_labels, y_probs)
        self.get_pr_curve(test_labels, y_probs)
    
    def predict(self, no_labels_data):
        """
            Takes in data with no labels.
            Output: 
            Prediction using model.
        """
        no_labels_data.drop(columns=['transcript_id', 'transcript_position', 'first5', 'second5', 'third5'], inplace = True)
        return self.model.predict(no_labels_data)
    
    def output_model(self, model_path = "savedModels/default"):
        """
            Puts model into a savedModels file.
            Output:
            None
        """
        dump(self.model, model_path)
    
    def split_data(self, data):
        train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
        
        
        train_labels = train_data['label']
        train_data = train_data.drop(columns=['label'])
        #Unneeded but may be changed.
        train_data = train_data.drop(columns=['transcript_id', 'transcript_position', 'first5', 'second5', 'third5'])

        test_labels = test_data['label']
        test_data = test_data.drop(columns=['label'])
        #Unneeded but may be changed.
        test_data = test_data.drop(columns=['transcript_id', 'transcript_position', 'first5', 'second5', 'third5'])

        return train_data, train_labels, test_data, test_labels
        
    def get_scores(self, test_data, test_labels):
        y_pred = self.model.predict(test_data)
        accuracy = accuracy_score(test_labels, y_pred)
        print(f"Accuracy: {accuracy * 100:.2f}%")

        precision = precision_score(test_labels, y_pred)
        print(f"Precision: {precision:.2f}")

        recall = recall_score(test_labels, y_pred, average='macro')  
        print(f"Recall: {recall:.2f}")
        
        
    
    def get_auc_curve(self, test_labels, y_probs):
        # For AUC
        
        fpr, tpr, thresholds = roc_curve(test_labels, y_probs)
        roc_auc = auc(fpr, tpr)
        plt.figure()
        plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic (ROC) Curve')
        plt.legend(loc="lower right")
        plt.show()
    
    def get_pr_curve(self, test_labels, y_probs):
        # For Precision Recall Curve
        
        precision, recall, _ = precision_recall_curve(test_labels, y_probs)
        pr_auc = auc(recall, precision)
        plt.figure(figsize=(8, 6))
        plt.plot(recall, precision, marker='.', label=f'PR AUC = {pr_auc:.2f}')
        plt.title('Precision-Recall Curve')
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.legend(loc='lower left')
        plt.grid()
        plt.show()
        