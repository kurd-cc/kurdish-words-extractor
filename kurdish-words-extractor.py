import re
import argparse


parser = argparse.ArgumentParser(description='Extract Kurdish (Kurmanji) letters from a text or a file')
parser.add_argument('-t','--text', dest='text', type=str, help='The text to extract the words from')
parser.add_argument('-d', '--delimiter', dest='delimiter', type=str, help='The delimiter to divide between extracted words, default is a new line')
parser.add_argument('-f', '--file', dest='file', type=str, help='The file path to extract words from its text')
parser.add_argument('-o', '--output', dest='output', type=str, help='The output file, if you want to save the results')
args = parser.parse_args()


def split_text(text, delimiter="\n"):
    kurdish_letters = "ABCÇDEÊFGHIÎJKLMNOPQRSŞTUÛVWXYZabcçdeêfghiîjklmnopqrsştuûvwxyz"
    reg = "[^"+kurdish_letters+"]+"
    text = re.sub(reg, '*', text).rstrip()
    return delimiter.join(text.split('*'))


def save_to_file(text, file_path):
    f = open(file_path, "w", encoding="utf-8")
    f.write(text)
    f.close()


def read_from_file(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    result = f.read()
    f.close()
    return result


if __name__ == "__main__":
    delimiter = '\n'
    if args.delimiter is not None:
        delimiter = args.delimiter

    if args.text is not None and args.file is not None:
        print("You should only choose one option, text or file")

    elif args.text is not None and args.output is None:
        print(split_text(args.text, delimiter))

    elif args.text is not None and args.output is not None:
        try:
            save_to_file(split_text(args.text, delimiter), args.output)
            print("Success: results saved to " + args.output + "\n")
        except Exception as ex:
            print(ex)

    elif args.file is not None and args.output is None:
        print(split_text(read_from_file(args.file), delimiter))

    elif args.file is not None and args.output is not None:
        try:
            save_to_file(split_text(read_from_file(args.file), delimiter), args.output)
            print("Success: results saved to " + args.output + "\n")
        except Exception as ex:
            print(ex)

    else:
        print("You didn't entered the requested arguments, run 'python kurdish-words-extractor.py -h' for more details")
