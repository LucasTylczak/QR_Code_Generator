import qrcode

print(╔═══════════════════════╦════════════════════════════════╦═══════════════════════╗)
print(║  Dev  LucasTylczak   ║  Info   Qr code generator     ║  Programm   Python   ║)
print(╚═══════════════════════╩════════════════════════════════╩═══════════════════════╝)

def generate_qr_code(data, file_name)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=black, back_color=white)
    img.save(file_name)
    print(fLe code QR a été généré avec succès et enregistré sous le nom  {file_name})

if __name__ == __main__
    print(Que voulez-vous encoder dans le code QR )
    user_input = input(Entrez du texte, une URL ou des données structurées  )

    file_name = input(Entrez le nom du fichier pour enregistrer le code QR (ex qr_code.png)  )

    generate_qr_code(user_input, file_name)
