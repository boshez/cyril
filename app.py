import os
from textgenrnn import textgenrnn

DIR = os.path.dirname(os.path.abspath(__file__))

textgen = textgenrnn()

textgen.train_from_file(DIR+'/text-new.txt', num_epochs=1)

textgen.save(DIR+'/cyril_trained_network.hdf5')

textgen.generate()