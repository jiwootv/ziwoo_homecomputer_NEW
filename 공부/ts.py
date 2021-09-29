def main(DISPLAYSURF, data, x):
    import pygame, sys, st
    pygame.init()
    pygame.mixer.init()
    bg = pygame.image.load("database/img/bg/3.png")
    char = data[0]
    team = data[1]
    button = x[0]
    glitter = x[1]
    back_button = x[2]
    cglitter = x[3]
    buttonGlitter = x[4]
    buttonClicked = x[5]
    FPS = x[6]
    fpsClock = x[7]
    fontObj = x[8]
    fontObj2 = pygame.font.Font("database/ko.ttf", 30)
    mouse_point = x[9]
    fg = x[10]
    sel = 0
    si_dark = pygame.image.load("database/img/char/si_dark.png")
    si_glitter = [pygame.image.load("database/img/char/si_glitter1.png"),
                  pygame.image.load("database/img/char/si_glitter2.png")]
    imgchar = []
    imgcharno = []
    typeName = ["흰", "빨강", "공중", "검정", "메탈", "천사", "에일리언", "스타 에일리언", "좀비", "고대"]
    effectName = ["없음", "멈추게 함", "느리게 함", "고1대의 저주를 검", "약화 시킴"]
    pick = [False, 0, 0]
    for i in range(len(char)):
        if char[i] == 1:
            imgcharno.append(len(imgchar))
            imgchar.append([pygame.image.load(f"database/img/char/{i}/si.png"), i])
        else:
            imgcharno.append(None)
    mouse = [0, 0]
    mouseClicked = False
    m = 0
    loop = True
    key = False
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEMOTION:
                mouse = event.pos
            if event.type == pygame.KEYDOWN:
                if str(event.key) in f"{pygame.K_LSHIFT}/{pygame.K_RSHIFT}":
                    key = True
            elif event.type == pygame.KEYUP:
                if str(event.key) in f"{pygame.K_LSHIFT}/{pygame.K_RSHIFT}":
                    key = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouseClicked = False
        if mouseClicked and not pick[0]:
            if mouse[0] < 135:
                if sel > 0:
                    sel -= 0.25
            if mouse[0] > 945:
                if sel < len(imgchar)-1:
                    sel += 0.25
        DISPLAYSURF.blit(bg, (0, 0))
        for i in range(len(imgchar)):
            if -165 <= 490+131*(i-int(sel)) <= 1080:
                DISPLAYSURF.blit(imgchar[i][0], (490+131*(i-int(sel)), 275))
                var2 = False
                if ", "+str(imgchar[i][1])+", " in ", "+str(team)[1:len(str(team))-1]+", ":
                    DISPLAYSURF.blit(si_dark, (490+131*(i-int(sel)), 275))
                    var2 = True
                if 490+131*(i-int(sel)) < mouse[0] < 591+131*(i-int(sel)) and 275 < mouse[1] < 355 and not pick[0]:
                    if not var2:
                        if m == 0:
                            m = 1
                        else:
                            m = 0
                        DISPLAYSURF.blit(si_glitter[m], (490+131*(i-int(sel)), 275))
                    if mouseClicked:
                        if key:
                            if var2:
                                for ii in range(10):
                                    if team[ii] == imgchar[i][1]:
                                        team[ii] = "-"
                            else:
                                var = False
                                for ii in range(10):
                                    if team[ii] == "-" and not var:
                                        team[ii] = imgchar[i][1]
                                        var = True
                            mouseClicked = False
                        elif not var2:
                            var = st.char(imgchar[i][1], False)
                            pick = [True, imgchar[i][1], charStatShow(var, fontObj, fontObj2, typeName, effectName)]
        for ii in range(2):
            for i in range(5):
                if team[5*ii+i] != "-":
                    DISPLAYSURF.blit(imgchar[imgcharno[team[5*ii+i]]][0], (250+126*i, 56+83*ii))
                    if 250+126*i < mouse[0] < 343+126*i and 56+83*ii < mouse[1] < 129+83*ii:
                        if m == 0:
                            m = 1
                        else:
                            m = 0
                        DISPLAYSURF.blit(si_glitter[m], (250+126*i, 56+83*ii))
                        if mouseClicked and not pick[0]:
                            if not key:
                                var = st.char(team[5*ii+i], False)
                                pick = [True, team[5*ii+i], charStatShow(var, fontObj, fontObj2, typeName, effectName)]
                            else:
                                mouseClicked = False
                            team[5*ii+i] = "-"
        if pick[0]:
            DISPLAYSURF.blit(imgchar[imgcharno[pick[1]]][0], (mouse[0]-50, mouse[1]-40))
            for i in range(5):
                DISPLAYSURF.blit(pick[2][i], (mouse[0], mouse[1]+40*(i+1)))
            for j in range(len(pick[2])-5):
                DISPLAYSURF.blit(pick[2][i+j+1], (mouse[0], mouse[1]+30*j+40*(i+2)))
            if not mouseClicked:
                for ii in range(2):
                    for i in range(5):
                        if 250+126*i < mouse[0] < 343+126*i and 56+83*ii < mouse[1] < 129+83*ii:
                            team[5*ii+i] = pick[1]
                pick[0] = False
        else:
            for i in range(1, 10):
                if team[i] != "-" and team[i-1] == "-":
                    team[i-1] = team[i]
                    team[i] = "-"
        DISPLAYSURF.blit(fg, (0, 0))
        DISPLAYSURF.blit(back_button, (0, 430))
        if (mouse[0]-37)**2+(mouse[1]-467)**2 <= 1369:
            buttonGlitter.play(0)
            if m == 0:
                m = 1
            else:
                m = 0
            DISPLAYSURF.blit(cglitter[m], (0, 430))
            if mouseClicked:
                buttonClicked.play(0)
                loop = False
        if mouseClicked:
            DISPLAYSURF.blit(mouse_point[1], mouse)
        else:
            DISPLAYSURF.blit(mouse_point[0], mouse)
        pygame.display.update()
        fpsClock.tick(FPS)
    return [char, team, data[2], data[3]]

def charStatShow(var, fontObj, fontObj2, typeName, effectName):
    pick = [0, 0, [fontObj.render(f"체력: {var[0]}", True, (0,255,0), (0,0,0)), fontObj.render(f"공격력: {var[1][0]}", True, (255,0,0), (0,0,0)), fontObj.render(f"이동속도: {var[2]}", True, (255,0,255), (0,0,0)), fontObj.render(f"공격범위: {var[3][0]}", True, (0,255,255), (0,0,0)), fontObj.render(f"비용: {var[6]}", True, (255,255,0), (0,0,0))]]
    varType = "속성: "
    for j in range(len(var[14])):
        varType += f"{typeName[int(var[14][j])]}, "
    pick[2].append(fontObj2.render(varType[0:len(varType)-2], True, (126,126,126), (0,0,0)))
    if var[16] != 0:
        pick[2].append(fontObj2.render(f"{var[16]}체력의 베리어 소유", True, (255,142,0), (0,0,0)))
    if len(var[1]) != 1:
        for j in range(len(var[1])-1):
            pick[2].append(fontObj2.render(f"적을 {var[1][j+1][1]}%확률로 {var[1][j+1][2]}f동안 {effectName[var[1][j+1][0]]}", True, (202, 189, 255), (0, 0, 0)))
    if var[17] != None:
        pick[2].append(fontObj2.render(f"{var[17][1]}%확률로 적을 {var[17][0]}거리만큼 이동", True, (63, 44, 142), (0,0,0)))
    if var[13] != None:
        if var[13][0] != 0:
            pick[2].append(fontObj2.render(f"{var[13][0]}번 땅 속으로 숨음", True, (202, 189, 255), (0, 0, 0)))
        pick[2].append(fontObj2.render(f"죽을 시 약화 상태가 아닌 경우 {var[13][5]}f후 {var[13][4]}의 체력으로 {var[13][3]}번 부활", True, (202, 189, 255), (0, 0, 0)))
    if var[18][0] != "-":
        varType = ""
        for j in range(len(var[18][0])):
            varType += f"{typeName[int(var[18][0][j])]}, "
        pick[2].append(fontObj2.render(f"{varType[0:len(varType)-2]}의 속성에 초 데미지", True, (255,0,0), (0,0,0)))
    if var[18][1] != "-":
        varType = ""
        for j in range(len(var[18][1])):
            varType += f"{typeName[int(var[18][1][j])]}, "
        pick[2].append(fontObj2.render(f"{varType[0:len(varType)-2]}의 속성에 맷집이 강함", True, (0,0,255), (0,0,0)))
    if var[18][2] != None:
        pick[2].append(fontObj2.render(f"{var[18][2][1]}%확률로 {var[18][2][0]}레벨의 파동을 소환", True, (202, 189, 255), (0, 0, 0)))
    if var[18][3] != None:
        pick[2].append(fontObj2.render(f"{var[18][3][1]}%확률로 {var[18][3][0]}레벨의 열파를 소환", True, (202, 189, 255), (0, 0, 0)))
    if var[18][4] != 0:
        pick[2].append(fontObj2.render(f"{var[18][4]}%확률로 적을 밀침", True, (202,189,255), (0,0,0)))
    if var[18][5] != 0:
        pick[2].append(fontObj2.render(f"{var[18][5]}%확률로 크리티컬 공격을 함", True, (202,189,255), (0,0,0)))
    if var[18][6][1] != 0:
        pick[2].append(fontObj2.render(f"죽을 시 {var[18][6][0]}%확률로 {var[18][6][1]}번 생존", True, (202,189,255), (0,0,0)))
    if var[18][7][0] != 0:
        pick[2].append(fontObj2.render(f"체력이 {var[18][7][1]}%이하로 떨어질 때, 공격력이 {var[18][7][0]}배로 강해짐", True, (202,189,255), (0,0,0)))
    return pick[2]
