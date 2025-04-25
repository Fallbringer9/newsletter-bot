def save_text_to_html(text, output_path="newsletter.html"):
    try:
        lines = "".join(f"<p>{line.strip()}</p>" for line in text.split("\n") if line.strip())

        html = f"""
        <html>
            <head>
                <meta charset="UTF-8">
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; }}
                    h1 {{ color: #2E86C1; }}
                    p {{ line-height: 1.6; }}
                </style>
            </head>
            <body>
                <h1>Newsletter Tech/Dev/Cloud</h1>
                {lines}
            </body>
        </html>
        """

        with open(output_path, "w", encoding="utf-8") as html_file:
            html_file.write(html)

        print(f"✅ HTML généré avec succès → {output_path}")

    except Exception as e:
        print(f"❌ Erreur générale lors de la génération du HTML : {e}")
