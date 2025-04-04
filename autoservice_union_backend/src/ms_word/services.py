from docx import Document

from members.schemas import BusinessOwnerValues, BusinessManagerValues, IndividualEntrepreneurValues


class MSWordManager:
    def create_participation_form(
            self,
            values: BusinessOwnerValues | BusinessManagerValues | IndividualEntrepreneurValues
    ):

        document = Document("templates/participation_form.docx")
        print(values.towns)
        replace_values = {
            "{organization_full_name}": values.organization_full_name,
            "{organization_short_name}": values.organization_short_name,
            "{organization_registration_date}": values.organization_registration_date,
            "{legal_address_of_organization}": values.legal_address_of_organization,
            "{main_business_place_address}": values.main_business_place_address,
            "{mailing_address_with_zip_code}": values.mailing_address_with_zip_code,
            "{organization_inn}": values.organization_inn,
            "{organization_main_okved_codes}": values.organization_main_okved_codes,
            "{bank_name}": values.bank_name,
            "{current_account}": values.current_account,
            "{correspondent_account}": values.correspondent_account,
            "{bic}": values.bic,
            "{towns}": values.towns
        }
        for placeholder, value in replace_values.items():
            self.replace_placeholder(document, placeholder, value)
        document.save(f"files/participation_form_{values.organization_full_name}.docx")

    def replace_placeholder(
            self,
            document: Document,
            placeholder: str,
            value: str
    ):
        for paragraph in document.paragraphs:
            if placeholder in paragraph.text:
                try:
                    paragraph.text = paragraph.text.replace(placeholder, value)
                except TypeError:
                    paragraph.text = paragraph.text.replace(placeholder, "")

        for table in document.tables:
            for row in table.rows:
                for cell in row.cells:
                    if placeholder in cell.text:
                        try:
                            cell.text = cell.text.replace(placeholder, value)
                        except TypeError:
                            cell.text = cell.text.replace(placeholder, "")
