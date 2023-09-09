from scipy import spatial
from laserembeddings import Laser
from transformers import AutoTokenizer, AutoModel
import torch


def embedding_generator_laser(sentence1, lang1, sentence2, lang2):
    path_to_encoder = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\bilstm.93langs.2018-12-26.pt"
    path_to_codes = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\93langs.fcodes"
    path_to_vocab = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\93langs.fvocab"
    model = Laser(encoder=path_to_encoder,
                  bpe_vocab=path_to_vocab,
                  bpe_codes=path_to_codes)
    sentence1, sentence2 = sentence1.lower(), sentence2.lower()
    lang1, lang2 = lang1.lower(), lang2.lower()
    if lang1 == "english":
        lang1 = "en"
    elif lang1 == "spanish":
        lang1 = "es"
    elif lang1 == "hindi":
        lang1 = "hi"
    else:
        return "Language 1 Not Supported!"

    if lang2 == "english":
        lang2 = "en"
    elif lang2 == "spanish":
        lang2 = "es"
    elif lang2 == "hindi":
        lang2 = "hi"
    else:
        return "Language 2 Not Supported!"

    embeddings = model.embed_sentences(sentences=[sentence1, sentence2], lang=[lang1, lang2])

    return embeddings


def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def embedding_generator_transformers(sentence1, sentence2):
    sentence1, sentence2 = sentence1.lower(), sentence2.lower()

    sentences = [sentence1, sentence2]
    tokenizer = AutoTokenizer.from_pretrained('AIDA-UPM/mstsb-paraphrase-multilingual-mpnet-base-v2')
    model = AutoModel.from_pretrained('AIDA-UPM/mstsb-paraphrase-multilingual-mpnet-base-v2')

    encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

    with torch.no_grad():
        model_output = model(**encoded_input)
    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
    return sentence_embeddings


def similarity_score(embeddings_array):
    cosine = 1 - spatial.distance.cosine(embeddings_array[0], embeddings_array[1])
    euclidean = spatial.distance.euclidean(embeddings_array[0], embeddings_array[1])
    return cosine, euclidean



