from pydantic import BaseModel, Field
from typing import List, Optional, Union
from datetime import date

# TODO: check optional fields


class AnswerFile(BaseModel):
    loading: bool
    name: str
    path: str
    size: int
    url: str


class InternetRepresentation(BaseModel):
    vk: Optional[str] = Field(default=None, alias="answer_short_text_47503876")
    telegram: Optional[str] = Field(default=None, alias="id-question-47504108")
    whatsapp: Optional[str] = Field(default=None, alias="id-question-47504127")


class BusinessOwnerValues(BaseModel):
    full_name: str = Field(..., alias="answer_short_text_47493732")
    status: List[str] = Field(..., alias="answer_choices_47493850")
    membership_level: List[str] = Field(..., alias="answer_choices_47494243")
    passport_data: str = Field(..., alias="answer_short_text_47494618")
    address_data: str = Field(..., alias="id-question-49184679")
    organization_full_name: str = Field(..., alias="id-question-47494641")
    organization_short_name: Optional[str] = Field(default=None, alias="id-question-47572714")
    organization_registration_date: Optional[str] = Field(default=None, alias="id-question-47499628")
    organization_inn: str = Field(..., alias="answer_short_text_47494694")
    position: str = Field(..., alias="id-question-47494736")
    organization_main_okved_codes: str = Field(..., alias="id-question-47494749")
    legal_address_of_organization: str = Field(..., alias="id-question-49211496")
    main_business_place_address: str = Field(..., alias="id-question-47494786")
    mailing_address_with_zip_code: str = Field(..., alias="id-question-47494813")
    organizations_first_phone: str = Field(..., alias="answer_phone_47494857")
    organizations_second_phone: Optional[str] = Field(default=None, alias="id-question-47494897")
    personal_phone: str = Field(..., alias="id-question-47494927")
    site: Optional[str] = Field(default=None, alias="answer_url_47494937")
    email: str = Field(..., alias="answer_non_profile_email_47498924")
    bank_name: str = Field(..., alias="answer_short_text_49185760")
    current_account: str = Field(..., alias="answer_short_text_48611763")
    correspondent_account: str = Field(..., alias="id-question-49185721")
    bic: str = Field(..., alias="id-question-48612106")
    towns: Optional[List[str]] = Field(default=None, alias="answer_choices_47499693")
    average_number_of_employees: str = Field(..., alias="answer_short_text_47499799")
    number_of_services_and_repair_posts: Optional[str] = Optional[Field(..., alias="answer_short_text_47500833")]
    facade_photos: List[AnswerFile] = Field(..., alias="answer_files_47504264")
    side_services: List[str] = Field(..., alias="answer_choices_47501037")
    organizations_specialization: str = Field(..., alias="id-question-47603918")
    internet_representation: Optional[List[InternetRepresentation]] = Field(default=None, alias="answer_group_47504045")
    interested_services: Optional[List[str]] = Field(default=None, alias="answer_choices_47504452")
    date_of_registration: str = Field(..., alias="answer_date_47505416")


class EmployeeValues(BaseModel):
    position: str = Field(..., alias="answer_short_text_47501171")
    full_name: str = Field(..., alias="id-question-47501196")
    email: str = Field(alias="id-question-47501207")
    phone: str = Field(..., alias="id-question-47501215")
    power_of_attorney_number: Optional[str] = Field(default=None, alias="id-question-47503651")
    power_of_attorney_date: str = Field(..., alias="id-question-49193900")
    power_of_attorney_place: Optional[str] = Field(default=None, alias="id-question-49196290")
    power_of_attorney_validity: Optional[str] = Field(default=None, alias="id-question-49196429")


class BusinessManagerValues(BaseModel):
    full_name: str = Field(..., alias="answer_short_text_47493732")
    status: List[str] = Field(..., alias="answer_choices_47493850")
    membership_level: List[str] = Field(..., alias="answer_choices_47494243")
    organization_full_name: str = Field(..., alias="id-question-47494641")
    organization_short_name: Optional[str] = Field(default=None, alias="id-question-47572714")
    id_question_47572714: str = Field(..., alias="id-question-47572714")
    organization_inn: str = Field(..., alias="answer_short_text_47494694")
    kpp: str = Field(..., alias="id-question-47498656")
    site: Optional[str] = Optional[Field(..., alias="answer_url_47494937")]
    registration_in_tax_authority_date: str = Field(..., alias="answer_date_47499356")
    organization_ogrn: str = Field(..., alias="id-question-47498691")
    organization_registration_date: str = Field(..., alias="id-question-47499628")
    head_of_organization_position: str = Field(..., alias="id-question-47498774")
    head_of_organization_full_name: str = Field(..., alias="id-question-47498799")
    organization_main_okved_codes: str = Field(..., alias="id-question-47494749")
    legal_address_of_organization: str = Field(..., alias="id-question-49211496")
    main_business_place_address: str = Field(..., alias="id-question-47494786")
    mailing_address_with_zip_code: str = Field(..., alias="id-question-47494813")
    organizations_first_phone: str = Field(..., alias="answer_phone_47494857")
    organizations_second_phone: Optional[str] = Field(default=None, alias="id-question-47494897")
    personal_phone: str = Field(..., alias="id-question-47494927")
    email: str = Field(..., alias="answer_non_profile_email_47498924")
    representation_documents: List[str] = Field(..., alias="id-question-47606980")
    bank_name: str = Field(..., alias="answer_short_text_49185760")
    current_account: str = Field(..., alias="answer_short_text_48611763")
    correspondent_account: str = Field(..., alias="id-question-49185721")
    bic: str = Field(..., alias="id-question-48612106")
    towns: Optional[List[str]] = Optional[Field(..., alias="answer_choices_47499693")]
    number_of_services_and_repair_posts: Optional[str] = Field(default=None, alias="answer_short_text_47500833")
    internet_representation: Optional[List[InternetRepresentation]] = Field(default=None, alias="answer_group_47504045")
    average_number_of_employees: str = Field(..., alias="answer_short_text_47499799")
    facade_photos: List[AnswerFile] = Field(..., alias="answer_files_47504264")
    side_services: List[str] = Field(..., alias="answer_choices_47501037")
    organizations_specialization: str = Field(..., alias="id-question-47603918")
    representative: Optional[List[EmployeeValues]] = Field(default=None, alias="answer_group_47501133")
    interested_services: Optional[List[str]] = Field(default=None, alias="answer_choices_47504452")
    date_of_registration: str = Field(..., alias="answer_date_47505416")


class IndividualEntrepreneurValues(BaseModel):
    full_name: str = Field(..., alias="answer_short_text_47493732")
    status: List[str] = Field(..., alias="answer_choices_47493850")
    membership_level: List[str] = Field(..., alias="answer_choices_47494243")
    ogrnip: str = Field(..., alias="id-question-47499229")
    organization_full_name: str = Field(..., alias="id-question-47494641")
    organization_short_name: str = Field(..., alias="id-question-47572714")
    organization_inn: str = Field(..., alias="answer_short_text_47494694")
    registration_in_tax_authority_date: str = Field(..., alias="answer_date_47499356")
    ogrnip: str = Field(..., alias="id-question-47499430")
    organization_registration_date: str = Field(..., alias="id-question-47499628")
    organization_main_okved_codes: str = Field(..., alias="id-question-47494749")
    legal_address_of_organization: str = Field(..., alias="id-question-49211496")
    main_business_place_address: str = Field(..., alias="id-question-47494786")
    mailing_address_with_zip_code: str = Field(..., alias="id-question-47494813")
    organizations_first_phone: str = Field(..., alias="answer_phone_47494857")
    organizations_second_phone: Optional[str] = Field(default=None, alias="id-question-47494897")
    personal_phone: str = Field(..., alias="id-question-47494927")
    site: Optional[str] = Field(default=None, alias="answer_url_47494937")
    email: str = Field(..., alias="answer_non_profile_email_47498924")
    bank_name: str = Field(..., alias="answer_short_text_49185760")
    current_account: str = Field(..., alias="answer_short_text_48611763")
    correspondent_account: str = Field(..., alias="id-question-49185721")
    bic: str = Field(..., alias="id-question-48612106")
    towns: Optional[List[str]] = Field(default=None, alias="answer_choices_47499693")
    average_number_of_employees: str = Field(..., alias="answer_short_text_47499799")
    number_of_services_and_repair_posts: Optional[str] = Field(default=None, alias="answer_short_text_47500833")
    facade_photos: List[AnswerFile] = Field(..., alias="answer_files_47504264")
    side_services: List[str] = Field(..., alias="answer_choices_47501037")
    organizations_specialization: str = Field(..., alias="id-question-47603918")
    interaction: List[str] = Field(..., alias="answer_choices_47503783")
    representative: Optional[List[EmployeeValues]] = Field(default=None, alias="answer_group_47501133")
    interested_services: Optional[List[str]] = Field(default=None, alias="answer_choices_47504452")
    representative: List[EmployeeValues]
    internet_representation: List[InternetRepresentation] = Field(..., alias="answer_group_47504045")
    date_of_registration: str = Field(..., alias="answer_date_47505416")


class Survey(BaseModel):
    surveyId: str
    values: BusinessOwnerValues | BusinessManagerValues | IndividualEntrepreneurValues
