import json
import os

from PyPDF2 import PdfReader
from dotenv import load_dotenv
from fastapi import APIRouter, UploadFile, File
from openai import OpenAI
from pydantic import BaseModel
from fastapi import Response

from preprocessing.pre_processing import pre_processing, build_prompt

api_router = APIRouter()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
)

class EmailTextRequest(BaseModel):
    emailContent: str

@api_router.post("/text")
async def analyze_text(request: EmailTextRequest):
    tokens = pre_processing(request.emailContent)
    result_json = openai_request(tokens)

    return result_json

@api_router.post("/file")
async def analyze_file(file: UploadFile = File(...)):
    try:
        _, ext = os.path.splitext(file.filename)
        ext = ext.lower()

        content = ""

        if ext == ".txt":
            temp = await file.read()
            content = temp.decode("utf-8")
        elif ext == ".pdf":
            temp_path = f"temp_{file.filename}"
            with open(temp_path, "wb") as f:
                f.write(await file.read())

            reader = PdfReader(temp_path)
            pdf_text = ""
            for page in reader.pages:
                pdf_text += page.extractText() + "\n"

            content = pdf_text
            os.remove(temp_path)

        tokens = pre_processing(content)

    except Exception as exception:
        return Response(content=f"Formato de arquivo não suportado {exception}", status_code=500)

    result_json = openai_request(tokens)

    return result_json

def openai_request(tokens) -> str:
    response = client.chat.completions.create(
        model="gpt-5-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": build_prompt()},
            {"role": "user", "content": f"E-mail:\n{tokens}"}
        ]
    )

    result_json = json.loads(response.choices[0].message.content)

    return result_json
