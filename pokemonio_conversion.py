def process_file(file_path):
    result = []
    
    # Open the file in read mode
    with open(file_path, 'r') as file:
        for line in file:
            # Strip the line to remove extra spaces or newlines
            line = line.strip()
            
            # Split the line by space
            parts = line.split(' ')
            
            name = parts[1]

            # If the card name is longer than 1 word
            name_length = len(parts) - 3
            if name_length > 1:
                for x in range(name_length-1):
                    name = name + " " + parts[x+2]

            # Accounting for strange set code for promo cards
            set_code = parts[len(parts)-2]
            if "-" in set_code:
                result_code = set_code[-2:]+"P"
            else:
                result_code = set_code

            # Making all collection numbers 3 long
            collection_number = parts[len(parts)-1]
            if len(collection_number) == 1:
                result_number = "00" + collection_number
            elif len(collection_number) == 2:
                result_number = "0" + collection_number
            else:
                result_number = collection_number

            record = {
                "amount": parts[0],    # amount of cards
                "name": name,               # card name
                "set": result_code,         # set code
                "col#": result_number   # collection number
            }
            result.append(record)
    
    return result

"""
# Example usage:
file_path = 'cleaned.txt'  # Replace with the path to your text file
data = process_file(file_path)
"""

"""
# Print out the data for verification
for entry in data:
    print(entry)
"""

