import enum


class Status(enum.Enum):
    individual = "Физическое лицо (руководитель, собственник компании)"
    legal_entity = "Юридическое лицо (представитель компании, один из руководителей)"
    individual_entrepreneur = "Индивидуальный предприниматель (работающий в автосервисной отрасли)"


class MembershipLevel(enum.Enum):
    third_college_member = "член третьей коллегии"


class RepresentationValidationDocuments(enum.Enum):
    charter = "Устав организации (если вы - руководитель организации)"
    power_of_attorney = "Доверенность (если вы сотрудник организации)"


class SideServices(enum.Enum):
    spare_parts_store = "Магазин автозапчастей"
    cafe = "Кафе"
    car_wash_service = "Автомойку"
    another = "Что-то другое"


class Interaction(enum.Enum):
    in_person = "Лично"
    representative = "Through a representative by power of attorney"


class InterestedServices(enum.Enum):
    legal = "юридические"
    information_support = "информационная поддержка, реклама"
    property_valuation = "оценка собственности"
    staff_training = "обучение персонала"
    recruitment = "подбор персонала"
    tenders_support = "поддержка при подготовке документов для тендеров (закупок) и участия в торгах"
    electronic_trades_support = ("мероприятия по работе на электронных торговых площадках (госзакупки, коммерческие "
                                 "закупки)")
    research = "исследовательские (маркетинговые, консалтинговые)"
    patent_science = "патентоведение и защита интеллектуальной собственности"
    exhibitions_participation = "участие в выставках, ярмарках, торгово-экономических миссиях"
    business_education = "деловое образование для руководителей (тематические семинары и тренинги)"
    register_of_reliable_partners = "внесение организации в негосударственный Реестр надежных партнеров ТПП РФ"
    other = "другое"
