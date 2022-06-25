import os
import re

file_name = "./data/WikiQAQuestionsCorpusAr-En.tsv"
target_dir = "./data/"

arabic_text = []
english_text = []

# the function that to save the data, cleanned_data: the text we cleanned, file_name: the name we want to save
def save_data(cleanned_data, file_name):
    with open(os.path.join(target_dir, file_name), 'w', encoding = "utf-8") as file:
        for item in cleanned_data:
            # save the item line in line
            file.writelines(item)

# this is to get the arabic text file, format: ID <SPACE> Arabic Text
def get_arabic_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for item in file.readlines():
            # strip all the multiple spaces and combine it into one space only
            item = ' '.join(item.split())
            # select the ID of the text
            id = item.split(" ")[0]
            # remove all the English characters along with the special characters, ignore the ID
            arabic_sentences = re.sub(r"[A-Za-z0-9_.!+-=——,$%^，。?、~@#￥%……&*《》<>「」{}【】()/\"\'؟]", "", item.strip(id))
            # append the text line by line
            arabic_text.append(id + " " + arabic_sentences.lstrip() + "\n")
            # save the Arabic text
            save_data(arabic_text, "arabic_text")

# this is to get the english text file, format: ID <SPACE> English Text
def get_english_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for item in file.readlines():
            # strip all the multiple spaces and combine it into one space only
            item = ' '.join(item.split())
            # remove all the arabic characters along with special characters
            english_sentences = re.sub("[\u0621-\u064a#\!\?\,$%^，。?、~@#￥%……&*《》<>「」{}【】()/\"\'؟]+", "", item)
            # append the text line by line
            english_text.append(english_sentences + "\n")
            # save the english_text
            save_data(english_text, "english_text")


if __name__ == "__main__":
    get_arabic_text(file_name)
    get_english_text(file_name)









