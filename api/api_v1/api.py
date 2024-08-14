from fastapi import APIRouter

from api.api_v1.endpoints import chroma, milvus, qdrant, faiss

api_router = APIRouter()
api_router.include_router(chroma.router)
# api_router.include_router(chroma.router, tags=["chroma"])

# api_router.include_router(chromaKr.router, tags=["chromaKr"])
# api_router.include_router(chromaEn.router, tags=["chromaEn"])

# api_router.include_router(milvus.router, tags=["milvus"])
# api_router.include_router(qdrant.router, tags=["qdrant"])
# api_router.include_router(faiss.router, tags=["faiss"])