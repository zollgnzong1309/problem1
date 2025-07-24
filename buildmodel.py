import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Load data from JSON
with open('hand_data_labeled.json', 'r') as f:
    data = json.load(f)

X = []
y = []
for frame in data.values():
    if frame["landmarks"]:
        hand = frame["landmarks"][0]
        features = []
        for pt in hand:
            features.extend([pt["x"], pt["y"], pt["z"]])
        X.append(features)
        y.append(frame["label"])

X = np.array(X)

le = LabelEncoder()
y_encoded = le.fit_transform(y)
y_cat = to_categorical(y_encoded)

print("Number of classes:", len(le.classes_))
print("Label list:", le.classes_)
X_train, X_test, y_train, y_test = train_test_split(
    X, y_cat, test_size=0.2, stratify=y_encoded, random_state=42
)
# Build the model
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(63,)))
model.add(Dropout(0.3))
model.add(Dense(64, activation='relu'))
model.add(Dense(y_cat.shape[1], activation='softmax'))  

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()
history = model.fit(
    X_train, y_train,
    epochs=30,
    batch_size=16,
    validation_split=0.2,
    verbose=1
)
loss, acc = model.evaluate(X_test, y_test)
print(f"Model accuracy on the test set: {acc * 100:.2f}%")
sample = np.array([X_test[0]])  # chọn 1 mẫu bất kỳ
pred = model.predict(sample)
pred_label = le.inverse_transform([np.argmax(pred)])
print("Dự đoán:", pred_label[0])
# Save the model
model.save('hand_model.h5')
