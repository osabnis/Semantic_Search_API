from fastapi import APIRouter
from api.app.modeling.model_parameters import model_initialization
from api.app.modeling.get_embedding import generate_embedding
from api.app.modeling.similarity_score import embedding_generator_transformers, embedding_generator_laser, similarity_score
from api.app.modeling.generate_semantic_index import semantic_index
from api.app.modeling.query_results import find_similar_sentences

router = APIRouter(tags=['Modeling'])


# @router.get("/modeling/model_parameters", description="Returns the model parameters!")
# def model_parameters(model_name: str):
#     config = model_initialization(model_name=model_name)
#     return config
#
#
# @router.get("/modeling/get_embedding", description="Gets the language-agnostic embedding for a given sentence!")
# def get_embedding(text: str, language: str):
#     result = generate_embedding(sentence=text, language=language)
#     return result
#
#
# @router.get("/modeling/create_semantic_index", description="Creates the semantic index from the content!")
# def create_semantic_index(dataset_id: str):
#     result = semantic_index(dataset_id=dataset_id)
#     return result
#
#
# @router.post("/modeling/train", description="Starts the fine-tuning on the pretrained model!")
# def train():
#     return {"Training Endpoint": "Not Ready"}
#

@router.get("/modeling/query", description="Run a query on the trained model!")
def query_result(query: str, dataset_id: str):
    result = find_similar_sentences(query=query, dataset_id=dataset_id)
    return result

#
# @router.get("/modeling/check_similarity", description="Compares 2 sentences for similarity!")
# def similarity(query1: str, lang1: str, query2: str, lang2: str):
#     em1 = embedding_generator_laser(sentence1=query1, lang1=lang1, sentence2=query2, lang2=lang2)
#     em2 = embedding_generator_transformers(sentence1=query1, sentence2=query2)
#     cosine1, euclidean1 = similarity_score(em1)
#     cosine2, euclidean2 = similarity_score(em2)
#     return {"Cosine Similarity Score - LASER": cosine1,
#             "Euclidean Distance Score - LASER": euclidean1,
#             "Cosine Similarity Score - Transformers": cosine2,
#             "Euclidean Distance Score - Transformers": euclidean2}
