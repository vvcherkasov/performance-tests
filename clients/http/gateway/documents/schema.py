from pydantic import BaseModel, HttpUrl

class DocumentSchema(BaseModel):
    """
    Описание структуры документа.
    """
    url: HttpUrl
    document: str

class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа документа по тарифу.
    """
    tariff: DocumentSchema

class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа документа по контракту.
    """
    contract: DocumentSchema
