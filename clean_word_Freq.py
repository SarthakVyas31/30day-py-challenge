def count_word_frequencies(file_path: str): 
# Reads a text file and counts the frequency of each word     
    word_frequency = {}

    try:
        #opening file in read mode
        with open(file_path,"r") as file:
            content = file.read().lower() # text converted into lowercase for unifromity 
        
        words = content.split() # split text into words

        #counts the frequency of each word
        for word in words:
            if word in word_frequency:
                word_frequency[word]+=1
            else:
                word_frequency[word] = 1

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return word_frequency

#Displays the word frequencies
def display_frequencies(frequency_dict: dict):

    if not frequency_dict:
        print("No word frequencies to display.")
        return 
    
    print("Frequencies of words in the file: \n")
    for word, count in frequency_dict.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    file_path = "data.txt"
    frequencies = count_word_frequencies(file_path)
    display_frequencies(frequencies)