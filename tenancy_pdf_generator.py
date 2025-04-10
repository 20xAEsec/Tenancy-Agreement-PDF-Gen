from fpdf import FPDF
import re

# Replace all special quotation marks and dashes with ASCII-compatible characters
def clean_text_thorough(text):
    text = re.sub(r'[–—]', '-', text)
    text = re.sub(r'[“”]', '"', text)
    text = re.sub(r"[‘’]", "'", text)
    return text

class TenantAgreementPDF(FPDF):
    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 11)

    def section_body(self, text):
        self.multi_cell(0, 8, text)
        self.ln(5)

class UltraSafeTenantAgreementPDF(TenantAgreementPDF):
    def section_body(self, text):
        text = clean_text_thorough(text)
        super().section_body(text)

def generate_tenant_agreement_pdf(output_path="Room_Rental_Agreement_Official_Format.pdf"):

    ##################### ENTER YOUR INFORMATION HERE ###########################
    landlord_name = ""
    tenant_name = ""
    home_address = ""
    rent_amount_int = 0 # Replace with rent amount

    security_deposit_conditions = ""

    pdf = UltraSafeTenantAgreementPDF()
    pdf.add_page()

    pdf.section_title("1. Parties")
    pdf.section_body(
        f"This Room Rental Agreement (the \"Agreement\") is entered into by and between {landlord_name} (the \"Landlord\"), "
        "and {tenant_name} (the \"Tenant\"). This Agreement governs the rental of a private room within a shared residence."
    )

    pdf.section_title("2. Premises")
    pdf.section_body(
        f"The premises covered by this Agreement is a private room located at {home_address}. "
        "The Tenant shall have exclusive use of the designated private room and shared access to the common areas of the second floor, "
        "which includes the living room, kitchen, dining area, and laundry facilities."
    )

    pdf.section_title("3. Term")
    pdf.section_body(
        "The tenancy shall commence on ____________ and continue on a month-to-month basis until terminated by either party "
        "in accordance with the terms of this Agreement."
    )

    pdf.section_title("4. Rent")
    pdf.section_body(
        f"The monthly rental amount shall be ${rent_amount_int}, payable in advance on the 1st day of each month. "
        "Rent is to be paid in full and on time. There is no grace period or late fee; however, timely payment is expected."
    )

    pdf.section_title("5. Utilities")
    pdf.section_body(
        "All standard utilities, including but not limited to water, electricity, gas, and internet, are included in the rent. "
        "Excessive or unreasonable usage, as determined by the Landlord, may be subject to additional charges payable by the Tenant."
    )

    pdf.section_title("6. Security Deposit")
    pdf.section_body(
        str(security_deposit_conditions)
    )

    pdf.section_title("7. Guests")
    pdf.section_body(
        "Guests are permitted for short visits only. Overnight guests may not stay for more than two consecutive nights or a total of five nights "
        "within any calendar month without prior written consent from the Landlord. Under no circumstances shall guests establish residency, "
        "and no individual other than the Tenant may reside in the room without the Landlord's written approval."
    )

    pdf.section_title("8. Conduct and Use")
    pdf.section_body(
        "The Tenant agrees to maintain a respectful and non-disruptive environment. Aggressive behavior, intimidation, or hosting of regular parties "
        "is strictly prohibited. The Tenant shall be held fully responsible for any damage or disturbance caused by their guests."
    )

    pdf.section_title("9. Smoking Policy")
    pdf.section_body(
        "Smoking of tobacco products is strictly prohibited inside the residence."
    )

    pdf.section_title("10. Pets")
    pdf.section_body(
        "No pets are allowed without prior express written consent from the Landlord."
    )

    pdf.section_title("11. Parking")
    pdf.section_body(
        "Parking is available on public streets outside the community. No parking within the gated community is provided. Use of a garage parking space "
        "may be granted by the Landlord on a discretionary basis."
    )

    pdf.section_title("12. Access and Entry")
    pdf.section_body(
        "The Tenant will be provided with an electronic access code for the front door, remote access to the garage via a mobile application, "
        "and a fingerprint-enabled lock for exclusive access to their room. The Landlord retains a master key to all rooms. Entry by the Landlord shall only occur in cases of emergency "
        "(e.g., fire, flooding), or with proper notice, in accordance with California Civil Code Section 1954."
    )

    pdf.section_title("13. Termination of Tenancy")
    pdf.section_body(
        "Either party may terminate this Agreement with thirty (30) days' written notice. In the event of an early move-out, the rent shall be prorated "
        "based on a 30.5-day month."
    )

    pdf.section_title("14. Condition Upon Move-Out")
    pdf.section_body(
        "At the termination of this Agreement, the Tenant shall return the room in its original condition, including all furnishings and items provided at move-in. "
        "The Tenant agrees to have the room professionally cleaned upon move-out, at an estimated cost between $20 and $50."
    )

    pdf.section_title("15. Entire Agreement")
    pdf.section_body(
        "This Agreement constitutes the entire understanding between the parties. Any modifications must be in writing and signed by both parties."
    )

    pdf.section_title("16. Signatures")
    pdf.section_body("""
IN WITNESS WHEREOF, the parties have executed this Agreement as of the date written below.

Landlord Signature: _______________________     Date: __________

Tenant Signature:  _______________________     Date: __________
""")

    pdf.output(output_path)
    print(f"PDF saved to {output_path}")
