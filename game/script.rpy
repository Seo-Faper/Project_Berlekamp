# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.

image yuri idle = "char/원주민/코딩_신_도트.png"
image chuhee idle ="char/chuhee/chuhee_idle.png"
image chuhee smail ="char/chuhee/chuhee_smail.png"
image chuhee happy ="char/chuhee/chuhee_happy.png"
image yujin idle = "char/yuri/yuri_idle.png"
image yujin angry = "char/yuri/yuri_angry.png"
image yujin surp = "char/yuri/yuri_surp.png"
image snowtown = "bg/snowtown.png"
image forest = "bg/forest.png"
image city = "bg/city.png"
define e = Character('유리', color="#acaea4")
define j = Character('유진', color="#ffffff")
define r = Character('추희', color="#ffffff")
define sys = Character('System', color="#ffffff")
init python:
    class Player:
        def __init__ (self, name, lv, hp):
            self.name = name
            self.lv = lv
            self.hp = hp


init python:
    show_inventory = False
    def inventory_button():
        if show_inventory:
            ui.vbox(spacing=100, xalign=0.99, yalign=0.01)
            # 인벤토리 이미지 버튼
            # click시 show_item_list label 호출
            ui.imagebutton("interactive/laptop0.png", 
            clicked=renpy.curried_call_in_new_context("show_item_list"))
            ui.close()

    # 오버레이에 추가
    config.overlay_functions.append(inventory_button)
label show_item_list:
# item list screen 호출
    call screen sc_item_list

screen sc_item_list:

    imagemap:
        auto "bg/menu_%s.png"
        hotspot(56, 110, 128, 96) action Return("intra")
        hotspot(243, 105, 128, 111) action Return("cart")
        hotspot(431, 90, 132, 128) action Return("rank")


# 여기에서부터 게임이 시작합니다.
screen set_name(title, init_name):
    frame:
        xpadding 1280
        ypadding 720
        xalign 1
        yalign 0.5
        vbox:
            xalign 0
            yalign 0
            spacing 50
            text title
            input default init_name

label end:
    "끝"
    return
label start:
    scene city:
    "아 취업 준나 안되네."
    "코딩 부트캠프나 한번 조지고 개발자 취업해 볼까."
    "요즘 개발자가 핫하던데."
    "엇, 이게 뭐야, 벌레캠프? 코딩 교육 부트캠프라고?"
    "숙식 지원에 노트북 지원.."
    "게다가 다른 유명한 부트캠프보다 가격도 훨씬 싸잖아."
    "헉, 마감 임박?! 15분전?" with vpunch
    "일단 신청하고 봐야겠다-!"
    nvl_narrator "그렇게 갑자기 왠 무인도로 끌려가게 된다."
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
    show chuhee idle at center:
        yalign 100
        ease 0.5 xalign 0.5 

    r "이봐, 당신! 처음 보는 얼굴인데, 것 보다 사람을 쳤으면 사과 먼저 해야 하는 거 아냐?"
    "죄송합니다."
    "(뭐야, 조그매서 못봤네.)"
    r "..됐어. 사과 대신에"
    r "두 자연수 A와 B가 주어진다."
    r "이때, A+B, A-B, A*B, A/B(몫), A\%B(나머지)를 출력하는 프로그램을 작성하시오. "
    r "단, (1 <= A, B <= 10,000)"
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
            r "이런 간단한 문제도 풀지 못 하면 당장 오늘 저녁은 쫄쫄 굶어야 할 걸."
            "아니.."

        "훗, 정답은 1, 0, -1 중 하나 입니다.":
            show yujin idle at right :
                yalign 100
            j "병신인가?"
    show yujin idle at right:
            yalign 100
    j "이런 사람이 어떻게 여기 온 거지?"
    show chuhee idle at left:
            yalign 100
    r "저기요, 제가 먼저 말하고 있잖아요."
    r "끼어들지 마시죠?"
    "이 학생들도 참가자인 건가?"

    show yujin angry at right:
            yalign 100 
    j "넌 뭐야? "
    j "혹시 죽여달란 말을 빙빙 돌려 말하는 건가?"
    "(뭐야.. 왜 이렇게 화가 나 있는 거지?)"
    r "흥, 자기가 코딩 허접이라서 틀려 놓고선 왜 엄한데 화풀이 신지?"
    r "남한테 화풀이 할 시간에 자기 코드나 풀이 하는게?"
    show chuhee happy at left:
            yalign 100
    r "뭐, 본인한테 정 어려우면 제가 살짝 도와줄 수도 있고."
    r "물론 하는 거 봐서."
    show yujin surp at right:
            yalign 100
    j "코.. 코딩 허접?"
    j "너 지금 대한민국 최고 알고리즘 대회를 최연소로 우승하고."
    j "코딩 특기자 전형으로 아시아 최고의 공대에 합격한 사람을 허접이라고 한 거야?"
    show chuhee smail at left:
            yalign 100
            ease 0.1 xalign 0.05
            ease 0.1 xalign -0.05
            ease 0.1 xalign 0.05
            ease 0.1 xalign -0.05
    r "푸하하하! 본인 입으로 대한민국 최고 알고리즘 대회 우승자~? 부끄러워라."
    r "그리고 너 말이야, 여기서 그렇게 대회에 우승했다느니."
    r "어디에 당당하게 합격했다느니 하는건 말이야."
    r "그저 `난 우리 엄마의 자랑스러운 딸이다` ~라고 자랑하는 거나 다를 바가 없다는 거 알아?"
    show yujin angry at right:
            yalign 100 
    j "......."
    j "너 두고 봐."
    j "흥."
    show yujin angry at right:
            yalign 100 
            ease 0.5 xalign -0.8 
    show chuhee happy at center:
        yalign 100
        ease 0.5 xalign 0.5 
    r "아~ 간만에 웃었네."
    "..."
    "저기, 대한민국 최고의 알고리즘 대회에 아시아 최고 공대면 엄청난 거 아냐?"
    r "물론 대단하지."
    r "유진이는 내 어릴적 친구야."
    r "나랑 다른 고등학교를 가게 됐던 건 안타깝지만.."
    r "그래도 여기서 만났으니 잘된 거지!"
    r "누구보다 우월했고, 잘난맛에 살아왔지만."
    r "어느세 부터인가 그저 어른들의 만들어놓은 시시한 틀에만 갇히게 됐달까?"
    "..의미를 모르겠네."
    r "뭐, 됐어. "
    r "너도 일단 여기 들어왔다는 것 부터 한 따까리 한다는 뜻일테니."
    r "알아서 잘 살아남아봐."
    r "그럼 난 풀던 문제가 있어서 이만. 덕분에 환기 잘 했어."
    hide chuhee with fade
    "사라졌네.."
    "난 그저 운이 좋아서 합격한 것 뿐이라고.."
    "그마저도 이런 곳인 줄 알았으면 신청도 안 했을 텐데.."
    "막막하다. 곧 어두워질 것 같은데."
    "배도 고프고.."
    "일단 아까 지급 받은 노트북이라도 펼쳐볼까."
    sys "노트북이 해금되었습니다."
    $ show_inventory = True
    jump end

    return
