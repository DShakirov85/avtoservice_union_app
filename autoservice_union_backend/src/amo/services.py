from typing import TypedDict

import httpx

from settings import settings
from members.schemas import CompanyLeaderForm, IndividualEntrepreneurForm, LegalEntityForm
from logger import logger


class Link(TypedDict):
    href: str


class SelfLink(TypedDict):
    self: Link


class LeadLink(TypedDict):
    self: Link


class Lead(TypedDict):
    id: int
    request_id: str
    _links: dict[str, LeadLink]


class EmbeddedLeads(TypedDict):
    leads: list[Lead]


class AMOResponse(TypedDict):
    _links: SelfLink
    _embedded: EmbeddedLeads


class AmoCRMManager:
    def __init__(self):
        self.amo_host = settings.AMO_HOST
        self.amo_token = settings.AMO_TOKEN

    async def send_lead_to_amo(
            self,
            data : CompanyLeaderForm | IndividualEntrepreneurForm | LegalEntityForm
    ) -> AMOResponse:
        url = f"{self.amo_host}/api/v4/leads"
        headers = {"Authorization": f"Bearer {self.amo_token}"}
        payload = [
                {
                "name": f"Заявка на вступление: {data.full_name} {data.personal_phone}",
            }
        ]
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=payload)
            logger.info(response)
            return response.json()