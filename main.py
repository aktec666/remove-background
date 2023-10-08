from rembg import remove
import numpy as np
import cv2

input_path = 'images/sample.png'
output_path = 'images/result.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)


def change_back2(background, img):
    x, y = 0, 0
    background = cv2.resize(background, (img.shape[1], img.shape[0]), interpolation = cv2.INTER_AREA)
    for i in range(img.shape[1]):
        for j in range(img.shape[0]):
            (b, g, r) = img[i,j]
            if (b, g, r) == (0, 0, 0):
                back[i][j] = img[i][j]
    return back

def change_back(background, img):
    x, y = 0, 0
    background = cv2.resize(background, (img.shape[1], img.shape[0]), interpolation = cv2.INTER_AREA)
    res = np.copy(background)
    place = res[y: y + img.shape[0], x: x + img.shape[1]]
    a = img[..., 3:].repeat(3, axis=2).astype('uint16')
    place[...] = (place.astype('uint16') * (255 - a) // 255) + img[..., :3].astype('uint16') * a // 255
    return res

image = cv2.imread('images/result.png', cv2.IMREAD_UNCHANGED)
back = cv2.imread('images/background_sample.jpg')
result = change_back(back, image)
print(image[1,0])
cv2.imwrite('images/result2.png', result)

    