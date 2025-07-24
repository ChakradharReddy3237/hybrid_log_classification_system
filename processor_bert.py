from sentence_transformers import SentenceTransformer
import joblib

# Load the model
classifer_model = joblib.load('Models/log_classifier.joblib')

# Load the SentenceTransformer model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def classify_with_bert(log_message):
    # Generate the embedding for the log message
    message_embedding = embedding_model.encode(log_message)

    probabilities = classifer_model.predict_proba([message_embedding])[0]

    if max(probabilities) < 0.5:
        return "UnClassified"


    # Predict the class
    prediction_class = classifer_model.predict([message_embedding])[0]

    return prediction_class

if __name__ == "__main__":
    log_messages = [
        "User User123 logged in.",
        "Backup started at 2023-10-01 12:00:00.",
        "Multiple bad login attempts detected.",
        "SSL certificate validation failed.",
        "System configuration invalid for module X.",
        "Hey Bro, chill ya!"
    ]

    for log in log_messages:
        classification = classify_with_bert(log)
        print(log, "->" , classification)