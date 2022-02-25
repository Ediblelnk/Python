import random
import os

def main(file):
    
    words = ("a about all also and as at be because but by can come could day "
    "do even find first for from get give go have he her here him his how I if "
    "in into it its just know like look make man many me more my new no not now "
    "of on one only or other our out people say see she so some take tell than "
    "that the their them then there these they thing think this those time to "
    "two up use very want way we well what when which who will with would year "
    "you your").split()

    excerpt = ("Text is one of the most widespread forms of sequence data. "
    "It can be understood as either a sequence of characters or "
    "a sequence of words, but it’s most common to work at the "
    "level of words. The deep-learning sequence-processing models "
    "introduced in the following sections can use text to produce "
    "a basic form of natural-l-anguage understanding, sufficient "
    "for applications including document classification, sentiment "
    "analysis, author identification, and even question-answering "
    "(QA) (in a constrained context). Of course, keep in mind "
    "throughout this chapter that none of these deep-learning models "
    "truly understand text in a human sense; rather, these models "
    "can map the statistical structure of written language, which "
    "is sufficient to solve many simple textual tasks. Deep learning "
    "for natural-language processing is pattern recognition applied "
    "to words, sentences, and paragraphs, in much the same way that "
    "computer vision is pattern recognition applied to pixels.")

    # 'r' is open for reading (default)
    with open(file, 'r', encoding='UTF-8') as tfile:
        t = tfile.read()

    # 'b' is binary mode
    with open(file, 'w') as tfile:
        for _ in range(10):
            sample = random.choices(words, k=12)
            tfile.write(" ".join(sample) + "\n")


if __name__ == "__main__":

    main(os.path.join(os.path.dirname(__file__), r"text.txt"))