from datetime import datetime


def create_timestamp_file():
    # Get current timestamp
    current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create file name with current timestamp
    file_name = f"{current_timestamp}.txt"
    
    # Write content into the file
    with open(file_name, 'w') as file:
        file.write(current_timestamp)
    
    print(f"File '{file_name}' created successfully.")

# Call the function to create the timestamp file
create_timestamp_file()


def read_tex(file_name):
    with open(file_name,'r') as file:
        contend=file.read()
        print(contend)

read_tex("guvi.txt")

        