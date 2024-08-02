from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import AsyncHtmlLoader
from bs4 import BeautifulSoup

def get_raw_html():
    url = 'https://en.wikipedia.org/wiki/2024_Summer_Olympics_medal_table'
    loader = AsyncHtmlLoader([url])
    docs = loader.load()
    raw_html = docs[0].page_content

    # Criar o objeto BeautifulSoup
    soup = BeautifulSoup(raw_html, 'html.parser')

    # Buscar pela tag <table> com a classe específica
    raw_table = soup.find('table', class_='wikitable sortable notheme plainrowheaders jquery-tablesorter')

    return raw_table

def transform_to_markdown(raw_table):
    messages = [
        ("system", "Transforme em uma table markdown:"),
        ("human", "{table}")
    ]
    prompt = ChatPromptTemplate.from_messages(messages)

    # <LLM model>
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, temperature=0, model='gpt-4o-mini-2024-07-18')

    chain = prompt | llm | StrOutputParser()

    return chain.invoke({"table": raw_table})

def get_medal_table():
    raw_table = get_raw_html()
    markdown_table = transform_to_markdown(raw_table)
    return markdown_table