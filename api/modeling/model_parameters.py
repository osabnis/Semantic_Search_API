from transformers import BertModel, BertConfig, BertTokenizer


def model_initialization(model_name):
    model = BertModel.from_pretrained(model_name)
    # tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")
    config = model.config
    return config
