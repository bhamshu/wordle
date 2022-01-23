from wordle import Wordle

max_tries = 5
default_num_hints = 10

def get_wordle_inputs():
    wordle_word = input("wordle current word: ")
    wordle_colours = input("wordle colour scheme: ")
    wordle_num_hints = int(input(f"wordle num hints [default: {default_num_hints}]: ") or str(default_num_hints))
    
    return wordle_word, wordle_colours, wordle_num_hints

def get_wordle_hints(wordle: Wordle):
    wordle_word, wordle_colours, wordle_num_hints = get_wordle_inputs()
   
    wordle.update(wordle_word, wordle_colours)
    wordle_hints = wordle.get_choices()[:wordle_num_hints]
    
    return wordle_hints

def get_wordle():
    wordle = Wordle()
    for tries in range(max_tries):
        wordle_hints = get_wordle_hints(wordle)
        print(f"Try {tries} hints: {wordle_hints}")

if __name__=='__main__':
    get_wordle()
