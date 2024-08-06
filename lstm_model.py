import pickle
import sys
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Temporarily alias 'keras.src.preprocessing' to 'tensorflow.keras.preprocessing'
sys.modules['keras.src.preprocessing'] = sys.modules['tensorflow.keras.preprocessing']

# Load the model
loaded_model = load_model('my_lstm_model.h5')

# Load the tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    loaded_tokenizer = pickle.load(handle)

# Clean up the temporary alias
del sys.modules['keras.src.preprocessing']

# Define the maximum sequence length used during training
max_sequence_length = 100  # Replace with the actual max sequence length used during training
max_sequence_len = 100     # Define this variable if different from max_sequence_length

next_words = 4
def getNextWord(seed_text):
    for _ in range(next_words):
        token_list = loaded_tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = loaded_model.predict(token_list, verbose=0)
        predicted = np.argmax(predicted)
        output_word = ""
        for word, index in loaded_tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

# seed_text = ''
# while True:
#     seed_text = input("Enter a seed text (type 'exit' to quit): ")
#     if seed_text.lower() == 'exit':
#         break
#     next_word = getNextWord(seed_text)
#     print(next_word)
