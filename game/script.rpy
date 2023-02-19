# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.

image yuri idle = "char/원주민/코딩_신_도트.png"
image maid idle = "char/원주민/코딩_노예.png"
image prinses idle = "char/원주민/코딩공주_사복.png"
image chuhee idle ="char/chuhee/chuhee_idle.png"
image chuhee smail ="char/chuhee/chuhee_smail.png"
image chuhee happy ="char/chuhee/chuhee_happy.png"
image yujin idle = "char/yuri/yuri_idle.png"
image yujin smail = "char/yuri/yuri_smail.png"
image yujin angry = "char/yuri/yuri_angry.png"
image yujin surp = "char/yuri/yuri_surp.png"
image snowtown = "bg/snowtown.png"
image forest = "bg/forest.png"
image city = "bg/city.png"
image hotel = "bg/hotel.png"
define e = Character('유리', color="#acaea4")
define j = Character('유진', color="#ffffff")
define r = Character('추희', color="#ffffff")
define m = Character('코딩 노예', color="#00ff00")
define p = Character('오리아나', color="#5BC0F8")
define sys = Character('System', color="#ffffff")
define pov = Character("[povname]", color="#FDA769")
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
    if _return is "intra":
        sys "인트라넷에 접속합니다."
        jump show_item_list
    elif _return is "cart":
        sys "물품 구매에 접속합니다."
        jump show_item_list
    elif _return is "rank":
        sys "현재 랭킹을 확인합니다."
        jump show_item_list


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
    r "식사 배급을 위해 A부터 F까지 6개 조에 대한 배급 순서를 정하려고 한다."
    r "이때, 가능한 발표 순서를 알파벳 순서로 나열해보면 \nABCDEF부터 FEDCBA까지 720가지가 있는데."
    r "그 중 CBADEF는 몇 번째인가?"
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
            j "미친놈인가?"
    show yujin idle at right:
            yalign 100
    j "잠깐 문제 안 풀려서 머리 식힐 겸 산책 나왔는데 \n별 신기한 광경을 다 보겠네."
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
    j "코딩 특기자 전형으로 아시아 최고의 공대에\n합격한 사람을 허접이라고 한 거야?"
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
    "저기, 대한민국 최고의 알고리즘 대회에 \n아시아 최고 공대면 엄청난 거 아냐?"
    r "물론 대단하지."
    r "유진이는 내가 어릴 때 부터 같이 지낸 친구야."
    r "나랑 다른 고등학교를 가게 됐던 건 안타깝지만.."
    r "그래도 여기서 만났으니 잘된 거지!"
    r "누구보다 우월했고, 잘난맛에 살아왔지만."
    r "어느세 부터인가 그저 어른들의 만들어놓은 시시한 틀에만 갇히게 됐달까?"
    "..의미를 모르겠네.. 이해할 수 없어."
    r "뭐, 됐어. "
    r "최고의 이해는 이해할 수 없음을 인정하는 거니까."
    r "너도 일단 여기 들어왔다는 것 부터 한 따까리 한다는 뜻일테니."
    r "알아서 잘 살아남아봐."
    r "그럼 난 풀던 문제가 있어서 이만. 덕분에 환기 잘 했어."
    hide chuhee with fade
    "사라졌네.."
    "난 그저 운이 좋아서 합격한 것 뿐이라고.."
    "그마저도 이런 곳인 줄 알았으면 신청도 안 했을 텐데.."
    "막막하다. 곧 어두워질 것 같은데."
    "배도 고프고.."
    "잠은 어디서 자야 하는 거지?"
    "분명 숙식지원에 노트북 지원이라고 했는데."
    show yuri idle at center:
        yalign 100
        ease 0.2 xalign 0.5
    e "지원자님!! 여기 계셨군요. 정말이지 한참 찾았네요!"
    e "아직 소개도 덜 했는데,\n잠시 자릴 비운사이에 바람처럼 사라지셔서.."
    e "전력 공급이 끊긴 휘발성 메모리(volatile memmory)인줄 알았어요!"
    e "그럼 숙소로 안내해 드리겠습니다."
    e "거기서 노트북 지급과 미리 와 계신 다른 지원자분들도 만나보아요."
    scene black with dissolve

    show text "Chapter 01\n\nGreedy쟁이 그녀!" with Pause(2.5)

    scene black with dissolve
    scene hotel 
    "우왓, 이런 곳에 호텔이?"
    show maid idle at left:
        yalign 100
        ease 0.5 xalign 0.1
    m "처음 뵙겠습니다." 
    "(명찰에 코딩 노예라고 적혀져 있다. 당황스럽군.)"
    "(요즘 IT 기업에서는 실명 말고 별명으로 업무를 본다던데, \n그건가보다.)" 

    m "여긴 Vector 호텔입니다."
    m "저는 여기를 관리하는 직원 입니다만.."
    m "다른 분들께 지원자님을 소개하기 전에 지원자님을 뭐라고 부르면 될까요?"
    
    $ povname = renpy.input("내 이름은..", length=32)
    $ povname = povname.strip()
    if not povname:
        $ povname = "문지혁"
    if 44032 <= ord(povname[-1]) <= 55203:
        if (ord(povname[-1]) - 44032) % 28 == 0:
                pov "[povname]! 난 [povname]라고 해."
        else:
                pov "[povname]! 난 [povname]이라고 해."
    else:
        pov "[povname]! 내이름은 [povname]."
    m "좋습니다. [povname]님, 그럼 따라오시죠."
    show prinses idle at right:
            yalign 100
            ease 0.5 xalign 1.0 
    p "진례야! 큰일났어! "
    "(본명이 진례셨구나.)"
    m "아가씨, 제가 분명 회사에선 본명말고 넥네임으로.."
    p "그게 중요한게 아니고! 지금 Vector 호텔에 손님이 꽉 차버렸단 말이야!" 
    m "네에? 그게 어떻게 가능하지요? "
    m "Vector는 {b}{color=#820000}크기가 무한대인 배열{/color}{/b}인데 꽉 차버렸다구요?"
    m "그럼 손님이 무한대 명 오셨다는 거예요?"
    p "그렇다니까!!"
    m "그럼 [pov]님이 입주하실 방은 어쩌죠?"
    p "[pov]? 그게 누군데."
    m "지금 저랑 같이 오신, {color=#ABC270}프로젝트 벌레캠프{/color}의 참가자셔요."
    
    show prinses idle at right:
            yalign 100
            ease 0.1 xalign 0.9 
            ease 0.1 xalign 1.0 
            ease 0.1 xalign 0.9 
            ease 0.1 xalign 1.0 
    p "뭐.. 뭣? 벌레캠프 참가자라고? 분명 더 이상 안뽑는다고 했잖아!"
    m "확실히 그렇다고는 했지만.. 그 분들의 변덕은 알 수가 없으니까요.."
    p "하.. 어쩌지, 빈방이 구해질 때 까지만이라도 \n일단 다른 참가자분과 같은 방을 쓰게 하는게.."
    m "하지만 아가씨, 아시다시피.. 이번 기수 참가자분들은 전부.."
    show maid idle at left:
        yalign 100
        ease 0.5 xalign 0.0
    show yujin idle at center:
        xalign 2
        yalign 100
        ease 0.8 xalign 0.5
    j "다들 안들어가고 뭐해?"
    j "어라? 호텔 지배인 아가씨도 있네."
    show yujin angry at center:
        yalign 100
    j "아 맞아 잘 만났다, 너. 지금 호텔이 너무 시끄러워서 집중을 못하겠어."
    j "층간소음이 원래는 없었는데."
    m "유진님, 사실은 그게.."
    "현 상황을 털어놓는 코딩 노예"
    show yujin smail at center:
        yalign 100
    j "뭐야, 간단한 일이잖아."
    j "그럼 그냥.."
    p "역시 다른 참가자분들 중 한명과 일단 같은 방을 쓰는게.."
    j "지배인씨, 모든 방 사람들에게 {color=#FFC93C}\'2 * 자기 방 번호 + 1 호\'{/color} 로 방을 옮겨 달라고 방송해줘."
    m "와아, 역시!"
    p "오, 그렇게 하면 제일 첫번째 방을 비울 수 있는건 물론이고 \n또 무한대명의 손님이 와도 대처할 수 있겠군."
    m "천재셔요! 그럼 바로 준비하겠습니다."
    m "[pov]님! 그럼 잠시 후에 제일 첫번째 방으로 안내해 드리겠습니다."
    m "가시죠, 아가씨!"
    p "그래~!"
    show maid idle at left:
        yalign 100
        ease 0.5 xalign -0.8 
    hide maid idle
    show prinses idle at left:
        yalign 100
        ease 0.5 xalign -0.8 
    hide prinses idle
    pov "헉, 빠르다.."
    show yujin idle at center:
        yalign 100
    j "좋아~ 이걸로 이제 윗층에서 시끄럽게 떠드는 것도 해결."
    j "저 사람들이 안내하는 걸 보니 너 정말 참가자가 맞나 보구나?"
    j "뭐 좋아, 그럼 곧 정산할 시간이기도 하니까 따라와."
    j "곧 어두워지기도 하고. 밥도 먹어야 하니까."
    pov "그..그래."
    jump end

    return
