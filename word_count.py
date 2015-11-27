import os
import csv
import sys

from chatterbot.twitter_api import clean
from pygal import Line


def word_count(text_sample_directory):

    print "Opening '" + text_sample_directory + "'"

    # Dictionary of each word that gets encountered
    words = {}

    for text_file in os.listdir(text_sample_directory):
        with open(text_sample_directory + text_file) as f:
            sys.stdout.write(".")
            sys.stdout.flush()

            for line in f:

                line = line.lower()
                line = clean(line)

                replace_characters = '0123456789~-+=!?@#$%^&*:;<>(){}[]|\/\'`"_,.'
                for character in replace_characters:
                    line = line.replace(character, "")

                word_list = line.split(" ")
                for word in word_list:

                    if word and word in words:
                        words[word] += 1
                    else:
                        words[word] = 1

    output_name = text_sample_directory.strip("/")

    writer = csv.writer(open(output_name + ".csv", "wb"))
    sorted_dict = sorted(words.items(), key=lambda x:x[1], reverse=True)

    # Get the count of occurance for the word that occurs the most
    max_value = int(sorted_dict[0][1])
    keys = []
    values = []

    for key, value in sorted_dict:
        keys.append(key)
        values.append(value)
        writer.writerow([key, value])

    line_chart = Line()
    line_chart.title = "Word Occurance Graph"
    line_chart.x_labels = keys
    line_chart.add(output_name,  values)

    svg_data = line_chart.render()
    graphfile = open(output_name + ".svg", "w")
    graphfile.write(svg_data)


    print "\nWriting '" + output_name + "'"


# Run the method on the following sample directories
word_count("data/english/")
word_count("data/spanish/")
