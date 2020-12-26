'''
@info:This is a project for physics lesson
@author: 伍竣義 B10917002 四資工一A
@date 12/26/20
'''
from vpython import *
import numpy as np

def main():
    '''
     1. 參數設定, 設定變數及初始值
    '''
    size = 0.15  # 球體半徑 (m)
    FloorLength = 100 # 場地大小
    Gravity = 9.8 # 重力加速度 (m/s^2)
    dt = 0.0005  # time grid

    '''
     2. 畫面設定
    '''
    scene = canvas(title = 'Physics Project', width = 800, height = 600, x = 0, y = 0, center = vec(0, 5, 0),
                   background = vec(0, 0.6, 0.6))
    floor = box(pos = vec(0, 0, 0), size = vec(FloorLength, 0.1,10), color = color.blue)

    #彙整資料並寫入標題
    with open('data03.csv', 'w', encoding = 'UTF-8') as file:
        file.write('theta(degree),Height(m),v0(m/s),t(s),x(m)\n')
    #根據知名學者許樹淵也提過理想的推擲角度約為 38°到 43°之間 所以測試範圍我設為30~50度之間以便觀測
    #高度設定我參考了參考來源2裡的表格 設為1.8 ~ 2.4 m 之間
    #初始速度一樣參考來源2的表格 設為9 ~ 14 m/s 之間
    for degree in np.arange(30,51,1): #起始角度設定

        theta =  radians(degree) #拋射角度

        for Height in np.arange(1.8,2.5,0.1): # 拋鉛球選手將球體拋出起始位置
            for v0 in np.arange(9,15,1): #拋射初速度
                t = 0 #重新初始時間
                ball = sphere(pos = vec(-FloorLength / 2, Height, 0), radius = size, color = color.red, make_trail = True,
                              v = vec(v0 * cos(theta), v0 * sin(theta), 0), a = vec(0, -Gravity, 0)) #球體設定

                '''
                 3. 物體運動, 當物體接觸地面即停止
                '''
                while (ball.pos.y - floor.pos.y >= size):
                    #rate(5000)
                    ball.v += ball.a * dt
                    ball.pos += ball.v * dt
                    # xt.plot(pos =(t,ball.pos.x+FloorLength/2))
                    # yt.plot(pos = (t, ball.pos.y+Height))
                    # vt.plot(pos = (t, ball.v))
                    t += dt
                print(str(round(degree,3)) + ','+str(round(Height,3))+ ',' + str(round(v0,3)) + ',' + str(round(t,3)) + ',' + str(round(ball.pos.x+FloorLength/2,3)) + '\n')
                with open('data03.csv', 'a', encoding = 'UTF-8') as file:
                    file.write(str(round(degree,3)) + ','+str(round(Height,3))+ ',' + str(round(v0,3)) + ',' + str(round(t,3)) + ',' + str(round(ball.pos.x+FloorLength/2,3)) + '\n')

        # gd = graph(title = 'x-t plot', width = 600, height = 450, x = 0, y = 600, xtitle = 't(s)', ytitle = 'x(m)')
        # gd2 = graph(title = 'v-t plot', width = 600, height = 450, x = 0, y = 1050, xtitle = 't(s)', ytitle = 'y(m)')
        # gd3 = graph(title = 'y-t plot', width = 600, height = 450, x = 0, y = 1050, xtitle = 't(s)', ytitle = 'v(m/s)')
        # xt = gcurve(graph = gd, color = color.red)
        # yt = gcurve(graph = gd3, color = color.red)
        # vt = gcurve(graph = gd2, color = color.red)







if __name__ == '__main__':
    main()


'''
    reference:
        https://github.com/YiZheWangTw/VPythonTutorial 王一哲教師教學網站上的源碼 讓我對於vpython用法可以直接上手
        https://www.shs.edu.tw/works/essay/2008/10/2008103009195010.pdf 拋球運動原理
'''