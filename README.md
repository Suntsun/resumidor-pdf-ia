# Resumidor de PDFs con IA

Aplicación en Python que permite subir un archivo PDF y obtener un resumen automático usando modelos de Inteligencia Artificial.

## Tecnologías usadas
- Python 3
- Streamlit
- Hugging Face Transformers
- PyTorch
- PyPDF2

## Funcionalidades
- Subida de archivos PDF
- Resumen automático por bloques (PDFs largos)
- Selector de longitud del resumen
- Descarga del resumen en formato .txt

## Cómo ejecutar el proyecto



1. Clona el repositorio:
```bash
git clone https://github.com/Suntsun/resumidor-pdf-ia.git
```

2. Instala dependencias:
```
pip install -r requirements.txt
```

3. Ejecuta la app:
```
python -m streamlit run resumidor.py