from tool.classes.Interpreter import *
from tool.classes.SimplifiedTT import *

def main():
    while True:
        try:
            try:
                text = raw_input("Enter expression for evaluation: ")
            except NameError:  # Python3
                text = input("Enter expression for evaluation: ")
        except EOFError:
            break
        if not text:
            continue

        lexer_boolean = Lexer(text)
        parser_boolean = ParserBoolExpr(lexer_boolean)
        interpreter_boolean = Interpreter(parser_boolean)
        result_boolean = interpreter_boolean.interpret()
        print('Expression in boolean format: ')
        print(result_boolean)
        print('')

        lexer_infix = Lexer(text)
        parser_infix = ParserInfix(lexer_infix)
        interpreter_infix = Interpreter(parser_infix)
        result_infix = interpreter_infix.interpret()
        print('Expression in infix format: ')
        print(result_infix)
        print('')
        print('Predicates list: ')
        predicates_list = []
        predicates = ''
        for predicate in parser_infix.sorted_pred_list():
            predicates_list.append(str(predicate))
            predicates = predicates + ' ' + predicate
        predicates = predicates + ' ' + result_infix
        print(predicates)
        print('')
        print('Truth Table')
        tt = TruthTable(result_boolean)
        tt.populate_tt()
        tt.print_predicates()
        tt.print_tt()
        print('')
        print('Simplified truth table')
        stt = SimplifiedTT(tt.exp_pred, tt.truth_table)
        stt.remove_rows_ending_0()
        stt.simplify()
        stt.print_simplified()



if __name__ == "__main__":
    main()