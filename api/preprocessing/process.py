import os
from glob import glob


def process(dataset_id):
    try:
        folder = r"D:\USC Academics\Semester 2\Natural Language Processing\Project\api\data" + r"\\" + dataset_id
        file_folder = folder + "\\flat_files"
        os.chdir(file_folder)
        content = ""
        for file in glob("*.txt"):
            with open(file, 'r', encoding='utf-8') as f:
                if os.stat(file).st_size != 0:
                    content += f.read()
        full_text_loc = folder + "\\full_text.txt"
        with open(full_text_loc, "w", encoding='utf-8') as f:
            f.write(content)
        return "Files have been processed!"
    except Exception as e:
        return "There is an issue = " + str(e)
