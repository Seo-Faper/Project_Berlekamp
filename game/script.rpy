# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.

image yuri idle = "char/원주민/코딩_신.png"
image chuhee idle ="char/chuhee/chuhee_idle.png"
image yujin idle = "char/yuri/yuri_idle.png"
image snowtown = "bg/snowtown.png"
image forest = "bg/forest.png"
image city = "bg/city.png"
define e = Character('유리', color="#acaea4")
define j = Character('유진', color="#ffffff")
define r = Character('추희', color="#ffffff")
init python:
    class Player:
        def __init__ (self, name, lv, hp):
            self.name = name
            self.lv = lv
            self.hp = hp



# 여기에서부터 게임이 시작합니다.
screen set_name(title, init_name):
    frame:
        xpadding 200
        ypadding 200
        xalign 1
        yalign 0.5
        vbox:
            xalign 0
            yalign 0
            spacing 50
            text title
            input default init_name


label start:
    scene city:
    "아 취업 준나 안되네. 흠"
    "코딩 부트캠프나 한번 조지고 개발자 취업해 볼까."
    "요즘 개발자가 핫하던데."
    "엇, 이게 뭐야, 벌레캠프? 코딩 교육 부트캠프라고?"
    "숙식 지원에 노트북 지원.."
    "게다가 다른 유명한 부트캠프보다 가격도 훨씬 싸잖아."
    "헉, 마감 임박?! 15분전?" with vpunch
    "일단 신청하고 봐야겠다-!"
    scene forest:
    show yuri idle at center:
        yalign 100
    e "저는 벌레캠프의 원주민이자 관리자, 유리라고 합니다."
    e "우선 벌레캠프에 지원하신 지원자 분들 반갑습니다."
    e "앞으로 여러분은 이 섬에서 생존하게 될 것 입니다."
    e "사전에 공지한 대로 교육 기간 동안에 외부와의 통신은 일절 금지되며,\n그 어떤 연락도 할 수 없습니다."
    e "저희가 지급한 노트북으로 인트라넷에 연결 할 수 있습니다."
    e "인터넷 검색 없이, 자동완성 ide 없이 코딩을 진행해 주시면 됩니다."
    e "또한, 그 곳에서 생존에 필요한 식량이나 물품을 구매 가능 합니다."
    e "그럼 행운을 빕니다."
    hide yuri with fade
    "잠깐.. 갑자기 이렇게 무인도에 떨궈놓고 사라지는게 어딧어?"
    "..."
    "일단 주변을 둘러봐도 진짜 숲 밖에 없네.."
    "말도안돼!!"
    "여기서 내보내줘!!" with vpunch
    show chuhee idle at left with dissolve:
        yalign 100
    r "아야야.. 아파라.."
    hide yuri with dissolve
    show chuhee idle at center with dissolve:
        yalign 100
    r "이봐, 당신! 사람을 쳤으면 사과 먼저 해야 하는 거 아냐?"
    "죄송합니다."
    "조그매서 못봤네."
    r "..됐어. 사과 대신에"
    r "식사 배급을 위해 A부터 F까지 6개 조에 대한 배급 순서를 정하려고 한다."
    r "모든 가능한 배급 순서를 알파벳 순서로 나열해보면\nA,B,C,D,E,F부터 F,E,D,C,B,A까지 총 720가지가 있는데,"
    r "그 중 C,B,A,D,E,F는 몇 번째일까?"
    r "쉽지?"
    window hide
    hide chuhee
    #$ name = renpy.call_screen("set_name",title="tutorial.py", init_name="")
    menu:
        "제가 그걸 어떻게 알죠?":
            show chuhee idle at left:
                yalign 100
            r "하, 진짜 심각하네. "
            r "이 정돈 무리 없이 알아야 할 텐데."
            r "이런 간단한 문제도 풀지 못 하면 오늘 저녁은 쫄쫄 굶어야 할 걸."
            "아니.."
        "훗, 정답은 1, 0, -1 중 하나 입니다.":
            show yujin idle at right:
                yalign 100
            j "병신인가?"
            j "이런 사람이 어떻게 여기 온 거지?"
            show chuhee idle at left:
                yalign 100
            r "저기요, 제가 먼저 말하고 있잖아요."
            r "끼어들지 마시죠?"
            "이 학생들도 참가자인 건가?"

    return
