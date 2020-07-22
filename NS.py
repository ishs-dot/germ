import turtle as t
import random as r
import time

def place_germ(num_white, num_black):
    global death_white
    global death_black
    global death_list
    global list
    global rad
    num_total = num_white + num_black
    list = [r.randint(-200+rad*2, 200-rad*2) for i in range(2*num_total)]
    for i in range(num_total) :
        if i+1 <= num_white :
            t.color('white')
            if not((50+rad <= list[2*i]%100 <= 100-rad and rad<= (list[2*i+1])%100 <= 50-rad) or (50+rad <= list[2*i+1]%100 <= 100-rad and rad<= (list[2*i])%100 <= 50-rad)) :
                death_white += 1
                death_list.append(i)
        elif i+1 > num_white :
            t.color('black')
            if ((rad <= list[2*i]%100 <= 50-rad and rad<= (list[2*i+1])%100 <= 50-rad) or (50+rad <= list[2*i+1]%100 <= 100-rad and 50+rad<= (list[2*i])%100 <= 100-rad)) :
                death_black += 1
                death_list.append(i)
        t.goto(list[2*i], list[2*i+1]-rad)
        t.pendown()
        t.begin_fill()
        t.circle(rad)
        t.end_fill()
        t.penup()
            
def mainboard(length, n):
    t.speed(0)
    t.delay(0)
    t.penup()
    t.ht()
    t.colormode(255)
    t.tracer(0, 0)
    t.title('Natural Selection Simulation - Antimicrobial Resistance')
    t.color(250, 250, 250)
    for i in range(-n, n) :
        for j in range(-n, n) :
            t.goto(i*length, j*length+50)
            t.pendown()
            if (i+j)%2 == 0 : t.fillcolor(170, 170, 170)
            elif (i+j)%2 == 1 : t.fillcolor(220, 220, 220)
            t.begin_fill()
            for k in range(4) :
                t.forward(length)
                t.right(90)
            t.end_fill()
            t.penup()
    t.tracer(3, 0)

def printinfo(i):
    global survive_white
    global survive_black
    global death_white
    global death_white
    t.goto(-300, 300)
    t.color(255, 255, 255)
    t.begin_fill()
    for j in range(2):
        t.forward(600)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()
    t.color(0, 0, 0)
    stage = str(i) + '세대'
    t.goto(-200, 270)
    t.write(stage, move=False, align="left", font=("맑은 고딕", 10, "normal"))
    msg1 = '현재 야생형 균주 수 : ' + str(survive_white)
    t.goto(-200, 250)
    t.write(msg1, move=False, align="left", font=("맑은 고딕", 10, "normal"))
    msg2 = '현재 내성 균주 수 : ' + str(survive_black)
    t.goto(-200, 230)
    t.write(msg2, move=False, align="left", font=("맑은 고딕", 10, "normal"))
    msg3 = '사멸할 야생형 균주 수 : ' + str(death_white)
    t.goto(0, 250)
    t.write(msg3, move=False, align="left", font=("맑은 고딕", 10, "normal"))
    msg4 = '사멸할 내성 균주 수 : ' + str(death_black)
    t.goto(0, 230)
    t.write(msg4, move=False, align="left", font=("맑은 고딕", 10, "normal"))
    t.goto(-200, -240)
    t.write('자동 진행 중', move=False, align="left", font=("맑은 고딕", 10, "normal"))
    t.goto(-200, -260)
    t.write('결과는 시뮬레이션 종료 후 그래프로 출력됩니다.', move=False, align="left", font=("맑은 고딕", 10, "normal"))

def highlight():
    global list
    global death_list
    global rad
    t.tracer(0, 0)
    t.color(255, 0, 0)
    for i in range(len(death_list)):
        j = death_list[i]
        t.goto(list[2*j], list[2*j+1]-rad)
        t.pendown()
        t.begin_fill()
        t.circle(rad)
        t.end_fill()
        t.penup()
    t.color(0, 0, 0)
    t.tracer(3, 0)

def datareset():
    global list
    global death_list
    del list
    del death_list
    list = []
    death_list= []

def germupdate():
    global survive_white
    global survive_black
    global death_white
    global death_black
    global result
    result.append(survive_white)
    result.append(survive_black)
    survive_white -= death_white
    survive_white *= 2
    survive_black -= death_black
    survive_black *= 2
    death_white = death_black = 0

def screenclear(i):
    if i != 9:
        t.reset()
        t.speed(0)
        t.delay(0)
        t.penup()
        t.ht()
        t.colormode(255)
        t.color(0, 0, 0)
        t.goto(-80, 240)
        t.write('정보 업데이트 중입니다...', move=False, align="left", font=("맑은 고딕", 10, "normal"))
    elif i == 9:
        t.color(255, 0, 0)
        t.goto(-193, 320)
        t.write('시뮬레이션 종료. 잠시 후 결과 화면으로 이동합니다.', move=False, align="left", font=("맑은 고딕", 12, "normal"))
        t.color(0, 0, 0)
        

def drawgraph():
    global result
    t.clearscreen()
    t.ht()
    t.delay(0)
    t.speed(0)
    t.penup()
    t.colormode(255)
    k = 1 + max(result)//50
    t.seth(0)
    for i in range(5):
        t.goto(-243, 40*i-280)
        t.pendown()
        t.forward(500)
        t.penup()
    
    t.seth(90)
    for i in range(11):
        t.goto(-243+50*i, -280)
        t.pendown()
        t.forward(160)
        t.penup()
        
    for i in range(1, 10):
        t.goto(-220+50*i, -150)
        t.write(str(i), move=False, align="left", font=("맑은 고딕", 12, "normal"))
    t.color(255, 0, 0)
    t.goto(-233, -190)
    t.write('야생', move=False, align="left", font=("맑은 고딕", 12, "normal"))
    t.color(0, 0, 255)
    t.goto(-233, -230)
    t.write('내성', move=False, align="left", font=("맑은 고딕", 12, "normal"))
    t.color(0, 0, 0)
    t.goto(-233, -270)
    t.write('전체', move=False, align="left", font=("맑은 고딕", 12, "normal"))

    for i in range(9):
        t.goto(-178+50*i, -190)
        t.write(str(result[2*i]), move=False, align="left", font=("맑은 고딕", 10, "normal"))
        t.goto(-178+50*i, -230)
        t.write(str(result[2*i+1]), move=False, align="left", font=("맑은 고딕", 10, "normal"))
        t.goto(-178+50*i, -270)
        t.write(str(result[2*i]+result[2*i+1]), move=False, align="left", font=("맑은 고딕", 10, "normal"))

    ####### 그래프 틀
    for i in range(1):
        t.penup()
        t.goto(-150, -50)
        t.seth(90)
        t.pendown()
        t.forward(300)
        t.right(135)
        t.forward(10)
        t.penup()
        t.goto(-150, 250)
        t.pendown()
        t.right(90)
        t.forward(10)
        t.penup()
        t.goto(-150, -50)
        t.seth(0)
        t.pendown()
        t.forward(300)
        t.right(135)
        t.forward(10)
        t.penup()
        t.goto(150, -50)
        t.pendown()
        t.right(90)
        t.forward(10)
        t.penup()
        t.goto(-170, 250)
        t.write('개체 수', move=False, align="left", font=("맑은 고딕", 10, "normal"))
        t.goto(160, -58)
        t.write('세대', move=False, align="left", font=("맑은 고딕", 10, "normal"))
        t.seth(90)
        for i in range(1, 10):
            t.goto(30*i-152, -78)
            t.write(str(i), move=False, align="left", font=("맑은 고딕", 10, "normal"))
            t.goto(30*i-150, -58)
            t.pendown()
            t.forward(12)
            t.penup()
        t.seth(0)
        for i in range(1, 10):
            t.goto(-192, 30*i-60)
            t.write(str(5*k*i), move=False, align="left", font=("맑은 고딕", 10, "normal"))
            t.goto(-158, 30*i-50)
            t.pendown()
            t.forward(16)
            t.penup()

    ######## 그래프 내용
        t.colormode(255)
        t.color(255, 0, 0)
        t.penup()
        for i in range(9):
            t.goto(-150+30*(i+1), (-50+int(270*(result[2*i]/(9*5*k)))))
            t.pendown()
        t.color(0, 0, 255)
        t.penup()
        for i in range(9):
            t.goto(-150+30*(i+1), (-50+int(270*(result[2*i+1]/(9*5*k)))))
            t.pendown()
        t.color(0, 0, 0)
        t.penup()
        t.ht()
        t.speed(0)
        t.pensize(2)
        for i in range(9):
            t.goto(-150+30*(i+1), (-50+int(270*(result[2*i]+result[2*i+1])/(9*5*k))))
            t.pendown()
        t.penup()
        t.pensize(1)
        t.color(0, 0, 0)
        t.goto(-143, -340)
        t.write('결과를 기록하신 후 이 창을 닫아 주세요.', move=False, align="left", font=("맑은 고딕", 12, "normal"))
    
######### main
death_white = death_black = 0        
survive_white = 25
survive_black = 5
result = []
list = []
death_list = []
rad = 8
print('코드는 깃허브의 해당 프로젝트 계정 \'ishs-dot\'에서 보실 수 있습니다.')
print('잠시 후 시뮬레이션이 시작됩니다...')
for i in range(9):
    mainboard(50, 4) #입력값 절대 수정하지 말 것
    datareset()
    place_germ(survive_white, survive_black)
    printinfo(i+1)
    germupdate()
    time.sleep(0.5)
    t.goto(-120, -239)
    t.write('▶', move=False, align="left", font=("맑은 고딕", 10, "normal"))
    highlight()
    for j in range(3):
        t.goto(-120+15*j, -239)
        t.write('▶', move=False, align="left", font=("맑은 고딕", 10, "normal"))
        time.sleep(0.5)
    screenclear(i+1)
time.sleep(2)
drawgraph()
print()
print('시뮬레이션 창을 닫으시면 이 창도 함께 닫힙니다.')
t.mainloop()
