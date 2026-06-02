from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any

VALID_TYPES = {'texto', 'numero', 'booleano', 'fecha', 'decimal'}

@dataclass
class Field:
    name: str
    type: str = 'texto'
    required: bool = True
    default: Optional[str] = None

@dataclass
class Entity:
    name: str
    fields: List[Field] = field(default_factory=list)

@dataclass
class Intention:
    objetivo: str = ''
    usuarios: List[str] = field(default_factory=list)
    entidades: List[Entity] = field(default_factory=list)
    funciones: List[str] = field(default_factory=list)
    restricciones: List[str] = field(default_factory=list)
    plataformas: List[str] = field(default_factory=lambda: ['web'])
    nombre: str = 'Aplicacion ONE'

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
