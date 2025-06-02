import re
from typing import Any

from pydantic import ValidationError

from .schemas import (
    CompanyLeaderForm,
    IndividualEntrepreneurForm,
    LegalEntityForm
)
from logger import logger


def fix_bad_json(bad_json_bytes):
    bad_json_str = bad_json_bytes.decode('utf-8')

    fixed_json_str = bad_json_str.replace('\\"', '"')

    fixed_json_str = re.sub(r'(?<!\\)\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', '', fixed_json_str)

    return fixed_json_str


async def process_data(data: Any):
    data_type = detect_form_type(data)
    logger.info(data_type)
    try:
        serialized_data = data_type(**data)
        logger.info(serialized_data)
    except ValidationError:
        logger.warning(data)



def detect_form_type(data: dict) -> type:
    status = data.get("В каком статусе вы планируете участвовать в деятельности Союза?", "")

    if "Юридическое лицо" in status:
        return LegalEntityForm
    elif "Физическое лицо" in status:
        return CompanyLeaderForm
    elif "Индивидуальный предприниматель" in status:
        return IndividualEntrepreneurForm
    else:
        raise ValueError("Неизвестный тип данных")