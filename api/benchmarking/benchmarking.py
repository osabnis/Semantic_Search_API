import pandas as pd
from scipy import spatial
from laserembeddings import Laser
from transformers import AutoTokenizer, AutoModel
import torch
import json
import numpy as np


path_to_encoder = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\bilstm.93langs.2018-12-26.pt"
path_to_codes = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\93langs.fcodes"
path_to_vocab = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\93langs.fvocab"

path_to_english = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\benchmarking\\true_annotations\\english_true_annotations_annotations.csv"
path_to_hindi = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\benchmarking\\true_annotations\\hindi_true_annotations_annotations.csv"
path_to_spanish = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\benchmarking\\true_annotations\\spanish_true_annotations_annotations.csv"

model = Laser(encoder=path_to_encoder,
              bpe_vocab=path_to_vocab,
              bpe_codes=path_to_codes)


def top_k_accuracy_score(true_labels, pred_labels):
    good_count, total_count = 0, 0
    for i in range(len(true_labels)):
        if pred_labels[i] in true_labels[i]:
            good_count += 1
            total_count += 1
        else:
            total_count += 1
    accuracy_score = good_count / total_count
    return accuracy_score


def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def annotator_function(path_to_csv, language, dataset_id):
    language = language.lower()
    if language == "english":
        language = "en"
    elif language == "spanish":
        language = "es"
    elif language == "hindi":
        language = "hi"
    else:
        return "Language Not Supported!"
    df_given = pd.read_csv(path_to_csv)
    df = pd.DataFrame({'text': df_given['grouped']})
    df_explode = df.assign(text=df.text.str.split(",")).explode('text')

    score = {}
    queries, url1, url2, url3, url4, url5 = [], [], [], [], [], []
    folder = r"D:\USC Academics\Semester 2\Natural Language Processing\Project\api\data" + r"\\" + dataset_id
    file = folder + "\\index.json"
    with open(file, 'r') as f:
        data = json.load(f)
    for query in df_explode['text'].values:
        queries.append(query)
        query_embedding = model.embed_sentences(sentences=[query], lang=[language])
        for key, value in data.items():
            score[key.strip()] = 1 - spatial.distance.cosine(value, query_embedding)
        sorted_scores = sorted(score.items(), key=lambda x: x[1], reverse=True)
        url1.append(sorted_scores[0][0].split("======>")[1].strip())
        url2.append(sorted_scores[1][0].split("======>")[1].strip())
        url3.append(sorted_scores[2][0].split("======>")[1].strip())
        url4.append(sorted_scores[3][0].split("======>")[1].strip())
        url5.append(sorted_scores[4][0].split("======>")[1].strip())
    benchmark_dict = {'Query': queries, 'url1': url1, 'url2': url2, 'url3': url3, 'url4': url4, 'url5': url5}
    benchmark_df = pd.DataFrame(benchmark_dict)
    return benchmark_df


def benchmarking(dataset_id, language):
    language = language.lower()
    if language == "english":
        language = "en"
    elif language == "spanish":
        language = "es"
    elif language == "hindi":
        language = "hi"
    else:
        return "Language Not Supported!"
    score = {}
    path_to_dataset = path_to_english if language == "en" else path_to_spanish if language == "es" else path_to_hindi
    df = pd.read_csv(path_to_dataset)
    queries = df['group_list'].values
    true_labels = df[['url1', 'url2', 'url3']].values.tolist()
    pred_labels = []
    folder = r"D:\USC Academics\Semester 2\Natural Language Processing\Project\api\data" + r"\\" + dataset_id
    file = folder + "\\index.json"
    with open(file, 'r') as f:
        data = json.load(f)
    for query in queries:
        query_embedding = model.embed_sentences(sentences=[query], lang=["en"])
        for key, value in data.items():
            score[key.strip()] = 1 - spatial.distance.cosine(value, query_embedding)
        sorted_scores = sorted(score.items(), key=lambda x: x[1], reverse=True)
        label = sorted_scores[0][0].split("======>")[1].strip()
        pred_labels.append(label)
    pred_labels = np.array(pred_labels)
    true_labels = np.array(true_labels)
    print("Pred_Labels_Shape = ", pred_labels.shape)
    print("True Labels Shape = ", true_labels.shape)
    accuracy_score = top_k_accuracy_score(true_labels=true_labels, pred_labels=pred_labels)
    return accuracy_score


def benchmarking_others(dataset_id, language):
    tokenizer = AutoTokenizer.from_pretrained('hiiamsid/sentence_similarity_hindi')
    model = AutoModel.from_pretrained('hiiamsid/sentence_similarity_hindi')
    language = language.lower()
    if language == "english":
        language = "en"
    elif language == "spanish":
        language = "es"
    elif language == "hindi":
        language = "hi"
    else:
        return "Language Not Supported!"
    score = {}
    path_to_dataset = path_to_english if language == "en" else path_to_spanish if language == "es" else path_to_hindi
    df = pd.read_csv(path_to_dataset)
    queries = df['group_list'].values
    true_labels = df[['url1', 'url2', 'url3']].values.tolist()
    pred_labels = []
    folder = r"D:\USC Academics\Semester 2\Natural Language Processing\Project\api\data" + r"\\" + dataset_id
    file = folder + "\\index_model1.json"
    with open(file, 'r') as f:
        data = json.load(f)
    for query in queries:
        encoded_input = tokenizer(query, padding=True, truncation=True, return_tensors='pt')
        with torch.no_grad():
            model_output = model(**encoded_input)
        sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
        for key, value in data.items():
            score[key.strip()] = 1 - spatial.distance.cosine(value, sentence_embeddings)
        sorted_scores = sorted(score.items(), key=lambda x: x[1], reverse=True)
        label = sorted_scores[0][0].split("======>")[1].strip()
        pred_labels.append(label)
    pred_labels = np.array(pred_labels)
    true_labels = np.array(true_labels)
    print("Pred_Labels_Shape = ", pred_labels.shape)
    print("True Labels Shape = ", true_labels.shape)
    accuracy_score = top_k_accuracy_score(true_labels=true_labels, pred_labels=pred_labels)
    return accuracy_score