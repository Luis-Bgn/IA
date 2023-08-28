from deepface import DeepFace
import cv2

img1=cv2.imread("foto1.png",cv2.IMREAD_COLOR)
img2=cv2.imread("foto2.png",cv2.IMREAD_COLOR)

result = DeepFace.verify(img1_path = "foto1.png", img2_path = "foto2.png")

x=result.get("facial_areas").get("img1").get("x")
y=result.get("facial_areas").get("img1").get("y")
w=result.get("facial_areas").get("img1").get("w")
h=result.get("facial_areas").get("img1").get("h")

x2=result.get("facial_areas").get("img2").get("x")
y2=result.get("facial_areas").get("img2").get("y")
w2=result.get("facial_areas").get("img2").get("w")
h2=result.get("facial_areas").get("img2").get("h")

cv2.rectangle(img1, (x, y), (x + w, y + h), (255), 2)
cv2.rectangle(img2, (x2, y2), (x2 + w2, y2 + h2), (255), 2)

cv2.imshow("uno",img1)
cv2.imshow("dos",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()