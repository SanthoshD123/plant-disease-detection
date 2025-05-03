import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import os

# Define paths
base_dir = "C:\\Users\\User\\PycharmProjects\\plant disease detection\\archive\\PlantVillage"  # Replace with the correct path

# Apply data augmentation
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

# Validation generator (without augmentation, only rescaling)
val_datagen = ImageDataGenerator(rescale=1. / 255, validation_split=0.2)

# Training generator
train_generator = train_datagen.flow_from_directory(
    base_dir,
    target_size=(100, 100),  # Adjust based on image resolution
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

# Validation generator
validation_generator = val_datagen.flow_from_directory(
    base_dir,
    target_size=(100, 100),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

# Define an improved CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.5),  # Add dropout to prevent overfitting
    layers.Dense(train_generator.num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    train_generator,
    epochs=15,  # Increased epochs
    validation_data=validation_generator
)

# Save the model using the Keras format
model.save('plant_disease_model.keras')

# Evaluate the model on the validation set
val_loss, val_acc = model.evaluate(validation_generator)
print(f"Validation accuracy: {val_acc * 100:.2f}%")
