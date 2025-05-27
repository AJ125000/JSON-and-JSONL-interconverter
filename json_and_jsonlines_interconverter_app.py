import streamlit as st
import json

st.set_page_config(page_title="JSON ⇄ JSONL Converter", layout="centered")
st.title("🔁 JSON ⇄ JSONL Converter")

# Ask user for conversion direction
conversion_choice = st.radio("Choose Conversion Direction:", ("JSON ➡ JSONL", "JSONL ➡ JSON"))

# Upload file
uploaded_file = st.file_uploader("Upload your file", type=["json", "jsonl", "txt"])

def convert_json_to_jsonl(file_bytes):
    try:
        text = file_bytes.decode("utf-8")
        data = json.loads(text)  # ✅ Read the entire JSON content

        result = []
        if isinstance(data, list):
            for obj in data:
                result.append(json.dumps(obj, ensure_ascii=False))
        else:
            result.append(json.dumps(data, ensure_ascii=False))

        output = "\n".join(result)
        return output.encode("utf-8")

    except Exception as e:
        st.error(f"Error during conversion: {e}")
        return None

def convert_jsonl_to_json(file_bytes):
    try:
        text = file_bytes.decode("utf-8")
        lines = text.strip().splitlines()
        result = []

        for line in lines:
            obj = json.loads(line)
            result.append(obj)

        output = json.dumps(result, ensure_ascii=False, indent=2)
        return output.encode("utf-8")

    except Exception as e:
        st.error(f"Error during conversion: {e}")
        return None

# Perform conversion and show download button
if uploaded_file:
    file_bytes = uploaded_file.read()

    if conversion_choice == "JSON ➡ JSONL":
        converted = convert_json_to_jsonl(file_bytes)
        filename = "converted.jsonl"
        mime = "application/jsonl"
    else:
        converted = convert_jsonl_to_json(file_bytes)
        filename = "converted.json"
        mime = "application/json"

    if converted:
        st.success("✅ Conversion successful!")
        st.download_button("📥 Download Converted File", converted, file_name=filename, mime=mime)
