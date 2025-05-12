from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, UnstructuredFileLoader

def parse_file(file_path: str):
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        loader = PyPDFLoader(file_path)
    else:
        loader = UnstructuredFileLoader(file_path)

    return loader.load()