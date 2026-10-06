
def main():
    file_name = input("File Name: ")
    while file_name != "":
        try:
            print(f"{file_name} has {get_number_of_lines(file_name)}")
        except FileNotFoundError:
            print("File does not exist")

def get_number_of_lines(file_name):
    in_file = open(file_name, "r")
    line_count = len(in_file.read())
    in_file.close()
    return line_count

main()
