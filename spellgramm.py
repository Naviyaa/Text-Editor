import language_check
from spellchecker import SpellChecker

spell = SpellChecker()

file=input("Enter file path: ")
file_name = open(file, 'r')
content = file_name.read()
content_list = content.split()
# find those words that may be misspelled
misspelled = spell.unknown(content_list)

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))

# Mention the language keyword
tool = language_check.LanguageTool('en-US')
i = 0
# Path of file which needs to be checked
with open(file, 'r') as fin:

    for line in fin:
        matches = tool.check(line)
        i = i + len(matches)
        pass

# prints total mistakes which are found
# from the document
print("No. of mistakes found in document is ", i)
print()

for mistake in matches:
    print(mistake)
    print()
