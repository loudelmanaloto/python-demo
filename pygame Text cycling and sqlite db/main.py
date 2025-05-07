import pygame, sys
import database


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))

#text display
# font = pygame.font.Font('font/custom.ttf', 32)
arial_font = pygame.font.SysFont('Arial', 32) # arial
tmr = pygame.font.SysFont('Times New Roman', 32) # arial



textList = [
    {
        "name":"Ezekiel",
        "text": "What's your name?",
        "image": 'ezekiel.png',
        "sfx": ""
    },
    {
        "name":"Tony",
        "text": "What?"
    },
    {
        "name":"Ezekiel",
        "text": "What's your name?"
    },
    {
        "name":"Tony",
        "text": "Tony"
    },
    
    {
        "name":"Ezekiel",
        "text": "**** you Tony."
    }
]

# dictionary = {
#     "Scene1": textList,
#     "Scene2": textList2,
#     "Scene3": [],
#     "Scene4": [],
#     "Scene1": [],

# }


textCounter = 0

box_width, box_height = 800, 100
box_rect = pygame.Rect(0, 0, box_width, box_height)
box_rect.bottom = 600


bullet_rect = pygame.Rect(400, 300, 50, 50)


while True:
    screen.fill('white')

    pygame.draw.rect(screen, 'grey', box_rect)

    textToDisplay = f"{textList[textCounter]['name']}: {textList[textCounter]['text']}"

    text = arial_font.render(textToDisplay, True, 'black', 'grey')
    text_rect = text.get_rect(topleft=box_rect.topleft)

    screen.blit(text, text_rect)

    # mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and textCounter < len(textList) - 1:
                print("space")
                textCounter += 1

            if event.key == pygame.K_F2:
                database.insertRecord("Dialogue", 22)
                print("saved progress")
            
            if event.key == pygame.K_F1:
                data = database.retrieveRecord()
                print(data)
            
            # if event.key == pygame.K_f:
            #     print("pressed f")
            #     pygame.draw.rect(screen, 'red', bullet_rect)
            #     x_pos, y_pos = pygame.mouse.get_pos()
            #     # bullet_rect.move_ip(2, 0)

           

        if event.type == pygame.MOUSEBUTTONDOWN and textCounter < len(textList) - 1:
            textCounter += 1
            print("Mouse clicked.")

        

    pygame.display.update()