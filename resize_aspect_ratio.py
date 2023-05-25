import cv2
import math

# target_x = int(w/2)
# target_y = int(h/2)
target_x = 900
target_y = 400


def mouse_callback(event, x, y, flags, param):
    global target_x, target_y
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"마우스 클릭 좌표: ({x}, {y})")
        target_x = x
        target_y = y


image_path = "image.png"    # input image path here
image = cv2.imread(image_path)

target_win = "click target pos"
cv2.namedWindow(target_win)
cv2.moveWindow(target_win, 0, 0)

image_win = "Image"
cv2.namedWindow(image_win)


def click_target():
    cv2.setWindowProperty(target_win, cv2.WND_PROP_TOPMOST, 1)
    cv2.setMouseCallback(target_win, mouse_callback)
    cv2.imshow(target_win, image)

    cv2.waitKey(0)
    print('target', target_x, target_y)


h, w = image.shape[:2]
scale = 1.0
aspect_ratio = w/h
sum = 0
cnt = 0

# set parameters
max_scale = 5


#  resize test
click_target()

while True:

    new_w = int(w*scale)
    new_h = int(h*scale)

    resized = cv2.resize(image, (new_w, new_h), cv2.INTER_LINEAR)

    left = target_x*scale - w/2
    top = target_y*scale - h/2
    print(left, top)

    if (left + w) > new_w:
        left = left - ((left + w) - new_w)
    elif left < 0:
        left = 0

    if (top + h) > new_h:
        top = top - ((top + h) - new_h)
    elif top < 0:
        top = 0

    print(left, top)
    crop = resized[int(top): int(top+h), int(left): int(left+w)]

    if scale == 1.0:
        cv2.namedWindow(image_win)
        cv2.setWindowProperty(image_win, cv2.WND_PROP_TOPMOST, 1)

    cv2.imshow(image_win, crop)
    cv2.waitKey(50)

    scale += 0.1

    if scale > max_scale:
        cv2.destroyWindow(image_win)
        scale = 1.0
        click_target()
        # break
    cnt += 1


while True:

    new_w = int(w*scale)
    new_h = int(h*scale)

    crop_x = 0
    crop_y = 0
    crop_w = 0
    crop_h = 0

    if w/2 > target_x:
        crop_w = target_x * 2
        crop_x = 0
    else:
        crop_w = (w-target_x)*2

    if h/2 > target_y:
        crop_h = target_y*2
        crop_y = 0
    else:
        crop_h = (h-target_y)*2

    if crop_w/crop_h > aspect_ratio:
        crop_w = int(crop_h*aspect_ratio)
    else:
        crop_h = int(crop_w/aspect_ratio)

    crop_x = int(target_x - crop_w*0.5)
    crop_y = int(target_y - crop_h*0.5)
    print(crop_x, crop_y, crop_w, crop_h)

    target_crop = image[crop_y:crop_y+crop_h, crop_x:crop_x+crop_w]

    resized = cv2.resize(target_crop, (new_w, new_h), cv2.INTER_LINEAR)

    left = int((new_w - w)/2)
    top = int((new_h-h)/2)
    right = left+w
    bottom = top+h

    if new_w != w:
        crop = resized[top:bottom, left:right]
    else:
        crop = resized

    if scale == 1.0:
        print('check')
        cv2.rectangle(image, (crop_x, crop_y),
                      (crop_w+crop_x, crop_h+crop_y), (0, 255, 0), 3)
        cv2.imshow(target_win, image)
        cv2.waitKey(0)

        cv2.namedWindow(image_win)
        cv2.setWindowProperty(image_win, cv2.WND_PROP_TOPMOST, 1)

    cv2.imshow(image_win, crop)
    cv2.waitKey(50)

    scale += 0.1

    if scale > max_scale:
        cv2.destroyWindow(image_win)
        scale = 1.0
        click_target()
        # break
    cnt += 1

cv2.destroyAllWindows()
