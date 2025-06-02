from pydantic import BaseModel, Field, HttpUrl, EmailStr, validator, field_validator
from typing import List, Optional, Union, Literal
from datetime import date, datetime

# TODO: check optional fields

"""
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
"""


class BankDetails(BaseModel):
    bank_name: Optional[str] = Field(None, alias="Наименование банка")
    account_number: Optional[str] = Field(None, alias="Расчетный счет")
    correspondent_account: Optional[str] = Field(None, alias="Корреспондентский счет")
    bik: Optional[str] = Field(None, alias="БИК")


class AutoServiceUnionForm(BaseModel):
    full_name: str = Field(..., alias="Ваши фамилия, имя и отчество")
    participation_status: str = Field(..., alias="В каком статусе вы планируете участвовать в деятельности Союза?")

    payment_confirmation: Optional[HttpUrl] = Field(None,
                                                    alias="Пожалуйста загрузите подтверждение оплаты вступительного взноса")
    passport_data: Optional[str] = Field(None, alias="Паспортные данные (серия, номер, дата выдачи, выдавший орган)")
    registration_address: Optional[str] = Field(None, alias="Адрес по прописке с индексом")
    ogrnip: Optional[str] = Field(None, alias="ОГРНИП")
    company_inn: Optional[str] = Field(None, alias="ИНН организации")

    tax_registration_date: Optional[Union[datetime,str]] = Field(None, alias="Дата постановки на учет в налоговом органе")
    registration_date: Optional[Union[datetime,str]] = Field(None, alias="Дата регистрации организации / ИП")

    legal_address: Optional[str] = Field(None, alias="Адрес организации юридический")
    actual_address: Optional[str] = Field(None, alias="Адрес места основной деятельности организации")
    mailing_address: Optional[str] = Field(None, alias="Адрес для почтовой корреспонденции с индексом")
    company_phone: str = Field(..., alias="Телефон 1 организации / ИП")
    personal_phone: str = Field(..., alias="Телефон личный в формате +7ХХХХХХХХХХ")
    website: Optional[str] = Field(None, alias="Адрес сайта")
    email: EmailStr = Field(..., alias="Е-мейл организации / ИП")

    bank_details: Optional[BankDetails] = None

    locations: Optional[str] = Field(None, alias="В каких городах и населенных пунктах работает ваше предприятие")
    employee_count: Optional[int] = Field(None, alias="Среднесписочная численность организации")
    service_points_count: Optional[str] = Field(None, alias="Количество сервисов и ремонтных постов в каждом из них")
    service_zones_photos: Optional[HttpUrl] = Field(None, alias="Приложите фотографии: ремонтной зоны, зону приёмки...")
    facilities: Optional[str] = Field(None, alias="Имеете ли при сервисе, даже если это не ваш бизнес:")
    specialization: Optional[str] = Field(None, alias="Какова специализация вашей организации?")
    okved_codes: Optional[str] = Field(None, alias="Основные коды ОКВЭД организации / ИП")
    company_ogrnip: Optional[str] = Field(None, alias="ОГРНИП"
                                          )
    interaction_method: Optional[str] = Field(None, alias="Как будете взаимодействовать с Союзом")
    representative: Optional[str] = Field(
        None,
        alias="Сотрудник, ответственный за взаимодействие с Союзом (по доверенности)"
    )
    social_media: Optional[str] = Field(
        None,
        alias="Укажите ваше представительство в интернете"
    )

    participation_purpose: Optional[str] = Field(None,
                                                 alias="Какова цель участия в Союзе автосервисов вас / вашей организации")
    interested_services: Optional[str] = Field(None, alias="В каких услугах Вы заинтересованы:")
    can_help_with: Optional[str] = Field(None, alias="Чем можете быть полезны...")
    recommended_partners: Optional[str] = Field(None,
                                                alias="Кого бы Вы рекомендовали в качестве добросовестного партнера...")

    consent_to_personal_data_processing: Optional[str] = Field(None, alias="Даю свое согласие на обработку персональных данных")
    data_accuracy_confirmation: Optional[str] = Field(None, alias="Достоверность данных подтверждаю")
    submission_date: str = Field(..., alias="Дата заполнения регистрационной формы")

    @field_validator('bank_details', mode='before')
    def set_bank_details(cls, v, values):
        if any(values.get(field) in (None, "Нет ответа") for field in [
            "Наименование_банка", "Расчетный_счет", "Корреспондентский_счет", "БИК"
        ]):
            return None
        return BankDetails(
            bank_name=values.get("Наименование_банка"),
            account_number=values.get("Расчетный_счет"),
            correspondent_account=values.get("Корреспондентский_счет"),
            bik=values.get("БИК")
        )

    @field_validator('tax_registration_date', 'registration_date', mode='before')
    def parse_dates(cls, v):
        if v in (None, "Нет ответа"):
            return None
        try:
            return datetime.strptime(v, '%Y-%m-%d').date()
        except ValueError:
            try:
                return datetime.strptime(v, '%d.%m.%Y').date()
            except ValueError:
                return v

    @field_validator("representative", mode='before')
    def set_representative(cls, v):
        if v in (None, "Нет ответа"):
            return None
        try:
            return v
        except (ValueError, AttributeError):
            return None

    @field_validator("social_media", mode='before')
    def set_social_media(cls, v, values):
        if v in (None, "Нет ответа"):
            return None
        return v

    @field_validator('company_ogrnip', 'company_inn', mode='before')
    def parse_ogrnip_and_inn(cls, v):
        return None if v == "Нет ответа" else v


class CompanyLeaderForm(AutoServiceUnionForm):
    company_name: Optional[str] = Field(None, alias="Полное название организации")
    company_short_name: Optional[str] = Field(None, alias="Сокращенное название организации")
    company_kpp: Optional[str] = Field(None, alias="КПП")
    company_ogrn: Optional[str] = Field(None, alias="ОГРН организации")


    @field_validator('company_ogrn', 'company_kpp', mode='before')
    def empty_to_none(cls, v):
        return None if v == "Нет ответа" else v


class LegalEntityForm(AutoServiceUnionForm):
    company_name: Optional[str] = Field(None, alias="Полное название организации")
    company_short_name: Optional[str] = Field(None, alias="Сокращенное название организации")
    company_kpp: Optional[str] = Field(None, alias="КПП")
    company_ogrn: Optional[str] = Field(None, alias="ОГРН организации")

    director_position: Optional[str] = Field(None, alias="Должность руководителя организации")
    director_full_name: Optional[str] = Field(None, alias="Фамилия, имя, отчество руководителя организации")
    representative_documents: Optional[str] = Field(
        None,
        alias="Документы, наделяющие вас правом представлять организацию в Союзе автосервисов"
    )

    okved: Optional[str] = Field(None, alias="Основные коды ОКВЭД организации / ИП")


    @field_validator('company_ogrn', 'company_ogrnip', 'company_inn', 'company_kpp', mode='before')
    def empty_to_none(cls, v):
        return None if v == "Нет ответа" else v


class IndividualEntrepreneurForm(AutoServiceUnionForm):
    pass
