import qrcode

job_code = "Abcdf2221"

qr = qrcode.make(job_code)

qr.save("job_qr.png")

print("QR Code created successfully!")
