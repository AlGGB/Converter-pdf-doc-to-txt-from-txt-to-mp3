import PyPDF2



def pdf_to_text_pypdf2(file_path, output_txt):
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        
        with open(output_txt, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)
        print(f"Texto extraído y guardado en: {output_txt}")
    except Exception as e:
        print(f"Error: {e}")

# Uso:
pdf_to_text_pypdf2("somefile.pdf", "somefile.txt")


#para convertir los pdf en txt
