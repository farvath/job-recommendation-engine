## Job recommendations engine 
This job recommendation engine is built using a combination of data scraping, machine learning techniques and deployed in a streamlit application. The model is built on a custom made a dataset by combining the survey conducted by stackoverflow(2018) and a kaggle dataset , data has preprocessed using custom components, and then applies machine learning algorithms( Collaborative Based recommendation system ) to generate personalized recommendations. The system uses historical data to create a similarity matrix (cosine similarity metric).  The  recommendation is solely on the skills provided in job posting and skills that the candidate has . 

## Dataset

Stackoverflow Survey dataset : [Link](https://www.kaggle.com/stackoverflow/stack-overflow-2018-developer-survey#survey_results_public.csv)


Kaggle Dataset for job-postings : [Link](https://www.kaggle.com/PromptCloudHQ/us-technology-jobs-on-dicecom)

## Feature Extraction and preprocessing
Initiallly a Exploratory data analysis (EDA) is done . 

In order to build a custom dataset feature extraction is done. I have decided to use certain columns containing the skills section , technologies worked on , etc... from the stackoverflow dataset. details can be `feature_extraction_user_a.ipynb` and `feature_extraction_user_b.ipynb`.


Next, preprocessed the job opening dataset taken from the kaggle and built a random users-company dataset can be found as `colabdata.csv`.

Detailed features extracted from the datset can be found in the `Features` folder

## Collaborative Filtering 
1. Download the stack overflow dataset and the job-postings dataset from the above link and place into `/data/collaborative filtering` folder.

2. Run collaborative filtering.ipynb to check the output of Collaborative filtering recommendations.


## Implementation  :

In order to run the collaborative filtering model:
1. Create a python virtual environment, activate it and install the packages from requirements.txt file :
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
2. Kindly download the two datasets mentioned above and place them in the data folder . Run the `collaborative filtering.ipynb`

3. The model depends on all files in the data folder. The csv files in data folder contain the userskills and colabdata.

4. The `recommendations.csv` contains top 10 recommendations for a random sample (first 200 users) of the Stack Overflow dataset.

5. `Inferences.ipynb` : This contains code which was used to make inferences about the dataset.


## Usage

To run the files, download the stack overflow dataset and the job-postings dataset from the given link and place into /data/collaborative filtering folder.
Run `collaborative filtering.ipynb` to check the output of CF recommendations based on skills .

Inorder to ease the process i have stored the ouptut of first 200 users in `recommendations.csv`. You can directly use that for inference. 

Also, similarity matrix is also exported as `similarity_matrix.pkl`. (NOTE: MATRIX IS FOR WHOLE DATASET IS EXPORTED)

You may indiviually run the `End-to-End/collaborative filtering.ipynb` file or run using streamlit application :

1. First clone the repository :
    ```bash
    git clone https://github.com/farvath/job-recommendation-engine.git
    ```
2. Replace the pre-processed data paths stored in pickle files (e.g.,  similarity_matrix.pkl), make sure these files are present in the same directory as your application (app.py).
3. In your terminal, navigate to your project directory(Frontend/app.py) and run the following command:
   ```bash
   streamlit run app.py
   ```


## Assumptions
1. Majority of the candidates have registered themselves and have their own user_id.
2. Out of the 5000 candidates , we have assumed that around 2000 candidates have already be hired .
3. Every candidate has rated all the recommended jobs that they have got before.


## Interface 

<img src="https://github.com/farvath/job-recommendation-engine/blob/main/inference_results/result.jpg" width="400px" height="400px" alt="alt text">