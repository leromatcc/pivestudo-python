# pip install "fastapi[standard]"

"""
documentacao oficial do fastapi
https://github.com/fastapi/fastapi
https://fastapi.tiangolo.com/tutorial/

muito inspirado no projeto apresentado em: https://www.youtube.com/watch?v=noTBY5_Po80

pode ser uma evolução transformar em htmx
https://docs.fastht.ml/
"""

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
import os
from random import randint
import uuid
from . import identificador

IMAGEDIR = "resources/upload/images/"


router = APIRouter(
    prefix="/detector",
    tags=["detector"],
    responses={404: {"description": "Not found uuu"}},
)




@router.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    # save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)

    return {"filename": file.filename}


@router.get("/show/")
async def read_random_file():

    files = os.listdir(IMAGEDIR)
    if len(files) <1:
        return {"PIV Estudo": "Diretorio Vazio"}
    else:
        random_index = randint(0, len(files) - 1)

        path = f"{IMAGEDIR}{files[random_index]}"

        return FileResponse(path)



@router.get("/detectar/")
async def detectar_texto_imagem():
    textos = identificador.todosPassos()

    return {"textos": textos}