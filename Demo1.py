print("Hello")
#print multiline string,indentation not important for string in tripple quote
print("""Multiline1
 Multiline 2
 Multiline3""")
print("Run a python file: pytest <x.py>")
print("Run a test in python file: pytest <x.py>::<testFunctionName>")
print("Run a test in python file with tag: pytest -m <tag>")
print("Run a test in python file with tag: pytest -m smoke")
print("Run a test in python file with multiple tag: pytest -m smoke or regression")

print("""install playwright: 1. pip install pytest-playwright
2. pip install playwright
""")
print("""Run playwright test in heahed mode pytest <x.py>::<testName> --headed""")