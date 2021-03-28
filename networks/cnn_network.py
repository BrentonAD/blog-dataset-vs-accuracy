from numpy import mean
from numpy import std
from sklearn.model_selection import KFold
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
import warnings


warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)

class CnnNetwork():

	# define cnn model
	def define_model(self):
		model = Sequential()
		model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
		model.add(MaxPooling2D((2, 2)))
		model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
		model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
		model.add(MaxPooling2D((2, 2)))
		model.add(Flatten())
		model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
		model.add(Dense(10, activation='softmax'))
		# compile model
		opt = SGD(lr=0.01, momentum=0.9)
		model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
		return model
