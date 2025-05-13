from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

from imblearn.over_sampling import SMOTE




def train_model(df):
    # 🎯 Split features and target
    X = df.drop("Risk Level", axis=1)
    y = df["Risk Level"]

    # 🔀 Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 🤖 List of models to test
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(),
        "Gradient Boosting": GradientBoostingClassifier(),
        "Support Vector Machine": SVC(),
        "Naive Bayes": GaussianNB(),
    }

    best_model = None
    best_accuracy = 0

    print("\n Model Performance Comparison:\n")

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        print(f" {name}")
        print(f"   Accuracy: {acc:.4f}")
        print("   Classification Report:\n", classification_report(y_test, y_pred))

        if acc > best_accuracy:
            best_accuracy = acc
            best_model = model

    print(f"\n Best Model: {type(best_model).__name__} with accuracy {best_accuracy:.4f}")

    return best_model




