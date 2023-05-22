import cv2
import math

image_path = "image.png"
image = cv2.imread(image_path)

h, w = image.shape[:2]
target_x = int(w/2)
target_y = int(h/2)

print('target', target_x, target_y)
scale = 1.0
aspect = w/h
sum = 0
cnt = 0


def find_optimum(w, h):
    print('find optimun')
    new_w = 0
    new_h = 0
    temp1 = 0
    temp2 = 0

    aspect_ratio = 1.77777
    if w/h > aspect_ratio:
        new_w = w - 2
        new_h = h
        temp1 = new_w/new_h

        new_w = w
        new_h = h+2
        temp2 = new_w/new_h

        if abs(temp1-aspect_ratio) < abs(temp2-aspect_ratio):
            return w-2, h
        else:
            return w, h+2
    else:
        new_w = w+2
        new_h = h
        temp1 = new_w/new_h

        new_w = w
        new_h = h-2
        temp2 = new_w/new_h

        if abs(temp1-aspect_ratio) < abs(temp2-aspect_ratio):
            return w+2, h
        else:
            return w, h-2

    return new_w, new_h


while True:
    # print('scale', scale)
    # 소수점 버리고 짝수로 변환
    new_w = math.floor(w/scale)
    new_h = math.floor(h/scale)
    if new_w % 2 != 0:
        new_w += 1
    if new_h % 2 != 0:
        new_h += 1

    # aspect_ratio 값과 현재 바뀐 이미지 사이즈 비율간의 차이가 일정 값보다 큰 경우 최적화 진행
    diff_ratio = new_w/new_h - aspect
    if abs(diff_ratio) > 0.005:
        print('diff ratio ', diff_ratio)
        new_w, new_h = find_optimum(new_w, new_h)

        diff_ratio = new_w/new_h - aspect
        print('after diff ratio ', diff_ratio)
        print('------------------------------')
    sum += diff_ratio

    left = target_x - int(new_w/2)
    top = target_y - int(new_h/2)
    wid = left + int(new_w)
    hei = top + int(new_h)

    cv2.circle(image, (target_x, target_y), 5, (0, 255, 0), -1)

    # print('check new center ', left + new_w/2, top + new_h/2)  # 센터가 흔들리는지 확인
    zoomed = image[top:hei, left:wid]
    resized = cv2.resize(
        zoomed, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_CUBIC)
    # cv2.circle(image, (target_x, target_y), 3, (0, 255, 0), -1)
    # cv2.rectangle(image, (left, top), (wid, hei), (0, 200, 0), 2)
    # cv2.imshow("Image", image)

    cv2.imshow("Image", resized)

    cv2.waitKey(100)

    scale += 0.1
    if scale > 6:
        break
    cnt += 1

cv2.destroyAllWindows()


mean = sum / cnt
print('mean ', mean)
