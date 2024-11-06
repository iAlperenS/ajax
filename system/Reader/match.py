class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def parse(self):
        return self.expr()
    
    def expr(self):
        result = self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('PLUS', 'MINUS'):
            if self.tokens[self.pos][0] == 'PLUS':
                self.pos += 1
                result += self.term()
            elif self.tokens[self.pos][0] == 'MINUS':
                self.pos += 1
                result -= self.term()
        return result
    
    def term(self):
        result = self.factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('MULTIPLY', 'DIVIDE'):
            if self.tokens[self.pos][0] == 'MULTIPLY':
                self.pos += 1
                result *= self.factor()
            elif self.tokens[self.pos][0] == 'DIVIDE':
                self.pos += 1
                result /= self.factor()
        return result
    
    def factor(self):
        if self.tokens[self.pos][0] == 'NUMBER':
            value = int(self.tokens[self.pos][1])
            self.pos += 1
            return value
        elif self.tokens[self.pos][0] == 'LPAREN':
            self.pos += 1
            result = self.expr()
            self.pos += 1  # RPAREN'i atla
            return result

tokens = lexer("(3 + 5) * 2")
parser = Parser(tokens)
result = parser.parse()
print(result)
