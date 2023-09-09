from laserembeddings import Laser
from transformers import AutoTokenizer, AutoModel
import torch
import json
import numpy as np

path_to_encoder = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\bilstm.93langs.2018-12-26.pt"
path_to_codes = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\93langs.fcodes"
path_to_vocab = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\93langs.fvocab"

model = Laser(encoder=path_to_encoder,
              bpe_vocab=path_to_vocab,
              bpe_codes=path_to_codes)


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def semantic_index(dataset_id):
    try:
        folder = r"D:\USC Academics\Semester 2\Natural Language Processing\Project\api\data" + r"\\" + dataset_id
        file = folder + "\\full_text.txt"
        with open(file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        embed_dict = {}
        counter = 1
        for text in content:
            text_part = text.split("======>")[0].strip()
            embedding = model.embed_sentences(sentences=[text_part], lang=['en'])
            embed_dict[text] = embedding
            counter += 1
            if counter % 10 == 0:
                print(counter, end=" ")
        json_content = json.dumps(embed_dict, cls=NumpyEncoder)
        jsonfile = folder + "\\index.json"
        with open(jsonfile, "w") as f:
            f.write(json_content)
        return "Semantic Index created!"
    except Exception as e:
        return "There was an issue = " + str(e)


def semantic_index_others(dataset_id):
        tokenizer = AutoTokenizer.from_pretrained('AIDA-UPM/mstsb-paraphrase-multilingual-mpnet-base-v2')
        model = AutoModel.from_pretrained('AIDA-UPM/mstsb-paraphrase-multilingual-mpnet-base-v2')
        try:
            folder = r"D:\USC Academics\Semester 2\Natural Language Processing\Project\api\data" + r"\\" + dataset_id
            file = folder + "\\full_text.txt"
            with open(file, 'r', encoding='utf-8') as f:
                content = f.readlines()
            embed_dict = {}
            counter = 1
            for text in content:
                text_part = text.split("======>")[0].strip()
                encoded_input = tokenizer(text_part, padding=True, truncation=True, return_tensors='pt')
                with torch.no_grad():
                    model_output = model(**encoded_input)
                sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
                embed_dict[text] = sentence_embeddings.tolist()
                counter += 1
                if counter % 10 == 0:
                    print(counter, end=" ")
            json_content = json.dumps(embed_dict, cls=NumpyEncoder)
            jsonfile = folder + "\\index_model1.json"
            with open(jsonfile, "w") as f:
                f.write(json_content)
            return "Semantic Index created!"
        except Exception as e:
            return "There was an issue = " + str(e)
