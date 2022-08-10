import tensorflow as tf  
from keras.preprocessing.image import ImageDataGenerator  

train_datagen = ImageDataGenerator(rescale = 1./255,  
                                   shear_range = 0.2,  
                                   zoom_range = 0.2,  
                                   horizontal_flip = True) 


training_set = train_datagen.flow_from_directory('./training_set',  
                                                 target_size = (64, 64),  
                                                 batch_size = 16,  
                                                 class_mode = 'binary')

test_datagen = ImageDataGenerator(rescale = 1./255) 

test_set = test_datagen.flow_from_directory('./test_set',  
                                            target_size = (64, 64),  
                                            batch_size = 16,  
                                            class_mode = 'binary')

#Building Model

cnn = tf.keras.models.Sequential()

#convolution layer1
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))

#pooling layer1
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

#convolution layer2
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))

#pooling layer2
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

#flattenning
cnn.add(tf.keras.layers.Flatten())

#first ANN layer
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))

#second ANN layer
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))

#third ANN layer
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))

#fourth ANN layer
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))

#output layer
cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

#model compiling
cnn.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#training model
#cnn.fit( training_set, validation_data = test_set, epochs = 10)
cnn.fit( training_set, validation_data = test_set, epochs = 10,steps_per_epoch=500, validation_steps=800)

#saving model
cnn.save("cat-dog-final.h5")
