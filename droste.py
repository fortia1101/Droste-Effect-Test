import cv2
import matplotlib.pyplot as plt
import random


capture = cv2.VideoCapture(1)
#引数はコンピュータに接続されているカメラの数に対応する番号（1台なら0、複数台なら1）
count = 0
#色付き四角形の更新の頻度をいじれる変数
random_color = [(0, 255, 0), (0, 0, 25), (255, 0, 0),
                (0, 242, 255), (0, 153, 255), (221, 255, 0),
                (255, 0, 127), (193, 182, 255)]
#色のリスト
choice = random.sample(random_color, 4)
#色のリストから任意の要素数に絞ったリストを選択


while True:
    ret, frame = capture.read()
    #1フレーム分の画像データをframeに代入
    #retは画像が格納されているかいないかを表す（格納されている：True、されてない：False）
    frame = cv2.resize(frame, dsize=(640, 480))
    if ret == False:
        break
    cv2.rectangle(frame, pt1=(50, 50), pt2=(150, 150), color=choice[0], thickness=-1)
    cv2.rectangle(frame, pt1=(50, 330), pt2=(150, 430), color=choice[1], thickness=-1)
    cv2.rectangle(frame, pt1=(490, 330), pt2=(590, 430), color=choice[2], thickness=-1)
    cv2.rectangle(frame, pt1=(490, 50), pt2=(590, 150), color=choice[3], thickness=-1)
    #rectangle(長方形)の生成
    #pt1：左下の頂点の座標、pt2：右上の頂点の座標

    if count == 10:
        choice = random.sample(random_color, 4)
        count = 0

    cv2.imshow('Video', frame)
    #第一引数は開くフレーム名
    count += 1

    k = cv2.waitKey(1)
    #キーボード入力を処理する
    #引数はミリ秒単位で入力待ち時間を表す
    if k == 27:
        print(frame.shape[:2][::-1])
        #sequence[start:stop:step]
        print(type(frame[0][0][0]))
        print(frame)
        break
        

capture.release()
cv2.destroyAllWindows()
