import json
import base64

# Open and encode the image
with open('utils/test-receipt.jpg', 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# Create the JSON structure
data = {
    "input": {
        "image_base64": encoded_string
    }
}

# Write to a JSON file
with open('src/test_input.json', 'w') as json_file:
    json.dump(data, json_file)

print("JSON file created successfully.")