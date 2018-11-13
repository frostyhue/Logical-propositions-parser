# The libraries that are used for the engine of the application.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from tool.classes.Interpreter import *
from tool.classes.SimplifiedTT import *
from django.views.generic import *
from tool.classes.TreeVisualizer import *
from django.shortcuts import *
import os

# Function used by the url file to redirect to the index's page.
def main(request):
    return render(request, 'Main.html')


# Function used by the url file to redirect to the index's page.
def tool(request):
    if os.path.exists("static/images/output.dot"):
        os.remove("static/images/output.dot")

    if os.path.exists("static/images/tree.png"):
        os.remove("static/images/tree.png")

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

        # Create the lexer, parser, interpreter of the infix expression and assign the result to a variable.
        lexer_infix = Lexer(expr)
        parser_infix = ParserInfix(lexer_infix)
        interpreter_infix = Interpreter(parser_infix)
        result_infix = interpreter_infix.interpret()

        # Generate graph
        viz = TreeVisualizer(parser_infix)
        content = viz.gendot()
        image_name = 'tree.png'
        image_parth = 'images/{name}'.format(name=image_name)
        with open("static/images/output.dot", "w+") as fh:
            fh.write(content)
        os.chmod("static/images/output.dot", 0o777)
        os.system("dot -Tpng -o static/images/tree.png static/images/output.dot")

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

        # Get the value of the normalization for the truth table.
        tt_dnf = tt.dnf()

        # Get the value of the normalization for the simplified truth table.
        stt_dnf = stt.dnf()

        # Populate the context that will be passed to the index.html page,
        context = {
            'bin': bin,
            'hex': hex.upper(),
            'input': expr,
            'expr': result_infix,
            'expr_bool': result_boolean,
            'pred_list': predicates_list,
            'TruthTable': tt.truth_table,
            'SimplifiedTT': stt.simplified_table,
            'image_path': image_parth,
            'tt_dnf': tt_dnf,
            'stt_dnf': stt_dnf
        }

        # Returns the rendered request, destination page and the context data that we want to pass to the page.
        return render(request, 'index.html', context)

# Function used by the url file to redirect to the tests's page.
def tests(request):
    return render(request, 'tests.html')