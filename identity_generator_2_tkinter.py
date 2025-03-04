import pandas as pd
import numpy as np
import random
from random_pesel import RandomPESEL



# Function to load data from files and calculate probability
def load_data(firstname_file, lastname_file, secondname_file):
    try:
        firstnames_df = pd.read_excel(firstname_file)
        lastnames_df = pd.read_excel(lastname_file)
        secondnames_df = pd.read_csv(secondname_file) if secondname_file else None
        print("Files loaded successfully")
        print(f"Firstnames shape: {firstnames_df.shape}")
        print(f"Lastnames shape: {lastnames_df.shape}")
        if secondnames_df is not None:
            print(f"Secondnames shape: {secondnames_df.shape}")
    except Exception as e:
        print(f"Error reading files: {e}")
        return None, None, None

    try:
        total_firstnames = firstnames_df.iloc[:,2].sum()
        total_lastnames = lastnames_df.iloc[:,1].sum()

        firstnames_df['probability'] = firstnames_df.iloc[:,2] / total_firstnames
        lastnames_df['probability'] = lastnames_df.iloc[:,1] / total_lastnames

        if secondnames_df is not None:
            total_secondnames = secondnames_df.iloc[:, 2].sum()
            secondnames_df['probability'] = secondnames_df.iloc[:, 2] / total_secondnames
    except KeyError as e:
        print(f"Error in data format: Missing expected column {e}")
        return None, None, None

    return firstnames_df, lastnames_df, secondnames_df

# Function to generate random fullnames and probability
def generate_name_with_probability(firstnames_df, lastnames_df, secondnames_df=None, include_secondname=False):
    
    if firstnames_df is None or lastnames_df is None or (include_secondname and secondnames_df is None):
        raise ValueError("One or more required DataFrames are None")
    
    firstname = np.random.choice(firstnames_df.iloc[:,0], p=firstnames_df['probability'])
    lastname = np.random.choice(lastnames_df.iloc[:,0], p=lastnames_df['probability'])

    if include_secondname and secondnames_df is not None:
        secondname = np.random.choice(secondnames_df.iloc[:, 0], p=secondnames_df['probability'])
        fullname = f"{firstname} {secondname} {lastname}"
        secondname_prob = secondnames_df[secondnames_df.iloc[:, 0] == secondname]['probability'].values[0]
        combined_prob = firstnames_df[firstnames_df.iloc[:, 0] == firstname]['probability'].values[0] * \
                        secondname_prob * \
                        lastnames_df[lastnames_df.iloc[:, 0] == lastname]['probability'].values[0]

    
    else:
        fullname = f"{firstname} {lastname}"
        combined_prob = firstnames_df[firstnames_df.iloc[:, 0] == firstname]['probability'].values[0] * \
                        lastnames_df[lastnames_df.iloc[:, 0] == lastname]['probability'].values[0]
    
    return fullname, combined_prob

# Loading files

female_firstnames_df, female_lastnames_df, female_secondnames_df = load_data(
    'db/firstname_female.xlsx', 'db/lastname_female.xlsx', 'db/secondname_female.csv'
)
if female_firstnames_df is None or female_lastnames_df is None:
    print("Failed to load female names data.")
else:
    print("Female names data loaded successfully")

male_firstnames_df, male_lastnames_df, male_secondnames_df = load_data(
    'db/firstname_male.xlsx', 'db/lastname_male.xlsx', 'db/secondname_male.csv'
)
if male_firstnames_df is None or male_lastnames_df is None:
    print("Failed to load male names data.")
else:
    print("Male names data loaded successfully")    

# Function generating identity basing on gender and optional secondname
def generate_identity(gender, include_secondname):
    if gender.lower() == 'female':
        name, probability = generate_name_with_probability(female_firstnames_df, female_lastnames_df, female_secondnames_df, include_secondname)
        pesel = RandomPESEL().generate(gender='f')
    elif gender.lower() == 'male':
        name, probability = generate_name_with_probability(male_firstnames_df, male_lastnames_df, male_secondnames_df, include_secondname)
        pesel = RandomPESEL().generate(gender='m')
    else:
        raise ValueError("Gender must be 'male' or 'female'")
    
    print(f"Generated name: {name}")
    name_parts = name.split()
    print(f"Name parts: {name_parts}")
    
    if include_secondname and len(name_parts) == 3:
        firstname, secondname, lastname = name_parts
    elif not include_secondname and len(name_parts) == 2:
        firstname, lastname = name_parts
        secondname = None
    else:
        raise ValueError("Unexpected name format")
    
    return firstname, secondname, lastname, pesel, probability