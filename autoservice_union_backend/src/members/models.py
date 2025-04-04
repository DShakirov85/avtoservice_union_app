from datetime import date

from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey, BigInteger, ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Enum as PGEnum

from db import Base
from .enums import (
    Status,
    MembershipLevel,
    RepresentationValidationDocuments,
    SideServices,
    Interaction,
    InterestedServices
)


class Bank(Base):
    __tablename__ = "banks"
    id = Column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)


class Representative(Base):
    __tablename__ = "representatives"
    id = Column(Integer, primary_key=True)
    position: Mapped[str] = mapped_column(
        String,
        comment="Должность сотрудника, отвечающего за взаимодействие с Союзом",
        nullable=False
    )
    full_name: Mapped[str] = mapped_column(
        String,
        comment="Фамилия, имя и отчество отвечающего за взаимодействие с Союзом",
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String,
        comment="Е-мейл отвечающего за взаимодействие с Союзом",
        nullable=False
    )
    phone: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    power_of_attorney_number: Mapped[str] = mapped_column(
        String,
        nullable=True,
        comment="Номер доверенности (если есть) для сотрудника, отвечающего за взаимодействие с Союзом"
    )
    power_of_attorney_date: Mapped[date] = mapped_column(
        Date,
        nullable=True,
        comment="Дата выдачи доверенности для сотрудника, отвечающего за взаимодействие с Союзом"
    )
    power_of_attorney_place: Mapped[str] = mapped_column(
        String,
        nullable=True,
        comment="Место выдачи доверенности для сотрудника, отвечающего за взаимодействие с Союзом"
    )
    power_of_attorney_validity: Mapped[date] = mapped_column(
        Date,
        nullable=True,
        comment="Срок действия доверенности для сотрудника, отвечающего за взаимодействие с Союзом"
    )


class InternetRepresentation(Base):
    __tablename__ = "internet_representation"
    id = Column(Integer, primary_key=True)
    vk: Mapped[str] = mapped_column(
        String,
        nullable=True
    )
    telegram: Mapped[str] = mapped_column(
        String,
        nullable=True
    )
    whatsapp: Mapped[str] = mapped_column(
        String,
        nullable=True
    )


class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(
        String,
        comment="Ваши фамилия, имя и отчество",
        nullable=False
    )
    status: Mapped[Enum] = mapped_column(
        Enum(Status),
        comment="В каком статусе вы планируете участвовать в деятельности Союза?",
        nullable=False
    )
    membership_level: Mapped[Enum] = mapped_column(
        Enum(MembershipLevel),
        comment="Какой уровень участия в Союзе членства выбираете?",
        nullable=False
    )
    passport_data: Mapped[str] = mapped_column(
        String,
        comment="Паспортные данные (серия, номер, дата выдачи, выдавший орган)",
        nullable=False
    )
    address_data: Mapped[str] = mapped_column(
        String,
        comment="Адрес по прописке с индексом",
        nullable=False
    )
    ogrnip: Mapped[int] = mapped_column(
        Integer,
        comment="ОГРНИП",
        nullable=False
    )
    organization_full_name: Mapped[str] = mapped_column(
        String,
        comment="Полное название организации",
        nullable=False
    )
    organization_short_name: Mapped[str] = mapped_column(
        String,
        comment="Сокращенное название организации",
        nullable=False
    )
    organizations_inn: Mapped[int] = mapped_column(
        Integer,
        comment="ИНН организации",
        nullable=False
    )
    kpp: Mapped[int] = mapped_column(
        Integer,
        comment="КПП",
        nullable=False
    )
    registration_in_tax_authority_date: Mapped[date] = mapped_column(
        Date,
        comment="Дата постановки на учет в налоговом органе",
        nullable=False
    )
    organization_ogrn: Mapped[int] = mapped_column(
        Integer,
        comment="ОГРН организации",
        nullable=False
    )
    ogrnip: Mapped[int] = mapped_column(
        Integer,
        comment="Основной государственный регистрационный номер (ОГРНИП)",
        nullable=False
    )
    organization_registration_date: Mapped[date] = mapped_column(
        Date,
        comment="Дата регистрации организации / ИП",
        nullable=False
    )
    head_of_organization_position: Mapped[str] = mapped_column(
        String,
        comment="Должность руководителя организации",
        nullable=False
    )
    head_of_organization_full_name: Mapped[str] = mapped_column(
        String,
        comment="Фамилия, имя, отчество руководителя организации",
        nullable=False
    )
    position: Mapped[str] = mapped_column(
        String,
        comment="Ваша должность",
        nullable=False
    )
    organization_main_okved_codes: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment=(
                "Укажите основной вид деятельности из выписки ЕГРИП "
                "(отдельный блок \"Сведения об основном виде деятельности\")"
                )
    )
    occupation: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="Чем в организации занимаетесь  лично вы"
    )
    legal_address_of_organization: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="Адрес организации юридический"
    )
    main_business_place_address: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="Адрес места основной деятельности организации"
    )
    mailing_address_with_zip_code: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="Адрес для почтовой корреспонденции с индексом"
    )
    organizations_first_phone: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="Телефон 1 организации / ИП"
    )
    organizations_second_phone: Mapped[str] = mapped_column(
        String,
        comment="Телефон 2 организации / ИП",
        nullable=True
    )
    personal_phone: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="Телефон личный в формате +7ХХХХХХХХХХ"
    )
    site: Mapped[str] = mapped_column(
        String,
        nullable=True,
        comment="Адрес сайта"
    )
    email: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment="Е-мейл организации / ИП"
    )
    representation_documents: Mapped[Enum] = mapped_column(
        Enum(RepresentationValidationDocuments),
        nullable=False,
        comment="Документы, наделяющие вас правом представлять организацию в Союзе автосервисов"
    )
    bank_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("banks.id"),
        nullable=False,
    )
    current_account: Mapped[int] = mapped_column(
        BigInteger,
        comment="Расчетный счет",
        nullable=False,
    )
    correspondent_account: Mapped[int] = mapped_column(
        BigInteger,
        comment="Корреспондентский счет",
        nullable=False,
    )
    bic: Mapped[str] = mapped_column(
        String,
        comment="BIC",
        nullable=False,
    )
    towns: Mapped[list[str]] = mapped_column(
        ARRAY(String),
        comment="В каких городах и населенных пунктах работает ваше предприятие",
        nullable=False,
    )
    average_number_of_employees: Mapped[int] = mapped_column(
        Integer,
        comment="Среднесписочная численность организации",
        nullable=False,
    )
    number_of_services_and_repair_posts: Mapped[str] = mapped_column(
        String,
        comment="Количество сервисов и ремонтных  постов в каждом из них",
        nullable=False,
    )
    facade_photos: Mapped[list[str]] = mapped_column(
        ARRAY(String),
        nullable=False,
        comment="Приложите фотографии фасадов, клиентской зоны (если есть), общий вид рабочей зоны."
    )
    side_services: Mapped[list[Enum]] = mapped_column(
        ARRAY(PGEnum(SideServices)),
        comment="Имеете ли при сервисе, даже если это не ваш бизнес",
        nullable=False,
    )
    organizations_specialization: Mapped[str] = mapped_column(
        String,
        comment="Какова специализация вашей организации?",
        nullable=False,
    )
    interaction: Mapped[Enum] = mapped_column(
        Enum(Interaction),
        comment="Как будете взаимодействовать с Союзом",
        nullable=False,
    )
    representative_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("representatives.id"),
        nullable=True
    )
    internet_representation_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("internet_representation.id"),
        nullable=True
    )
    interested_services: Mapped[list[Enum]] = mapped_column(
        ARRAY(PGEnum(InterestedServices)),
        comment="В каких услугах Вы заинтересованы:",
        nullable=False,
    )
    can_be_useful: Mapped[str] = mapped_column(
        String,
        nullable=True,
        comment="Чем можете быть полезны (какую работу вести в Союзе, например, взаимодействие с органами власти, "
                "обучение персонала)?"
    )
    recommended_partner: Mapped[str] = mapped_column(
        String,
        nullable=True,
        comment="Кого бы Вы рекомендовали в качестве добросовестного партнера для сотрудничества  с Союзом автосервисов"
    )
    date_of_registration: Mapped[date] = mapped_column(
        Date,
        comment="Дата заполнения регистрационной формы",
        nullable=False,
    )


