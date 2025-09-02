import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfFilReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text

        except Exception as e:
            raise Exception("error reading the PDF file")

    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        raise Exception(
            "unsupported file format only pdf and text file suppoted "
        ) 

def get_table_data(quiz_str):
    try:
        # Handle when quiz_str comes with "### RESPONSE_JSON" prefix
        if isinstance(quiz_str, str):
            quiz_str = quiz_str.strip()
            if quiz_str.startswith("### RESPONSE_JSON"):
                quiz_str = quiz_str.replace("### RESPONSE_JSON", "", 1).strip()
            quiz_dict = json.loads(quiz_str)
        else:
            quiz_dict = quiz_str  # already a dict

        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join(
                [f"{opt}: {opt_val}" for opt, opt_val in value["options"].items()]
            )
            correct_key = value["correct"]
            correct_answer = value["options"].get(correct_key, correct_key)

            quiz_table_data.append(
                {"MCQ": mcq, "Choices": options, "Correct": correct_answer}
            )

        return quiz_table_data

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return None
