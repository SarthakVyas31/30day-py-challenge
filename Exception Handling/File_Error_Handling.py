def Number_file(filename):
    try:
        with open("Number.txt","r") as file:
            number_list=[]
            for line_number, line in enumerate(file,start=1):
                line=line.strip()
                try:
                    number = float(line)
                    number_list.append(number)
                except ValueError as e:
                    print(f"Error: line {line_number} is not a valid number : {line}")
            print("Numbers: ", number_list)
        return number_list
    except FileNotFoundError as e:
        print(f"Error: File {filename} not found")
    except Exception as e :
        print("Error : Errortype-> ", type(e).__name__)
    
Number_file("Number.txt")
