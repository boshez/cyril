import os
from textgenrnn import textgenrnn
import markovify

DIR = os.path.dirname(os.path.abspath(__file__))

with open(DIR+'/text-new.txt', 'r') as file:
    data = file.read().replace("\n", " ")
    data = data.split("+-+")

# # blog_post_model = markovify.Text(data)

# # blog_post_model.make_sentence()

# # blog_post_model.make_short_sentence(140)

# textgen = textgenrnn()

# textgen.train_on_texts(data, num_epochs=2)

# textgen.save(DIR+'/cyril_trained_network2.hdf5')

# # textgen.save(DIR+'/cyril_trained_network2.hdf5')

# textgen.load(DIR+'/cyril_trained_network.hdf5')

# textgen.train_from_file(DIR+'/text-new.txt', num_epochs=1)



# textgen.generate(3, temperature=0.7)

textgen = textgenrnn(weights_path=DIR+'/colaboratory_weights.hdf5',
                       vocab_path=DIR+'/colaboratory_vocab.json',
                       config_path=DIR+'/colaboratory_config.json')
                       
# textgen.generate_samples(max_gen_length=1000)

textgen.generate(temperature=0.3, interactive=True, top_n=5)

#textgen.generate_to_file('textgenrnn_texts.txt', max_gen_length=1000)
