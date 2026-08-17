"""
actualizar.py — Convierte el Excel a JSON para el dashboard.

USO: python actualizar.py

Requiere: pip install pandas openpyxl
"""

import pandas as pd
import json
import sys
from pathlib import Path

EXCEL_FILE = "Compromisos.xlsx"   # ← cambia el nombre si es diferente
SHEET_NAME = "Hoja2"              # ← cambia la hoja si es diferente
OUTPUT_FILE = "compromisos.json"

def main():
    excel_path = Path(EXCEL_FILE)
    if not excel_path.exists():
        print(f"❌ No se encontró el archivo: {EXCEL_FILE}")
        print(f"   Asegúrate de que el Excel esté en la misma carpeta que este script.")
        sys.exit(1)

    print(f"📂 Leyendo {EXCEL_FILE}...")
    df = pd.read_excel(excel_path, sheet_name=SHEET_NAME)

    # Convertir fechas a texto
    for col in df.columns:
        if df[col].dtype == 'datetime64[ns]':
            df[col] = df[col].dt.strftime('%Y-%m-%d')

    # Reemplazar NaN por None (null en JSON)
    df = df.where(pd.notnull(df), None)

    records = df.to_dict(orient='records')

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

    print(f"✅ Exportados {len(records)} compromisos → {OUTPUT_FILE}")
    print(f"   Ahora haz git add, commit y push para publicar los cambios.")

if __name__ == "__main__":
    main()
