# resize_center_check


## This is

This code was created to detect the shaking of the center when resizing the image (zoom), and to record the findings during debugging.


-----------------------
## example 

```
# image size -> center point

(1921, 1081) -> (960, 540)  // same 1
(1920, 1080) -> (960, 540)  // same 1
(1919, 1079) -> (959, 539)  // same 2
(1918, 1078) -> (959, 539)  // same 2

```
🤔
The image size is different, but the center point is the same?!


Let`t check in the python opencv!


---------------------------
## Test
![center](https://github.com/HeynaPark/resize_center_check/assets/90448406/a3d2278a-4148-4695-95ef-85053147901a)


    - only even size
    (1916, 1076),
    (1918, 1078),
    (1920, 1080),
    (1922, 1082)

    - even + odd size
    (1918, 1078),
    (1919, 1079),
    (1920, 1080),
    (1921, 1081)

## Result
- This is the result of displaying the center points of images of different sizes and resizing them to 1920 and 1080.

- When the image size is an even number, the center point does not shake, but when there are both even and odd numbers, it shakes. (Slight but shakes!)
