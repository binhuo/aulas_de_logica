import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam





# Configurações
img_height, img_width = 224, 224
batch_size = 32
epochs = 10

# Preparação dos dados
# Supondo que você tenha as imagens em pastas "maçã" e "não_maçã"
data_dir = 'imagens'

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',  # Classificação binária
    subset='training'
)

validation_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'
)

# Criação do modelo
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(img_height, img_width, 3))
base_model.trainable = False  # Congela a base

model = Sequential([
    base_model,
    Flatten(),
    Dense(1, activation='sigmoid')  # Saída para classificação binária
])

model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

# Treinamento do modelo
model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=epochs
)

# Salvar o modelo
model.save('modelo_reconhecimento_maca.h5')

# Função para verificar se a imagem é uma maçã
def verificar_maca(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (img_width, img_height))
    img = np.expand_dims(img, axis=0) / 255.0

    prediction = model.predict(img)
    return 'maçã' if prediction[0][0] >= 0.5 else 'não maçã'

# Exemplo de uso
resultado = verificar_maca('teste/teste.jpg')
print(f'A imagem é: {resultado}')
