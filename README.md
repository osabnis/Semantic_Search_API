# Semantic Search API
A FastAPI-based Semantic Search API to analyze users' health queries and extract answers from USC's health website!

### Overview:
SEMSE is an innovative application designed to serve as a multi-lingual semantic search engine for websites. Unlike traditional semantic search engines that require extensive data labeling and training, SEMSE offers an automated pipeline that can create a semantic search engine for any given website without human intervention. This project leverages cutting-edge language models and indexing techniques to streamline the process, making it efficient and user-friendly.

### Key Features:

#### Block Diagram of the Project:
![Alt text](https://github.com/osabnis/Semantic_Search_API/blob/main/graphs__and_statistics/block_diagram.drawio.png "Block Diagram")

#### Content Extraction: 
SEMSE extracts and cleans content from websites, creating a corpus of text for indexing. This ensures that the main content is extracted while ignoring repetitive headers and footers.

#### Language Agnostic Model: 
The project utilizes the Language Agnostic SEntence Representations (LASER) model by Facebook, which supports 93 different languages. LASER's unique feature is its ability to embed multiple languages into a shared space, making it suitable for English, Hindi, and Spanish without the need for fine-tuning.

#### Indexing: 
SEMSE converts processed web content into a semantic index, using FAISS to efficiently store and retrieve embeddings. This ensures fast and accurate search results.

#### Similarity Metric: 
The project uses cosine similarity as the primary measure of similarity to find content related to user queries. This approach is ideal for returning content similar to the query, rather than entire paragraphs.

#### Training:
We wanted to use the model without training to see the results without the need for any training. However, we did try to fine-tune the model for around 50 iterations on the extracted data from the website using AWS resources provided to us by the University.  
The training graph is shown below:
![Alt text](https://github.com/osabnis/Semantic_Search_API/blob/main/graphs__and_statistics/laser_training.PNG "Block Diagram")

#### Runtime Process: 
SEMSE's real-time application takes user queries, preprocesses them, encodes them using LASER, and retrieves the most similar content from the semantic index. It then returns the content, the source webpage, and the similarity score.

#### Evaluation:
SEMSE's performance is evaluated using a dataset of user queries related to a student health website. The top-3 accuracy metric is used to assess the model's performance in comparison to other models, including Multilingual BERT and XLM-Roberta, in both zero-shot and fine-tuned scenarios. SEMSE achieves impressive results in a zero-shot scenario, outperforming keyword-based search. Even after fine-tuning, it remains competitive with fine-tuned models.  
##### Comparison of the results:
Zero-Shot Performance:

Fine-Tuned Performance:


#### Conclusion:
SEMSE presents a significant achievement in the world of unsupervised semantic search engines. It achieves a top-3 accuracy of 81.82% in a zero-shot scenario and remains competitive after fine-tuning. Unlike other models, SEMSE does not require extensive training and can be easily regenerated when new content is added to the website. It offers a powerful and user-friendly solution for enhancing search capabilities on websites.  
##### Performance of SEMSE in English against m-BERT and XLM-R in English:  
![Alt text](https://github.com/osabnis/Semantic_Search_API/blob/main/graphs__and_statistics/top-3-accuracy-graph-english.png "Block Diagram")  
##### Performance of SEMSE in English against m-BERT and XLM-R in Hindi:  
![Alt text](https://github.com/osabnis/Semantic_Search_API/blob/main/graphs__and_statistics/top-3-accuracy-graph-hindi.png "Block Diagram")  
##### Performance of SEMSE in English against m-BERT and XLM-R in Spanish:  
![Alt text](https://github.com/osabnis/Semantic_Search_API/blob/main/graphs__and_statistics/top-3-accuracy-graph-spanish.png "Block Diagram")  

### How to run this?
Make the following changes to be able to run this code for yourself!
- Create an environment with the requirements file provided.
- Run the main.py file using this environment.
- You should be good to go - with the API being visible at the 8000 port on LocalHost!
