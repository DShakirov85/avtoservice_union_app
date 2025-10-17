import os
import re
from typing import Any

from pydantic import ValidationError

from .schemas import (
    CompanyLeaderForm,
    IndividualEntrepreneurForm,
    LegalEntityForm
)
from logger import logger

from ms_word.services import MSWordManager
from mail.services import EmailManager
from amo.services import AmoCRMManager


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
        logger.info(f"Successfully validated: {serialized_data}")
    except ValidationError as e:
        logger.error(e)
        logger.warning(f"Сan not validate data: {data}")
        return
    word = MSWordManager()
    if data_type == CompanyLeaderForm:
        participation_form = word.create_leader_participation_form(serialized_data)
    if data_type == IndividualEntrepreneurForm:
        participation_form = word.create_individual_entrepreneur_participation_form(serialized_data)
    if data_type == LegalEntityForm:
        participation_form = word.create_legal_entity_participation_form(serialized_data)
    principle = word.create_principle(serialized_data)
    survey_form = word.create_survey_form(serialized_data)
    personal_data_consent = word.create_personal_data_consent(serialized_data)
    if serialized_data.email:
        email_manager = EmailManager()
        response = await email_manager.send_participation_email(
            serialized_data.email,
            participation_form,
            survey_form,
            principle,
            personal_data_consent
        )

    amo_crm_manager = AmoCRMManager()
    response = await amo_crm_manager.send_lead_to_amo(serialized_data)
    logger.info(response)


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