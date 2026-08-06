import pytest


#call 'browser_name' fixture in conftest
# if we pass in cmd line it will take ow chrome
# pytest .\global_variable.py::test_browser_cmd_line_param --browser firefox
def test_browser_cmd_line_param(page,request):
    print("browser =",request.get_command_line())
    page.goto("https://rahulshettyacademy.com/client")