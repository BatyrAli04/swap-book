import shutil

from fastapi import APIRouter, Depends, UploadFile
from fastapi.responses import FileResponse

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/files",
    tags=["Files"],
    dependencies=[
        Depends(
            HTTPBearer())])

@router.post("/file", dependencies=[Depends(HTTPBearer())])
async def upload_file(*,
                    file: UploadFile,
                    Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()                
    file_location = f"files/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}


@router.get("/file/{file_name}", dependencies=[Depends(HTTPBearer())])
async def download_file(*,
                        file_name: str,
                        Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()    
    return FileResponse(path='files/' + file_name, filename=file_name, media_type='multipart/form-data')
