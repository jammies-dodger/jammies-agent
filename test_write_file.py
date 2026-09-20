from calculator.functions.write_file import write_file

lorem_test = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
morelorem_test = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
tmp_test = write_file("calculator", "/tmp/temp.text", "this should not be allowed")

print(lorem_test, morelorem_test, tmp_test)