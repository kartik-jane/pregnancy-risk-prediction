## from src.preprocessing import preprocess_data

# # Load and clean the data
# df = preprocess_data("data/Maternal fetal data.xlsx")

# # Show first few rows
## print(df.head())


 ####1111111111

# Step 1: Import preprocessing


# from src.preprocessing import preprocess_data

# # Step 2: Import model training
# from src.model import train_model

# # 🚀 Load and preprocess the dataset
# df = preprocess_data("data/Maternal fetal data.xlsx")

# # ✅ Train and evaluate the model
# model = train_model(df)


############222222222222222222222


from src.preprocessing import preprocess_data
from src.model import train_model
import joblib
import os

# Step 1: Load and preprocess the data
df = preprocess_data("data/Maternal fetal data.xlsx")


# Step 2: Train and evaluate the model
model = train_model(df)

# Step 3: Save the trained model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/best_model.pkl")
print("✅ Model saved to models/best_model.pkl")



# 🔍 Print actual column names to match in Streamlit
print("📋 Columns used to train the model:")
print(df.columns.tolist())

# Optional: stop here temporarily to just inspect
exit()

