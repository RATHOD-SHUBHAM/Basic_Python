import time

def print_animated_text(text):
    for char in text:
        print(char, end = "", flush=True)
        time.sleep(0.02)


if __name__ == '__main__':
    text = "This repository serves as a template for Python projects, providing a structure and examples to kickstart my development process. This template offers me best practices and common patterns to follow thus saving development time."
    print_animated_text(text)