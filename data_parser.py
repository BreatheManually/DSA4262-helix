"""
Module parses json or zipped json m6a data into panda dataframe. 
"""

import gzip
import json
import pandas as pd

import sklearn
from sklearn.model_selection import train_test_split
import pandas as pd

class DataParser:
    
    def __init__(self, data, label_data = ""):
        self.path_to_data = data
        self.label_data = label_data
    
    
    def full_parse(self):
        """
        Parses data, combines labeled data and unlabeled data.
        """
        dictionary = eval(str(self.pull_data_into_dict()))
        df = self.data_to_df(dictionary)
        return df

    def parse_without_labels(self):
        """
        Parses unlabeled data.
        """
        dictionary = eval(str(self.pull_data_into_dict()))
        df = self.data_to_df_no_labels(dictionary)
        return df
    
    def data_to_df(self, dictionary):
        """
        Convert data into a df with appropriate column names this includes labels.
        """
        rows = []
        for key, value in dictionary.items():
            row = {
                'transcript_id': key[0],
                'transcript_position': key[1],
                'first5': value[0],
                # metrics for 1st 5
                'first_signal_length(mean)': value[1][0],
                'first_signal_var(mean)': value[1][1],
                'first_signal_strength(mean)': value[1][2],
                'second5': value[2],
                # metrics for 2nd 5
                'second_signal_length(mean)': value[3][0],
                'second_signal_var(mean)': value[3][1],
                'second_signal_strength(mean)': value[3][2],
                'third5': value[4],
                'third_signal_length(mean)': value[5][0],
                'third_signal_var(mean)': value[5][1],
                'third_signal_strength(mean)': value[5][2],
                'label': value[6]
            }
            rows.append(row)
        return pd.DataFrame(rows)
    
    def data_to_df_no_labels(self, dictionary):
        """
        Convert data into a df with appropriate column names this does not include labels.
        """
        rows = []
        for key, value in dictionary.items():
            row = {
                'transcript_id': key[0],
                'transcript_position': key[1],
                'first5': value[0],
                # metrics for 1st 5
                'first_signal_length(mean)': value[1][0],
                'first_signal_var(mean)': value[1][1],
                'first_signal_strength(mean)': value[1][2],
                'second5': value[2],
                # metrics for 2nd 5
                'second_signal_length(mean)': value[3][0],
                'second_signal_var(mean)': value[3][1],
                'second_signal_strength(mean)': value[3][2],
                'third5': value[4],
                'third_signal_length(mean)': value[5][0],
                'third_signal_var(mean)': value[5][1],
                'third_signal_strength(mean)': value[5][2],
            }
            rows.append(row)
        return pd.DataFrame(rows)
    
    
    def pull_data_into_dict(self):
        """
        Convert data from json to a dictionary.
        """
        
        listofjsondata = []
        # If file is gzipped
        if self.path_to_data[-8:] == '.json.gz':
            with gzip.open(self.path_to_data, 'rb') as f:
                file_content = f.read()

            listofjsondata = file_content.splitlines()
        
        # If file is json
        if self.path_to_data[-5:] == '.json':
            with open(self.path_to_data, 'r') as f:
                for line in f:
                    listofjsondata.append(line.strip())
        
        if self.label_data != "":
            label_data = pd.read_csv(self.label_data)
        
        fulldict = {}
        
        
        i = 0
        length = len(listofjsondata)
        
        
        for jsonitem in listofjsondata:
            i += 1
            transdict = json.loads(jsonitem)
            # This just helps to see how many is left.
            if i % 5000 == 0:
                print(str(i) + "/" + str(length))
            for transcript_id in transdict.keys():
                for position_id in transdict[transcript_id].keys():
                    for nucleotides in transdict[transcript_id][position_id].keys():
                        
                        # Split into 5-mer
                        first_five = nucleotides[0:5]
                        second_five = nucleotides[1:6]
                        third_five = nucleotides[2:7]

                        #Adding all the values up to get average
                        if self.label_data != "":
                            label = label_data[(label_data['transcript_id'] == transcript_id) & (label_data['transcript_position'] == int(position_id))].iloc[0]["label"]
                        total_scans = 0
                        first_length_aggregate = 0
                        first_sd_aggregate = 0
                        first_mean_aggregate = 0
                        
                        second_length_aggregate = 0
                        second_sd_aggregate = 0
                        second_mean_aggregate = 0
                        
                        third_length_aggregate = 0
                        third_sd_aggregate = 0
                        third_mean_aggregate = 0
                        
                        for first_length, first_sd, first_mean, second_length, second_sd, second_mean, third_length, third_sd, third_mean in transdict[transcript_id][position_id][nucleotides]:
                            total_scans += 1
                            first_length_aggregate += first_length
                            first_sd_aggregate += first_sd
                            first_mean_aggregate += first_mean
                            
                            second_length_aggregate += second_length
                            second_sd_aggregate += second_sd
                            second_mean_aggregate += second_mean
                            
                            third_length_aggregate += third_length
                            third_sd_aggregate += third_sd
                            third_mean_aggregate += third_mean
                        
                        #Get mean of all
                        first_five_mean = (first_length_aggregate/total_scans, first_sd_aggregate/total_scans, first_mean_aggregate/total_scans)
                        second_five_mean = (second_length_aggregate/total_scans, second_sd_aggregate/total_scans, second_mean_aggregate/total_scans)
                        third_five_mean = (third_length_aggregate/total_scans, third_sd_aggregate/total_scans, third_mean_aggregate/total_scans)
                        
                        if self.label_data != "":
                            fulldict[transcript_id, position_id] = first_five, first_five_mean, second_five, second_five_mean, third_five, third_five_mean, label
                        else:
                            fulldict[transcript_id, position_id] = first_five, first_five_mean, second_five, second_five_mean, third_five, third_five_mean
        return fulldict