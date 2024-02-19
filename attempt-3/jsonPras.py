import json

business_names = []

# Read the JSON data from the file in the program directory
file_path = 'f.txt'
with open(file_path, 'r') as file:
        # Load the JSON data
        json_data = file.read()[0]

        # Print the raw JSON data
        
        json_data = json_data.lstrip(")]}'")

        # Print the cleaned JSON data
        print("\nCleaned JSON Data:")
        print(json_data)
        json_data = json_data.lstrip(")]}'")

        # Parse the JSON data
        data = json.loads(json_data[0][0][0])

        # Print intermediate results
        print("\nIntermediate Data:")
        print(data)

        # Access the relevant part of the JSON structure
        business_data = data[0][1][0][14]

        # Print intermediate results
        print("\nBusiness Data:")
        print(business_data)

        # Extract business names from the nested list
        business_names.extend([business_info[0] for business_info in business_data if business_info and business_info[0]])

    

# Print the extracted business names
print("\nExtracted Business Names:")
print(business_names)
