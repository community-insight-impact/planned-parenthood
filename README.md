# CDC School Profile & Flags  
  
1. **Questionnaires**:    
The document of '2024-Principal.docx' and '2024-Teacher.docx' are the two 2024 SCHOOL HEALTH PROFILES from CDC to assess school health education. Here, we try to match the questions in these two documents with policy implementation flags.

2. **Flags and Match**:    
This excel document includes 3 sheets showing all the details of flags and matches.    
The sheet named 'Flags' is the summary of all the flags pulled from Guttmacher.     
The sheet named 'Flag-Matched Number' summarizes each flag, along with the number of questions in the profiles that reflect this flag. (since a flag may be reflected by multiple questions)     
The sheet named 'Match' specifically details which flags are reflected by each question from the two questionnaires. (since a question can reflect several flags)       
  
    
# Confounding Variables
This folder includes all the raw and cleaned datasets for the confounding variables (other factors beside policy that can influence youth health outcomes).

1. **Summary of Confounding Variables and Data**:           
'Confounding Variables.xlsx' : This document outlines all the confounding variables we use, along with the available data and the sources where this data was obtained. The sheet titled 'Estimation' details the method and data used to estimate the school enrollment breakdown, filling all the gaps between 1990 and 2023.     
'Variables_Availability_Summary.xlsx' : The file outlines the availability of each confounding variable for every state and year, providing a clear summary of the available data.

2. **Raw Data**:     
I recorded raw data here for reference if needed. The raw data includes 'Religious Affiliation.xlsx', 'access.xlsx', 'private_enrollment.xlsx', 'public_enrollment.xlsx', and files in the folders 'Race', 'family', medium income', 'mother labor force', 'population'.

3. **Transformed Data**:     
I transformed all the raw data into a consistent format and recorded it in the 'Transformed Datasets' folder.

4. **Final Data**:     
After transforming all the datasets, I combined them and cleaned the dataset. Then I estimated the data for public and private enrollment. 'Full_Data_afterEstimation.xlsx' is the dataset with all the states and territories from 1990 to 2024. 'Final_Data.xlsx' contains the final dataset after completing all estimations and data cleaning, with the data for territories removed.
  
    
# Outcome Variables  

1. **Outcome Variables**:     
In the folder 'outcome', there are:    
Original Data: Abortion rate.csv, Birth rate.csv, Pregnancy rate.csv, hiv data.csv, std data.csv;      
Calculate Rate or Impute for NA Data: abortion_rate.csv, birth_rate.csv, pregnancy_rate.csv, hiv_rate.csv, std_rate.csv;     
Adjusted Data: files with adjusted in their names.      
The adjusted data removed the national trend by subtracting the average of the outcome across states, and standardized the units for the rates, so they are all expressed as per the same number of people.

2. **Combined Dataset**:    
I combined all the outcome datasets for each state and year in 'Total_Outcome.csv'.

3. **EDA**:    
I’ve included all my EDA work on outcome variables in the file 'EDA.docx', particularly highlighting the positive correlations among the outcome variables. I also uploaded 'excel_clustered_states.xlsx', which contains the clustering of states based on time-series change patterns (STL Decomposition) from 2010 to 2017, when the data is complete.


