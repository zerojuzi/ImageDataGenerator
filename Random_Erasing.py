
import random
import math
import cv2

def RandomErasing(img):
    probability = 1
    sl = 0.02
    sh = 0.4
    r1 = 0.3
    mean = [0.4914, 0.4822, 0.4465]

    if random.uniform(0, 1) > probability:
        return img

    for attempt in range(100):
        area = img.shape[0] * img.shape[1]
        target_area = random.uniform(sl, sh) * area
        aspect_ratio = random.uniform(r1, 1 / r1)

        h = int(round(0.8*math.sqrt(target_area * aspect_ratio)))
        w = int(round(0.8*math.sqrt(target_area / aspect_ratio)))

        if w < img.shape[1] and h < img.shape[0]:
            x1 = random.randint(0, img.shape[0] - h)
            y1 = random.randint(0, img.shape[1] - w)
            if img.shape[2] == 3:
                img[x1:x1 + h, y1:y1 + w,0] = mean[0]
                img[x1:x1 + h, y1:y1 + w,1] = mean[1]
                img[x1:x1 + h, y1:y1 + w,2] = mean[2]
            else:
                img[ x1:x1 + h, y1:y1 + w,0] = mean[0]
            return img

    return img
j=1
for j in range(1,47):

    for k in range(1,21):
        fname = './data/' + str(j) + '.jpg'
        print(fname)
        img = cv2.imread(fname)
        img=RandomErasing(img)
        cv2.imwrite('./data2/'+str(j)+'_'+str(k)+'.jpg',img)

