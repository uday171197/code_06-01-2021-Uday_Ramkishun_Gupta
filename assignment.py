import pandas as pd
import numpy as np

def find_category(x,y):
    """
    This function will find the person `BMI Category` & `Health risk` based BMI values.

    Args:
        variable (x):  This is BMI value of person
        variable (y):  This is index value where 0 index for BMI Category or 1 for Health risk
    Returns:
        type: It will return `BMI Category` & `Health risk` based on index values


    """

    if  x <= 18.4:
        return ('Underweight','Malnutrition risk')[y]
    elif 18.5 <= x <= 24.9:
        return ('Normal weight','Low risk')[y]
    elif 25 <= x <= 29.9:
        return ('Overweight','Enhanced risk')[y]
    elif 30 <= x <= 34.9:
        return ('Moderately obese','Medium risk')[y]
    elif 35 <= x <= 39.9:
        return ('Severely obese','High risk')[y]
    elif  x >= 40:
        return ('Very severely obese','Very high risk')[y]

def main(data):
    # data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
    df = pd.DataFrame(data)
    df['BMI'] = np.vectorize(lambda x,y: round(y/((x*0.01)**2),1))(df['HeightCm'],df['WeightKg'])
    df['BMI Category'] = np.vectorize(find_category)(df['BMI'],0)
    df['Health risk'] = np.vectorize(find_category)(df['BMI'],1)
    # df[df['BMI Category'] == 'Overweight' ]
    df1 = df.groupby(['BMI Category']).Gender.count().reset_index()
    df1.columns = ['BMI Category', 'Count']
    try:
        total = df1[df1['BMI Category']==i]['Count'].values[0]
    except:
        total = 0
    # print('total number of overweight people : {}'.format(str(total)))
    # print(df.to_dict('records'))
    return df1.to_dict('records')

if __name__ == "__main__":
    data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
    # data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
    print(main(data))
