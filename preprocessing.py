import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(filepath):
    # 📥 Load the Excel dataset
    df = pd.read_excel(filepath)

    # 🛠️ Make a copy to avoid modifying original
    df_clean = df.copy()

    # 🧽 Rename problematic column name
    df_clean.rename(columns={"Body Temperature (Â°C)": "Body Temperature (C)"}, inplace=True)

    # 🎯 Convert 'Pregnancy Number' like 'G3P1' into total pregnancies
    df_clean['Pregnancy Number'] = df_clean['Pregnancy Number'].str.extract(r'G(\d+)P(\d+)').astype(int).sum(axis=1)

    # 🔢 Encode 'Fetal Position'
    label_encoder_fp = LabelEncoder()
    df_clean['Fetal Position'] = label_encoder_fp.fit_transform(df_clean['Fetal Position'])

    # 🎯 Encode 'Risk Level' target variable: Low=0, Medium=1, High=2
    risk_mapping = {'Low': 0, 'Medium': 1, 'High': 2}
    df_clean['Risk Level'] = df_clean['Risk Level'].map(risk_mapping)

    return df_clean


from src.preprocessing import preprocess_data

# Load and preprocess the data
df_clean = preprocess_data("data/Maternal fetal data.xlsx")

# View cleaned data
print(df_clean.head())
