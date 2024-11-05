# DSA4262 Team Helix: m6A Modification Detection

<h2 align="center"> 
  <img src="https://cbx-prod.b-cdn.net/COLOURBOX65073341.jpg?width=800&height=800&quality=70" alt="drawing" width="200"/>
  <br>
  <center>Detecting m6A modifications in direct RNA sequencing data</center>
</h2>
<summary>Table of Contents</summary>
    <ol>
        <li><a href="#project-description">Project Description</a></li>
        <li><a href="#getting-started-in-ec2-ubuntu-environment">Getting Started (In EC2 Ubuntu Environment)</a></li>
        <li><a href="quick-start-get-prediction-output">Quick Start (Get Prediction Ouput)</a></li>
        <li><a href="#user-guide">User Guide</a></li>
        <li><a href="#file-structure">File Structure</a></li>
        <li><a href="#tech-stack">Tech Stack</a></li>
        <li><a href="#contributors">Contributors </a></li>
        <li><a href="#license">License</a></li>
    </ol>
   
## Project Description
RNA modifications  play a critical role in many biological processes such as regulating gene expression, facilitating immune response and cellular differentiation. The N6-methyladenosine (m6A) modifcation, which involves the addition of a methyl group to a Adenosine(A) base, is the most prevalent modifcation in eukaryotic mRNA. It has been associated with various psychological conditions and pathologies, including cancer. Hence, identifiying m6A sites within RNA is crucial for understanding its regulatory roles in diseases, which can ultimately help in the development of targeted treatments that can more effectively address these conditions.

## Getting Started (In EC2 Ubuntu Environment)
1. Connect to EC2 ubuntu instance.

    Recommended:

    InstanceType: t3.medium

    EBS Volume Size: 100GB

2. Ensure python is installed.
    ```bash
    python3 --version
    ```
    If not installed, install python.
    
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip -y
    ```

3. Navigate to any directory of your choice and clone the repository:

    ```bash
    git clone https://github.com/BreatheManually/DSA4262-helix.git

    # Navigate to the cloned directory
    cd DSA4246-helix/
    ```

4. Install venv if not installed:
    ```bash
    sudo apt install python3-venv
    ```

5. Activate venv and install Python dependencies in a virtual environment:

    For MacOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate

    # Install packages
    pip install -r requirements.txt
    ```

    For Windows
    ```bash
    python3 -m venv venv
    venv/Scripts/activate

    # Install packages
    pip install -r requirements.txt
    ```

## Quick Start (Get Prediction Ouput)
> [!TIP]
>
> **For student evaluators**
>
> If you are in a rush to evaluate and are unable to take the time to read and understand the entire README.
>
> You can run the in this section below to get the prediction results.
1. Parse A549_500.json Data:
    ```bash 
    python app.py --data_path "data/A549_500.json"  --function "parse" --output "data/prediction_data"
    ```
2. Use parsed data to predict output:
    ```bash 
    python app.py --data_path "data/prediction_data.csv" --model_path "savedModels/rfc" --function "predict" --output "predictions"
    ```
3. Look at predicted output:
    ```bash 
    cat predictions.csv
    ```
  
## User Guide

Command app.py, to use:

  ```bash 
  python app.py --[insert flag] "[insert parameter]" --[insert flag2] "[insert parameter2]"
  ```

Flags are as follows:

    --data_path

Default: "data/test_data.csv"

Description: Specifies the file location of the data CSV file.

Usage: Provides the path to data file, should be correct type [labeled data, unlabeled data, raw data] depending on the chosen function.

 ------------------

    --label_path

Default: None

Description: Specifies the file location of the data labels. Does not have a default value, only need for train function.

Usage: **ONLY REQUIRED FOR PARSE FUNCTION.** Provide the path to your labels file, which should align with your data.

------------------

    --model_path

Default: "savedModels/rfc"

Description: Specifies the file location of the model file, which should be a .joblib file.

Usage: If your model file is saved elsewhere, please provide the full path.

------------------

    --function

Default: "predict"

Choices: ["parse", "predict", "train"]

Description: Chooses the function to execute. You must specify one of the options: parse, predict, or train.

Usage: Indicate the desired operation to be performed by the application.

Details: 
-   Parsing without label_path gives data (csv) without labels for prediction.
-   Parsing with label_path gives training data (csv) with labels for training.
-   Train uses model with same parameters but 'resets' training, so it is only trained on dataset given.

------------------

### Example command for parsing sample data:
    python app.py --data_path "data/A549_500.json"  --function "parse" --output "data/prediction_data"

Note: A549_500 is the collection of data for the first 500 transcript & position in the SGNex_A549_directRNA_replicate5_run1 file.

### Example command for predicting with our model with sample data:

    python app.py --data_path "data/prediction_data.csv" --model_path "savedModels/rfc" --function "predict" --output "predictions"


### Example command for training our model with data set 0:

    python app.py --data_path "data/train_data.csv" --model_path "savedModels/rfc" --function "train" --output "savedModels/rfc2"

Note: train_data.csv is dataset0 parsed.

## File Structure

```bash
DSA4246-HELIX/
├── LICENSE
├── requirements.txt
├── data_parser.py
├── model_user.py
├── README.md
├── Model Experimentation
│   └── DSA4262_Intermediate_leaderboard_code.ipynb
├── data
│   └── A549_500.json
│   └── train_data.csv
├── savedModels/
│   └── rfc
├── .gitignore
└── model/
    └── DSA4262_Intermediate_leaderboard_code.ipynb
```


## Tech Stack

- **Pandas**: Pandas is a software library written for the Python programming language for data manipulation and analysis. 

- **SKLearn**: scikit-learn is a free and open-source machine learning library for the Python programming language. 

- **NumPy**: NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

- **Matplotlib**: Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.  


## Contributors 
<div>
 <table>
  <tr>
    <th>No.</th>
    <th>Contributers</th>
    <th>GitHub Link</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Lincoln Teo</td>
    <td><a href="https://github.com/BreatheManually" target="blank_">
    GitHub</a>
    </td>
  </tr>
  <tr>
    <td>2</td>
    <td>Fong Kah Vui</td>
    <td><a href="https://github.com/Kahvui" target="blank_">
    GitHub</a>
    </td>
  </tr>
   <tr>
    <td>3</td>
    <td>Olivia Yap</td>
    <td><a href="https://github.com/oliviadsa3101" target="blank_">
    GitHub</a>
    </td>
  </tr>
  <tr>
    <td>4</td>
    <td>Tay Wan Lin</td>
    <td><a href="https://github.com/Wehnlynn" target="blank_">
    GitHub</a>
    </td>
  </tr>
  <tr>
    <td>5</td>
    <td>Rayner Cheng</td>
    <td><a href="https://github.com/ray1123001" target="blank_">
    GitHub</a>
    </td>
  </tr>
</table> 

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/BreatheManually/DSA4262-helix?tab=MIT-1-ov-file) tab for more details.

[def]: quick-star