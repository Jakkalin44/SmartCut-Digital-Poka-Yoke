import cv2

image = cv2.imread("job_qr.png")

if image is None:
    print("Image not found")

else:
    detector = cv2.QRCodeDetector()

    data, points, _ = detector.detectAndDecode(image)

    if data:
        print("QR Code detected!")
        print("Job Code:", data)
    else:
        print("QR Code not found")
