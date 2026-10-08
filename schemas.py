from pydantic import BaseModel, Field
from typing import Optional

class Despesa(BaseModel):
    descricao_original: str = Field(description="Texto original fornecido pelo colaborador")
    fornecedor: str = Field(description="Nome do estabelecimento ou fornecedor")
    valor: float = Field(description="Valor total da despesa")
    categoria: str = Field(description="Categoria, ex: refeicao, transporte, alojamento")
    status: Optional[str] = Field(default="Pendente", description="Estado da aprovação")
    motivo: Optional[str] = Field(default=None, description="Justificativa da aprovação ou rejeição")