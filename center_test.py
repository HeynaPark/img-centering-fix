import cv2
import numpy as np
import imageio
import glob

# 이미지 사이즈 객체
image_sizes = [

    # only even
    # (1916, 1076),
    # (1918, 1078),
    # (1920, 1080),
    # (1922, 1082)

    # even + odd
    (1918, 1078),
    (1919, 1079),
    (1920, 1080),
    (1921, 1081)

]

# for size in image_sizes:

#     mat = np.zeros((size[1], size[0], 3), dtype=np.uint8)
#     center = (size[0] // 2, size[1] // 2)
#     print(center)

#     cv2.circle(mat, center, 50, (0, 255, 0), thickness=4)
#     cv2.circle(mat, center, 5, (0, 255, 0), thickness=-1)

#     cv2.putText(mat, str(center), (center[0] + 50, center[1] - 50),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

#     dst = cv2.resize(mat, (1920, 1080))
#     print(dst.shape)
#     cv2.putText(dst, str(size) + " : odd + even", (200, 200),
#                 cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
#     filename = f"odd_{size[0]}x{size[1]}.png"

#     cv2.namedWindow("test", cv2.WINDOW_NORMAL)
#     cv2.imshow("test", dst)
#     # cv2.moveWindow("test", 0, 0)
#     cv2.waitKey(0)
#     cv2.imwrite(filename, dst)
#     print(f"Saved {filename}")


def png_to_gif():
    image_paths = glob.glob('*.png')

    images = []

    for image_path in image_paths:
        image = imageio.imread(image_path)
        images.append(image)

    output_path = 'center.gif'
    imageio.mimsave(output_path, images, duration=0.5)


png_to_gif()
