import argparse
from openai import OpenAI
from tqdm import tqdm
from datetime import datetime
import os


class Rindoku:

    def __init__(self):
        print("Rindoku CLI INIT")
        args = Rindoku.get_args()
        self.prompt_str = Rindoku.read_prompt(args.prompt)
        self.model = args.model
        self.input = args.input

    def get_args():
        print("Rindoku CLI GET_ARGS")
        parser = argparse.ArgumentParser(description="Rindoku CLI")
        parser.add_argument("input", type=str, help="Input text")
        parser.add_argument(
            "-m", "--model", type=str, default="gpt-4o", help="Model name"
        )
        parser.add_argument(
            "-p", "--prompt", type=str, default="prompt.txt", help="Prompt file path"
        )
        return parser.parse_args()

    def read_prompt(prompt_path):
        # read the prompt file
        print("Rindoku CLI READ_PROMPT")
        try:
            with open(prompt_path, "r", encoding="utf-8") as file:
                file_content = file.read()
        except Exception as e:
            print(
                f"Error reading the prompt file: {e}\nCreate an original prompt and set it in the `prompt.txt` file."
            )
            exit(1)
        return file_content

    def save_string_to_file(output_string):
        folder_name = "output"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{folder_name}/{current_time}.txt"

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(output_string)

    def run(self):
        print("Rindoku CLI RUN")
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print(
                "Error: OPENAI_API_KEY is not set in the environment variables.\nCreate an API key and set it in the `.env` file that references `.env.example`."
            )
            exit(1)

        client = OpenAI(api_key=api_key)
        print("Rindoku CLI create")
        completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": self.prompt_str,
                },
                {"role": "user", "content": self.input},
            ],
        )

        print(completion.choices[0].message.content)
        Rindoku.save_string_to_file(completion.choices[0].message.content)


rindoku = Rindoku()
rindoku.run()
