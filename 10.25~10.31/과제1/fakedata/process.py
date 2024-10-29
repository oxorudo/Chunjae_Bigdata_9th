import pandas as pd


def create_fakedatamart(df: pd.DataFrame) -> pd.DataFrame:

    # 도시 컬럼
    # 나이 컬럼
    # 혈액형
    # 나이대 컬럼

    df['city'] = df['residence'].str.split().str[0]
    df['age'] = 2024 - df['birthdate'].str[:4].astype(int)
    df['blood'] = df['blood_group'].replace({r'\+': '', '-': ''}, regex=True)
    df['age_category'] = df['age'].apply(categorize_age)

    df_list = ['uuid', 'name', 'job', 'sex', 'blood', 'city', 'birthdate', 'age', 'age_category']

    df_datamart = df[df_list]

    return df_datamart


def categorize_age(age: int) -> str:
    if age >= 90:
        return '90대 이상'
    else:
        return f"{(age // 10) * 10}대"