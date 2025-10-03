import re
import nltk
import spacy
from nltk.corpus import stopwords

nltk.downloader.download('stopwords')

stop_words = set(stopwords.words('portuguese'))

spacy = spacy.load('pt_core_news_sm')

def pre_processing(email: str) -> list[str]:
    email = email.lower()
    email = re.sub(r"http\S+|www\S+", " <URL> ", email)
    email = re.sub(r"\S+@\S+", " <EMAIL> ", email)
    email = re.sub(r"[^a-záéíóúãõâêîôûç\s]", " ", email)

    doc = spacy(email)

    tokens = []
    for token in doc:
        if token.is_alpha and token.lemma_ not in stop_words:
            tokens.append(token.lemma_)

    return tokens

def build_prompt() -> str:
    system_prompt = """
    Você é um classificador de e-mails.
    Sua tarefa é classificar o e-mail como **produtivo** ou **improdutivo**.

    Definições:
    - produtivo: relacionado a trabalho, estudo, finanças, compromissos, reuniões, ou informações úteis.
    - improdutivo: propaganda, spam, correntes, promoções irrelevantes, ou mensagens sem valor prático.

    Exemplos:
    - "reunião marcada para amanhã às 10h" → produtivo
    - "feliz natal para você e sua família!" → improdutivo
    
    Além da classificação, você deve gerar uma resposta adequada ao e-mail:
    - Se for produtivo: crie uma resposta educada e coerente com o conteúdo.
    - Se for improdutivo: crie uma resposta educada agradecendo a mensagem ou recusando/ignorando o conteúdo, de acordo com o caso.

    Classifique a mensagem e retorne o resultado **apenas** em JSON válido, usando aspas duplas, no seguinte formato:

    {
        "classificacao": "produtivo" | "improdutivo",
        "resposta": "<texto da resposta gerada>"
    }
    """
    return system_prompt.strip()