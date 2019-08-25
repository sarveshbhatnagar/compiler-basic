import copy



### Defining DIGITS
DIGITS = '0123456789'

### Declaring Tokens
TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'TT_MINUS'
TT_MUL = 'TT_MUL'
TT_DIV = 'TT_DIV'
TT_LPAREN = 'TT_LPAREN'
TT_RPAREN = 'TT_RPAREN'

### ERROR class

class Error:
    """docstring for Error."""

    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = "{} : {} ".format(self.error_name,self.details)
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)





#### Token ####
class Token:
    """docstring for Tokens."""

    def __init__(self,type_,value = None):
        self.type = type_
        self.value = value
    def __repr__(self):
        if self.value: return "{} : {}".format(self.type, self.value)# used for representation...
        return "{}".format(self.type)

class Lexer:
    """docstring for Lexer."""

    def __init__(self, text):
        self.text = text
        self.pos = -1 # defines current position
        self.current_char = None # defines current character
        self.advance()#to move ahead...

    def advance(self):
        self.pos += 1 #move ahead.
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None # assign accordingly

    def make_tokens(self):
        tokens = [] # create an empty list of tokens.
        while self.current_char != None:
            print(self.current_char)
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                print("IN DIGIT")
                tokens.append(self.make_number())
            elif self.current_char is '+':
                print("IN PLUS")
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                pos_start = copy.copy(self.pos)
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'") #empty tokens and an illegal character error

        return tokens , None; #normal tokens and no error.

    def make_number(self):
        """
        Make number reads characters and checks if its a . or is in digits, it maintains dot count and number string
        Dot count tells if the number is FLOAT
        num string is used to maintain the number we are reading.
        finally we check dot count and return an int token or a float token as per requirements.
        """
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

### Run

def run(text):
    lexer = Lexer(text)
    tokens ,error= lexer.make_tokens()
    return tokens,error
