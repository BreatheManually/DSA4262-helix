import argparse
from data_parser import DataParser as DataParser
from model_user import ModelUser as ModelUser
import pandas as pd
from joblib import load
import os

def main():
    parser = argparse.ArgumentParser(description="For help in commands, refer to README.")
    
    parser.add_argument('--data_path', type=str, default="data/test_data.csv", help='File location of data, csv file.')
    parser.add_argument('--label_path', type=str, help='File location of data labels')
    parser.add_argument('--model_path', type=str, default="savedModels/rfc", help='File location of the model, .joblib file')
    parser.add_argument('--function', required=True, type=str, default="predict", choices=["parse", "predict", "train"], help="Choose predict/train/parse, predict by default.")
    parser.add_argument('--output',required=True, type=str, help='Name and path of output')
    
    args = parser.parse_args()
    
    #Checking if output already exists
    if os.path.exists(args.output):
        print(f"File {args.output}, already exists. Choose a different filename")
        return None
    
    #Using parse function
    if args.function == "parse":
        if args.label_path is None:
            parser = DataParser(args.data_path)
            df = parser.parse_without_labels()
        else:
            parser = DataParser(args.data_path, args.label_path)
            df = parser.full_parse()
            
        #Adds .csv to the output
        df.to_csv(args.output + ".csv")
        return None
    
    #For predict or train, load model and pull csv file.
    print("Loading csv data file...")
    if args.data_path[-3:] == "csv":
        data_df = pd.read_csv(args.data_path)
    else:
        print("Data file is not .csv")
    
    #Loading model for predicting or training
    print("Loading model...")
    modelUser = ModelUser(load(args.model_path))
    
    #Predict data
    if args.function == "predict":
        print("Model Predicting...")
        if "label" in data_df.columns:
            print("The data input has labels, wrong input.")
            return None
        
        #Adds .csv to the output.
        pd.DataFrame(modelUser.predict(data_df)).to_csv(args.output + ".csv")
        return None
    
    #Train data
    if args.function == "train":
        
        print("Training Model...")
        if "label" not in data_df.columns:
            print("The data input has no labels, wrong input.")
            return None
        
        modelUser.train_test_model(data_df)
        print("Outputing Model...")
        modelUser.output_model(args.output)
        return None
         
    

if __name__ == "__main__":
    main()