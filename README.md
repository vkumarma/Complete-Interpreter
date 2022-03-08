# Complete-Interpreter
Interpreter for a simple imperative programming language

Scanner Specification There are four types of tokens in our language, defined by the following regular
expressions.

      IDENIFIER = ([a-z] | [A-Z])([a-z] | [A-Z] | [0-9])*
      NUMBER = [0-9]+
      SYMBOL = \+ | \- | \* | / | \( | \) | := | ;
      KEYWORD = if | then | else | endif | while | do
      | endwhile | skip
      
      The following rules define how separation between tokens should be handled.
      • White space1 is not allowed in any token, so white space always terminates a token and separates it
      from the next token. Except for indicating token boundaries, white space is ignored.
      • The principle of longest substring should always apply.
      • Any character that does not fit the pattern for the token type currently being scanned immediately
      terminates the current token and begins the next token. The exception is white space, in which case
      the first rule applies.
      
Parser Specification Grammar of Limp is defined as follows:

      statement ::= basestatement { ; basestatement }
      basestatement ::= assignment | ifstatement | whilestatement | skip
      assignmet ::= IDENTIFIER := expression
      ifstatement ::= if expression then statement else statement endif
      whilestatement ::= while expression do statement endwhile
      expression ::= term { + term }
      term ::= factor { - factor }
      factor ::= piece { / piece }
      piece ::= element { * element }
      element ::= ( expression ) | NUMBER | IDENTIFIER
      
Note that statement is the starting nonterminal.
