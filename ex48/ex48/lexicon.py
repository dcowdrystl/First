
lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'bear': 'noun',
    'princess': 'noun'
 
    
    }

directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat', 'open')
stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')
errors = ('asdfadfasdf', 'ias')
def number_check(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def get_tuple(word):
    test_word = word.lower()
    if test_word in directions:
        return ('direction', word)
    elif test_word in verbs:
        return ('verb', word)
    elif test_word in stop_words:
        return ('stop', word)
    elif test_word in nouns:
        return ('noun', word)
    elif test_word.isdigit():
        return ('number', int(word))
    elif test_word in errors:
        return 'error', word
    else:
        return ('stop', word)

def scan(sentence):
    words = sentence.split()
    return [get_tuple(word) for word in words]