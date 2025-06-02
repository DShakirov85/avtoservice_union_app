from pydantic import BaseModel, Field, HttpUrl, EmailStr, field_validator
from typing import Optional, Union
from datetime import datetime


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
