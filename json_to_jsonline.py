import jsonlines
import json

def json_to_jsonline(input_file, output_file):

    with jsonlines.open(output_file, mode='w') as writer:
        with open(input_file, 'r', encoding='utf-8') as reader:
            for line in reader:
                data = json.loads(line)
                writer.write(data)

def jsonline_to_json(input_file, output_file):
    with open(output_file, 'w', encoding='utf-8') as writer:
        with jsonlines.open(input_file, mode='r') as reader:
            for obj in reader:
                writer.write(json.dumps(obj, ensure_ascii=False) + '\n')                

if __name__ == "__main__":

    user_input = input("Do you want to convert JSON to JSON Lines (j) or JSON Lines to JSON (jl)? (j/jl): ").strip().lower()
    if user_input not in ['j', 'jl']:
        print("Invalid input. Please enter 'j' for JSON to JSON Lines or 'jl' for JSON Lines to JSON.")
        exit(1)
    if user_input == 'j':
        input_file = input("Enter the path to the input JSON file: ").strip()
        output_file = input("Enter the path to the output JSON Lines file: ").strip()
        json_to_jsonline(input_file, output_file)
    elif user_input == 'jl':
        input_file = input("Enter the path to the input JSON Lines file: ").strip()
        output_file = input("Enter the path to the output JSON file: ").strip()
        jsonline_to_json(input_file, output_file)    
