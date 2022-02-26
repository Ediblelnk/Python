#takes a text file input and scrubs it for an email address
import re
import os

email_key = r'([\w\.-]+)@([\w\.-]+)(\.[\w]+)'
sentence_key = r'([\.\?\!])( |\Z|"|\n)'
word_key = r'\b(\w+’*\w*)\b'

with open(os.path.join(os.path.dirname(__file__), r"scrubbed.txt"), encoding='UTF-8') as f:
    text = f.read()
    
    emails = re.finditer(email_key, text)
    if emails:
        print('Emails:', end='    ')
        for email in emails:
            print(email.group(), end='    ')
        print()

    sentences = re.findall(sentence_key, text)
    if sentences:
        print('Total Sentences:', len(sentences))

    words = re.findall(word_key, text)
    if words:
        print('Total Words', len(words))

    print('Average words per sentence:', round(len(words)/len(sentences), 1))