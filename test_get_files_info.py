from calculator.functions.get_files_info import get_files_info
test_results = [
    get_files_info("calculator", "."),
    get_files_info("calculator", "pkg"),
    get_files_info("calculator", "/bin"),
    get_files_info("calculator", "../")
]

for result in test_results: print(result)
