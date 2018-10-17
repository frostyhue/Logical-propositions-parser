# The libraries that are used for the engine of the application.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from tool.classes.Interpreter import *
from tool.classes.SimplifiedTT import *
from django.views.generic import *
from django.shortcuts import *


# Function used by the url file to redirect to the index's page.
def index(request):
    return render(request, 'index.html')


def convert(request):

    # Assign the expression to variables
    expr = request.POST.get('expr', None)

    # Check if the request method is of type POST
    if request.method == 'POST':

        # Create the lexer, parser, interpreter of the boolean expression and assign the result to a variable.
        lexer_boolean = Lexer(expr)
        parser_boolean = ParserBoolExpr(lexer_boolean)
        interpreter_boolean = Interpreter(parser_boolean)
        result_boolean = interpreter_boolean.interpret()

        # reate the lexer, parser, interpreter of the infix expression and assign the result to a variable.
        lexer_infix = Lexer(expr)
        parser_infix = ParserInfix(lexer_infix)
        interpreter_infix = Interpreter(parser_infix)
        result_infix = interpreter_infix.interpret()

        # Create a list of predicates to add the expression in infix notation.
        predicates_list = []
        for predicate in parser_infix.sorted_pred_list():
            predicates_list.append(str(predicate))
        predicates_list.append(result_infix)

        # Creating the truth table out of the boolean expression using python's built in bitwise operators.
        tt = TruthTable(result_boolean)
        tt.populate_tt()

        # Creating the simplified version of the truth table without the rows that have 0s in them.
        stt = SimplifiedTT(tt.exp_pred, tt.truth_table)
        stt.remove_rows_ending_0()
        stt.simplify()

        # Create the variables for the hexadecimal of the expression.
        hex = tt.hex

        # Create the variable for the binary of the expression.
        bin = tt.bin

        # Populate the context that will be passed to the index.html page,
        context = {
            'bin': bin,
            'hex': hex.upper(),
            'input': expr,
            'expr': result_infix,
            'pred_list': predicates_list,
            'TruthTable': tt.truth_table,
            'SimplifiedTT': stt.simplified_table
        }

        # Returns the rendered request, destination page and the context data that we want to pass to the page.
        return render(request, 'index.html', context)

# Function used by the url file to redirect to the tests's page.
def tests(request):
    return render(request, 'tests.html')