from calculator.functions.get_file_content import get_file_content

lorem_test = get_file_content("calculator", "lorem.txt")
main_test = get_file_content("calculator", "main.py")
calculatorpy_test = get_file_content("calculator", "pkg/calculator.py")
cat_test = get_file_content("calculator", "/bin/cat")
does_not_exist_test = get_file_content("calculator", "pkg/does_not_exist.py")

print(f"lorem.txt length: {len(lorem_test)}")
print(f"lorem.txt truncated: {'truncated' in lorem_test}")

print(main_test, calculatorpy_test, cat_test, does_not_exist_test)