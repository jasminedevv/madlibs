import re
# MVP
# ask the user for the terms
# put the terms into a list
# put the list items into the story slots

# what does text look like?
# for now it looks like a list of strings and tuples where the tuple is ("type", "example")
# mostly just using tuples for clarity

my_story = [
("exclamation", "Yikes"),
"! he said",
("adverb", "whistfully"),
"as he jumped into his convertible",
("noun", "catbus"),
"and drove off with his",
("adjective", "beautiful"),
"wife"
]

def convert_story_to_text(raw_story):
    text = ""
    for item in raw_story:
        if type(item) is tuple:
            # item is changeable
            text = " " + text + item[1] + " "
        else:
            # item is just a string
            text = " " + text + " " + item + " "
    # I borrowed this regular expression from stack overflow https://stackoverflow.com/questions/15950672/join-split-words-and-punctuation-with-punctuation-in-the-right-place
    text = re.sub(r' (?=\W)', '', text)
    return text

def get_new_word(type):
    prompt = type + " > "
    the_new_term = input(prompt)
    # the_new_tuple = (type, the_new_term)
    return the_new_term

def run_story(raw_story):
    index = 0
    for item in raw_story:
        if type(item) is tuple:
            # if item is changeable
            the_new_term = get_new_word(item[0])
            raw_story[index] = (item[0], the_new_term)
        index += 1
    return raw_story

def test():
    # new_word = get_new_word("noun")
    # print(new_word) # I should look like ('type', 'word')
    # print(my_story)
    story = run_story(my_story)
    print(convert_story_to_text(story))
    # print(convert_story_to_text(my_story))

test()
