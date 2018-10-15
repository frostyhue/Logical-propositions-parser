from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from classes.Interpreter import *
from django.views.generic import *


class ToolView(TemplateView):
    template_name = 'index.html'


def index(request):
    return render(request, 'index.html')

def convert(request, expr):
    lexer_boolean = Lexer(expr)
    parser_boolean = ParserBoolExpr(lexer_boolean)
    interpreter_boolean = Interpreter(parser_boolean)
    result_boolean = interpreter_boolean.interpret()

    lexer_infix = Lexer(expr)
    parser_infix = ParserInfix(lexer_infix)
    interpreter_infix = Interpreter(parser_infix)
    result_infix = interpreter_infix.interpret()

def tests(request):
    return render(request, 'tests.html')