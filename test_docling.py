from docling.document_converter import DocumentConverter

file_path = "data/exemplo.pdf"  # Substitua por um arquivo real

try:
    converter = DocumentConverter()
    result = converter.convert(file_path)  # Tentar converter o documento
    print("✅ Extração bem-sucedida!")
    print(result)
except Exception as e:
    print(f"❌ Erro ao processar o arquivo: {e}")
