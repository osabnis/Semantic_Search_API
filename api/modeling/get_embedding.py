from laserembeddings import Laser

path_to_encoder = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\bilstm.93langs.2018-12-26.pt"
path_to_codes = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\93langs.fcodes"
path_to_vocab = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\93langs.fvocab"

model = Laser(encoder=path_to_encoder,
              bpe_vocab=path_to_vocab,
              bpe_codes=path_to_codes)


def generate_embedding(sentence, language):
    language = language.lower()
    if language == "english":
        language = "en"
    elif language == "spanish":
        language = "es"
    elif language == "hindi":
        language = "hi"
        print(language)
    else:
        return "Language Not Supported!"
    embedding = model.embed_sentences(sentences=[sentence], lang=[language])
    embedding_string = "["
    for i in range(len(embedding[0])):
        if i != len(embedding[0])-1:
            embedding_string = embedding_string + str(embedding[0][i]) + ", "
        else:
            embedding_string = embedding_string + str(embedding[0][i]) + "]"
    return embedding_string
