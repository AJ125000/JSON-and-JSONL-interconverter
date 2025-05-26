import jsonlines
import json
def json_to_jsonline(input_file, output_file):

    with jsonlines.open(output_file, mode='w') as writer:
        with open(input_file, 'r', encoding='utf-8') as reader:
            for line in reader:
                data = json.loads(line)
                writer.write(data)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert JSON file to JSON Lines format.")
    parser.add_argument("input_file", type=str, help="Path to the input JSON file.")
    parser.add_argument("output_file", type=str, help="Path to the output JSON Lines file.")

    args = parser.parse_args()

    json_to_jsonline(args.input_file, args.output_file) 