
from calculator.functions.run_python_file import run_python_file

main_test = run_python_file("calculator", "main.py")
main1_test = run_python_file("calculator", "main.py", ["3 + 5"])
test = run_python_file("calculator", "tests.py")
mainup_test = run_python_file("calculator", "../main.py")
nofile_test = run_python_file("calculator", "nonexistent.py")
lorem_test = run_python_file("calculator", "lorem.txt")

print(main_test)
print(main1_test)
print(test)
print(mainup_test)
print(nofile_test)
print(lorem_test)