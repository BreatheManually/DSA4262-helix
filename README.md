# DSA4213 Team Helix: m6A Modification Detection

<h2 align="center"> 
  <img src="https://cbx-prod.b-cdn.net/COLOURBOX65073341.jpg?width=800&height=800&quality=70" alt="drawing" width="200"/>
  <br>
  <center>Detecting m6A modifications in direct RNA sequencing data</center>
</h2>

   
## Project Description
RNA modifications  play a critical role in many biological processes such as regulating gene expression, facilitating immune response and cellular differentiation. The N6-methyladenosine (m6A) modifcation, which involves the addition of a methyl group to a Adenosine(A) base, is the most prevalent modifcation in eukaryotic mRNA. It has been associated with various psychological conditions and pathologies, including cancer. Hence, identifiying m6A sites within RNA is crucial for understanding its regulatory roles in diseases, which can ultimately help in the development of targeted treatments that can more effectively address these conditions.

## Getting Started (In EC2 Ubuntu Environment)
1. Connect to EC2 ubuntu instance.

2. Ensure python is installed.
    ```bash
    python --version
    ```
    If not installed, install python.
    
    ```bash
    sudo apt update
    sudo apt install python python-pip -y
    ```

3. Navigate to chosen directory and clone the repository:

    ```bash
    git clone https://github.com/BreatheManually/DSA4262-helix.git
    cd DSA4246-helix
    ```

4. Install Python dependencies in a virtual environment:

    For MacOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

    For Windows
    ```bash
    python3 -m venv venv
    venv/Scripts/activate
    pip install -r requirements.txt
    ```
## User Guide
Use app.py to access commands, flags are as follows:

    --data_path

Default: "data/test_data.csv"

Description: Specifies the file location of the data CSV file.

Usage: Provides the path to data file, if flag not stated, test_data.csv (For Predictions) is used.

    --label_path

Default: None

Description: Specifies the file location of the data labels. Does not have a default value, only need for train function.

Usage: Provide the path to your labels file, which should align with your data.

    --model_path

Default: "savedModels/rfc"

Description: Specifies the file location of the model file, which should be a .joblib file.

Usage: If your model file is saved elsewhere, provide the full path.

    --function

Default: "predict"

Choices: ["parse", "predict", "train"]

Description: Chooses the function to execute. You must specify one of the options: parse, predict, or train.

Usage: Indicate the desired operation to be performed by the application.

Details: 
-   Parsing without label_path gives data (csv) without labels for prediction.
-   Parsing with label_path gives training data (csv) with labels for training.
-   Train uses model with same parameters but 'resets' training, so it is only trained on dataset given.

Example command:

    python app.py --data_path "data/test_data.csv" --model_path "savedModels/rfc" --function "predict" --output "predictions.csv"

## File Structure

```bash
DSA4246-HELIX/
├── LICENSE
├── requirements.txt
├── data_parser.py
├── model_user.py
├── README.md
├── data
│   └── test_data.csv
├── savedModels/
│   └── rfc
├── .gitignore
└── model/
    └── DSA4262_Intermediate_leaderboard_code.ipynb
```


## Tech Stack

- **Pandas**: Pandas is a software library written for the Python programming language for data manipulation and analysis. 

- **SKLearn**: scikit-learn is a free and open-source machine learning library for the Python programming language. 


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