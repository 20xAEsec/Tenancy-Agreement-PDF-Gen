# Room Rental Agreement PDF Generator

This repository contains a Python script that generates a legally sound, professional-grade Room Rental Agreement in PDF format. The agreement is tailored to reflect landlord and tenant terms relevant to California law, including utilities, guest policy, termination, and more.

The default conditions are relaxed, but you may update with your own, more protective conditions within the function.

## 📄 What It Does
The script uses the `fpdf` Python library to:
- Generate a full rental agreement for a private room
- Include terms for month-to-month tenancy, utilities, pet and guest policies
- Produce a polished, print-ready or digital-signature-ready PDF document

## 🛠 Requirements
- Python 3.x
- `fpdf` library

You can install the required library with:
```bash
pip install fpdf
```

## 🚀 How to Use
Edit the script and look for the `generate_tenant_agreement_pdf()` function. Inside this function, you’ll find all the predefined sections that make up the rental agreement. 

### ✏️ Fill in Your Information:
Modify the following details directly inside the `generate_tenant_agreement_pdf()` function before running it:
- **Landlord Name**
- **Tenant Name** *(leave blank if creating a template)*
- **Property Address**
- **Room Description and Furnishings**
- **Start Date of Tenancy**
- **Monthly Rent Amount**
- **Payment Method**
- **Any Additional Terms** (optional)

### 🧾 To Generate the PDF
Simply run the script:
```bash
python your_script_name.py
```
This will create a PDF file named `Room_Rental_Agreement_Official_Format.pdf` (or your custom filename).

## 📬 Output
The output is a legally comprehensive and cleanly formatted room rental agreement PDF. It can be:
- Printed and signed
- Digitally signed
- Customized for multiple tenants

## 📌 Notes
- The agreement includes a clause for utilities, guest limits, shared spaces, and termination notice.
- It uses sanitized ASCII characters to ensure compatibility with PDF rendering tools.

## 📄 License
This project is provided as-is for personal and small-business use. It is your responsibility to ensure local compliance with rental laws.

---

Need an interactive web app or auto-fill template version? Reach out or fork this repo to extend it!
