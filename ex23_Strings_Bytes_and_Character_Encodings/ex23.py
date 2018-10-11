# use the sys module, because we need its fxn so we can interact with the interpreter
import sys
script, input_encoding, error = sys.argv

# main gets called recursively until the last line is read
# which is an empty string, thus 'falsy' which fails the loop
def main(language_file, encoding, errors):
    line = language_file.readline()

# while line is true, print_line gets called
    if line:

        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
# strip (sans arg) removes trailing whitespace
    next_lang = line.strip()
# Remeber DBES -> Decode Bytes, Encode Strings
# Encode the string to byte code
    raw_bytes = next_lang.encode(encoding, errors=errors)
# Decode the byte code just encoded, i.e. revert it back to a string
    cooked_string = raw_bytes.decode(encoding, errors=errors)

# visually represent the str -> to -> byte encoding
# and byte -> to -> str decoding
    print(raw_bytes, "<===>", cooked_string)

# open the languages.txt file, not sure how the mode arg works
languages = open("languages.txt", encoding="utf-8")

# initial call to main reads each line calls print_line if no-white space
# fails at last line of file, because empty string is falsy.
main(languages, input_encoding, error)
