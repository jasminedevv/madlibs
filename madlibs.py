import re

# story looks like a list of strings and tuples where the tuple is formatted like ("type", "example")
# mostly just using tuples for clarity (could use lists or dicts)
my_story = [
("exclamation", "Yikes"),
"! he said",
("adverb", "whistfully"),
"as he jumped into his convertible",
("noun", "catbus"),
"and drove off with his",
("adjective", "beautiful"),
"wife."
]

# takes a prompt and then asks the user for a word
def get_new_word(type):
    prompt = type + " > "
    the_new_term = input(prompt)
    return the_new_term

# loops trough the formatted story list and asks the user for a list of words
def run_story(raw_story):
    index = 0
    for item in raw_story:
        if type(item) is tuple:
            # if item is changeable
            the_new_term = get_new_word(item[0])
            raw_story[index] = (item[0], the_new_term)
        index += 1
    return raw_story

# converts a story in the above format to a text story format
def convert_story_to_text(raw_story):
    text = ""
    for item in raw_story:
        if type(item) is tuple:
            # item is changeable
            text = text + " " + item[1]
        else:
            # item is just a string
            text = text + " " + item
    # I borrowed this regular expression from stack overflow https://stackoverflow.com/questions/15950672/join-split-words-and-punctuation-with-punctuation-in-the-right-place
    text = re.sub(r' (?=\W)', '', text)
    return text

def main():
    story = run_story(my_story)
    print(convert_story_to_text(story))

def test():
    new_word = get_new_word("noun")
    print(new_word) # I should look like ('type', 'word')
    print(my_story)
    story = run_story(my_story)
    print(convert_story_to_text(story))
    print(convert_story_to_text(my_story))

# test()
main()
