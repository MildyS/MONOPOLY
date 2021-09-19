import pygame
import random
import time


WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MONOPOLY')

# BEZ FPS IDU TLACIDLA
FPS = 2000
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (102, 255, 0)
RED = (255, 8, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 51)

pygame.init()
font = pygame.font.Font(None, 24)
font_winner = pygame.font.Font(None, 40)
font_info = pygame.font.Font(None, 25)
kolko_hodil = 0

class Player:
    bought_houses_players = []


    def __init__(self, name, color, position, finance):
        # maybe add name later
        self.name = name
        self.color = color
        self.position = position
        self.finance = finance
        self.bought_houses = []

    def change_in_balance(self, finance):
        if type(finance) == int:
            self.finance -= finance

    def buy_new_house(self, house_to_buy):
        if house_to_buy in Player.bought_houses_players:
            pass
        elif house_to_buy == 0 or house_to_buy == 4 or house_to_buy == 8 or house_to_buy == 12 or house_to_buy == 16 or house_to_buy == 20 or house_to_buy == 22:
            pass
        else:
            return True
        return False



class Policko:
    houses = []

    def __init__(self, position, name, price, hire, upgrade, is_p1, is_p2, color):
        self.name = name
        self.price = price
        self.position = position
        self.hire = hire
        self.upgrade = upgrade
        self.is_p1 = is_p1
        self.is_p2 = is_p2
        self.color = color
        self.houses.append(self)

    #pridat hire/nájom
    def create_policko(self, x, y, color, name, price, hire, is_p1, is_p2):
        pygame.draw.rect(WIN, color, (x, y, 100, 100), 2)
        name_help = font.render(name, True, color)
        WIN.blit(name_help, (x + 20, y + 45))
        if name == "Start" or name == "CHANCE" or name == "BOOST":
            price_help = font.render(str(price), True, color)
            WIN.blit(price_help, (x + 30, y + 65))
            hire_help = font.render(str(hire), True, color)
            WIN.blit(hire_help, (x + 20, y + 85))
        else:
            price_help = font.render(f"{str(price)} €", True, color)
            WIN.blit(price_help, (x + 30, y + 65))
            hire_help = font.render(f"{str(hire)} €", True, color)
            WIN.blit(hire_help, (x + 20, y + 85))
        if is_p1:
            draw_player1 = font.render('p1', True, BLUE)
            WIN.blit(draw_player1, (x + 10, y + 10))
        if is_p2:
            draw_player2 = font.render('p2', True, RED)
            WIN.blit(draw_player2, (x + 75, y + 10))

    def is_player_here(self, p1, p2):
        if p1.position == self.position:
            self.is_p1 = True
        else:
            self.is_p1 = False

        if p2.position == self.position:
            self.is_p2 = True
        else:
            self.is_p2 = False



    def set_color_of_house(self, p1, p2):
        if self.position in p1.bought_houses:
            self.color = BLUE
        elif self.position in p2.bought_houses:
            self.color = RED
        else:
            self.color = BLACK

    def show_big_house_middle(self, color, name, price, hire):
        pygame.draw.rect(WIN, color, (450, 200, 200, 300), 2)
        name_help = font.render(name, True, color)
        WIN.blit(name_help, (450 + 80, 250 + 45))
        if name == "Start" or name == "CHANCE" or name == "BOOST" or name == "BOOST":
            pass
        else:
            price_help = font.render(f"Cena: {str(price)} €", True, color)
            WIN.blit(price_help, (420 + 80, 250 + 65))
            hire_help = font.render(f"Nájom: {str(hire)} €", True, color)
            WIN.blit(hire_help, (420 + 80, 250 + 85))

        pygame.display.update()


def draw_window(p1, p2, kocka1, pole1, pole2, pole3, pole4, pole5, pole6, pole7, pole8, pole9, pole10, pole11, pole12, pole13, pole14, pole15, pole16, pole17, pole18, pole19, pole20, pole21, pole22, pole23, pole24, changing_turns):

    WIN.fill(WHITE)

    # crash handle for first round
    if kocka1 == None:
        kolko_hodil = 0
    else:
        kolko_hodil = kocka1

    #top-middle how much player rolled
    kolko_hodil_help = font.render(str(kolko_hodil), True, BLACK)
    WIN.blit(kolko_hodil_help, (550, 50))

    #BUTTONS

    #BUTTON HOD
    pygame.draw.rect(WIN, YELLOW, pygame.Rect(500, 620, 100, 60))
    hod_tag = font.render("HOD", True, BLACK)
    WIN.blit(hod_tag, (532, 640))

    #BUTTON NÁKUP
    pygame.draw.rect(WIN, GREEN, pygame.Rect(100, 620, 100, 60))
    hod_tag = font.render("NÁKUP", True, BLACK)
    WIN.blit(hod_tag, (120, 640))

    #BUTTON VYLEPŠI
    pygame.draw.rect(WIN, GREEN, pygame.Rect(240, 620, 100, 60))
    hod_tag = font.render("VYLEPŠI", True, BLACK)
    WIN.blit(hod_tag, (255, 640))




    # DISPLAY PLAYERS POSITIONS
    p1_help = font.render("Player 1", True, BLUE)
    WIN.blit(p1_help, (10, 10))
    p2_help = font.render("Player 2", True, RED)
    WIN.blit(p2_help, (1020, 10))


    # DISPLAY PLAYERS FINANCE
    p1_finance_help_blit = font.render(str(p1.finance) + " €", True, BLACK)
    WIN.blit(p1_finance_help_blit, (10, 30))
    p2_finance_help_blit = font.render(str(p2.finance) + " €", True, BLACK)
    WIN.blit(p2_finance_help_blit, (1020, 30))

    # DISPLAY INFO ABOUT GAME
    info1_help = font_info.render("Boost => Hádžeš ešte raz", True, BLACK)
    WIN.blit(info1_help, (230, 300))
    info2_help = font_info.render("Chance => +(1000-5000) €", True, BLACK)
    WIN.blit(info2_help, (230, 330))



    # TOP-SIDE

    pole1.is_player_here(p1, p2)
    pole1.set_color_of_house(p1, p2)
    pole1.create_policko(100, 100, pole1.color, "Start", "", pole1.price, pole1.is_p1, pole1.is_p2)

    pole2.is_player_here(p1, p2)
    pole2.set_color_of_house(p1, p2)
    pole2.create_policko(200, 100, pole2.color, "Kyjev", 1000, pole2.price * 0.5 * pole2.upgrade, pole2.is_p1, pole2.is_p2)

    pole3.is_player_here(p1, p2)
    pole3.set_color_of_house(p1, p2)
    pole3.create_policko(300, 100, pole3.color, "Minsk", 2000, pole3.price * 0.5 * pole3.upgrade, pole3.is_p1, pole3.is_p2)

    pole4.is_player_here(p1, p2)
    pole4.set_color_of_house(p1, p2)
    pole4.create_policko(400, 100, pole4.color, "Riga", 3000, pole4.price * 0.5 * pole4.upgrade, pole4.is_p1, pole4.is_p2)

    pole5.is_player_here(p1, p2)
    pole5.set_color_of_house(p1, p2)
    pole5.create_policko(500, 100, pole5.color, "CHANCE", "", pole5.price, pole5.is_p1, pole5.is_p2)

    pole6.is_player_here(p1, p2)
    pole6.set_color_of_house(p1, p2)
    pole6.create_policko(600, 100, pole6.color, "Oslo", 5000, pole6.price * 0.5 * pole6.upgrade, pole6.is_p1, pole6.is_p2)

    pole7.is_player_here(p1, p2)
    pole7.set_color_of_house(p1, p2)
    pole7.create_policko(700, 100, pole7.color, "Kodaň", 7000, pole7.price * 0.5 * pole7.upgrade, pole7.is_p1, pole7.is_p2)

    pole8.is_player_here(p1, p2)
    pole8.set_color_of_house(p1, p2)
    pole8.create_policko(800, 100, pole8.color, "Dublin", 9000, pole8.price * 0.5 * pole8.upgrade, pole8.is_p1, pole8.is_p2)

    pole9.is_player_here(p1, p2)
    pole9.set_color_of_house(p1, p2)
    pole9.create_policko(900, 100, pole9.color, "BOOST", "", pole9.price, pole9.is_p1, pole9.is_p2)

    # RIGHT-SIDE

    pole10.is_player_here(p1, p2)
    pole10.set_color_of_house(p1, p2)
    pole10.create_policko(900, 200, pole10.color, "Haiti", 11000, pole10.price * 0.5 * pole10.upgrade, pole10.is_p1, pole10.is_p2)

    pole11.is_player_here(p1, p2)
    pole11.set_color_of_house(p1, p2)
    pole11.create_policko(900, 300, pole11.color, "Havana", 12000, pole11.price * 0.5 * pole11.upgrade, pole11.is_p1, pole11.is_p2)

    pole12.is_player_here(p1, p2)
    pole12.set_color_of_house(p1, p2)
    pole12.create_policko(900, 400, pole12.color, "Belize", 13000, pole12.price * 0.5 * pole12.upgrade, pole12.is_p1, pole12.is_p2)

    # BOTTOM-SIDE !!! POZOR IDE Z PRAVA !!!

    pole13.is_player_here(p1, p2)
    pole13.set_color_of_house(p1, p2)
    pole13.create_policko(100, 500, pole13.color, "BOOST", "", pole13.price, pole13.is_p1, pole13.is_p2)

    pole14.is_player_here(p1, p2)
    pole14.set_color_of_house(p1, p2)
    pole14.create_policko(200, 500, pole14.color, "Paríž", 26000, pole14.price * 0.5 * pole14.upgrade, pole14.is_p1, pole14.is_p2)

    pole15.is_player_here(p1, p2)
    pole15.set_color_of_house(p1, p2)
    pole15.create_policko(300, 500, pole15.color, "Berlín", 24000, pole15.price * 0.5 * pole15.upgrade, pole15.is_p1, pole15.is_p2)

    pole16.is_player_here(p1, p2)
    pole16.set_color_of_house(p1, p2)
    pole16.create_policko(400, 500, pole16.color, "Londýn", 22000, pole16.price * 0.5 * pole16.upgrade, pole16.is_p1, pole16.is_p2)

    pole17.is_player_here(p1, p2)
    pole17.set_color_of_house(p1, p2)
    pole17.create_policko(500, 500, pole17.color, "CHANCE", "", pole17.price, pole17.is_p1, pole17.is_p2)

    pole18.is_player_here(p1, p2)
    pole18.set_color_of_house(p1, p2)
    pole18.create_policko(600, 500, pole18.color, "Ottawa", 20000, pole18.price * 0.5 * pole18.upgrade, pole18.is_p1, pole18.is_p2)

    pole19.is_player_here(p1, p2)
    pole19.set_color_of_house(p1, p2)
    pole19.create_policko(700, 500, pole19.color, "Dallas", 18000, pole19.price * 0.5 * pole19.upgrade, pole19.is_p1, pole19.is_p2)

    pole20.is_player_here(p1, p2)
    pole20.set_color_of_house(p1, p2)
    pole20.create_policko(800, 500, pole20.color, "L.A.", 17000, pole20.price * 0.5 * pole20.upgrade, pole20.is_p1, pole20.is_p2)

    pole21.is_player_here(p1, p2)
    pole21.set_color_of_house(p1, p2)
    pole21.create_policko(900, 500, pole21.color, "CHANCE", "", pole21.price, pole21.is_p1, pole21.is_p2)

    # LEFT-SIDE !!! POZOR IDE Z HORA !!!

    pole22.is_player_here(p1, p2)
    pole22.set_color_of_house(p1, p2)
    pole22.create_policko(100, 200, pole22.color, "Sydney", 40000, pole22.price * 0.5 * pole22.upgrade, pole22.is_p1, pole22.is_p2)

    pole23.is_player_here(p1, p2)
    pole23.set_color_of_house(p1, p2)
    pole23.create_policko(100, 300, pole23.color, "CHANCE", "", pole23.price, pole23.is_p1, pole23.is_p2)

    pole24.is_player_here(p1, p2)
    pole24.set_color_of_house(p1, p2)
    pole24.create_policko(100, 400, pole24.color, "Moskva", 30000, pole24.price * 0.5 * pole24.upgrade, pole24.is_p1, pole24.is_p2)

    if changing_turns == False:
        for x in Policko.houses:
            if p1.position == x.position:
                x.show_big_house_middle(x.color, x.name, x.price, x.hire)
    else:
        for x in Policko.houses:
            if p2.position == x.position:
                x.show_big_house_middle(x.color, x.name, x.price, x.hire)

    pygame.display.update()


def player_movement(p_position):
    kocka1 = random.randint(1, 6)
    #kocka2 = random.randint(1, 6)
    #sucet_kociek = kocka1 + kocka2
    # až ked bude vačšie pole
    new_round = False
    if p_position + kocka1 <= 23:
        p_position += kocka1
    else:
        p_position += kocka1 - 24
        new_round = True
    return p_position, kocka1, new_round


def check_buttons(pos):

    button_hod_clicked = False
    if pos[0] > 500 and pos[0] < 600 and pos[1] > 620 and pos[1] < 680:
        button_hod_clicked = True

    button_buy_clicked = False
    if pos[0] > 100 and pos[0] < 200 and pos[1] > 620 and pos[1] < 680:
        button_buy_clicked = True

    button_upgrade_clicked = False
    if pos[0] > 240 and pos[0] < 340 and pos[1] > 620 and pos[1] < 680:
        button_upgrade_clicked = True

    return button_hod_clicked, button_buy_clicked, button_upgrade_clicked

def test_if_house_is_bought(player):
    for x in Policko.houses:
        if x.position == player.position:
            return x.position, x.price
        else:
            pass
    return -1, -1

def chance_function(player):
    rand_finance = random.randrange(1000, 5000, 1000)
    player.finance += rand_finance

def player_win(player):
    winner = font_winner.render(f"{player.name} vyhral !!!", True, player.color)
    WIN.blit(winner, (500, 20))
    pygame.display.update()

def main():
    p1 = Player("p1", BLUE, 0, 40000)
    p2 = Player("p2", RED, 0, 40000)


    pole1 = Policko(0, "Start", "", 1, False, True, True, BLACK)
    pole2 = Policko(1, "Kyjev", 1000, 1000, 1, True, True, BLACK)
    pole2.hire = pole2.price * 0.5 * pole2.upgrade
    pole3 = Policko(2, "Minsk", 2000, 2000, 1, True, True, BLACK)
    pole3.hire = pole3.price * 0.5 * pole3.upgrade
    pole4 = Policko(3, "Riga", 3000, 3000, 1, True, True, BLACK)
    pole4.hire = pole4.price * 0.5 * pole4.upgrade
    pole5 = Policko(4, "CHANCE", "", 0, 1, True, True, BLACK)
    pole6 = Policko(5, "Oslo", 5000, 5000, 1, True, True, BLACK)
    pole6.hire = pole6.price * 0.5 * pole6.upgrade
    pole7 = Policko(6, "Kodaň", 7000, 7000, 1, True, True, BLACK)
    pole7.hire = pole7.price * 0.5 * pole7.upgrade
    pole8 = Policko(7, "Dublin", 9000, 9000, 1, True, True, BLACK)
    pole8.hire = pole8.price * 0.5 * pole8.upgrade
    pole9 = Policko(8, "BOOST", "", 0, 1, True, True, BLACK)
    pole10 = Policko(9, "Haiti", 11000, 11000, 1, True, True, BLACK)
    pole10.hire = pole10.price * 0.5 * pole10.upgrade
    pole11 = Policko(10, "Havana", 12000, 12000, 1, True, True, BLACK)
    pole11.hire = pole11.price * 0.5 * pole11.upgrade
    pole12 = Policko(11, "Belize", 13000, 13000, 1, True, True, BLACK)
    pole12.hire = pole12.price * 0.5 * pole12.upgrade
    pole13 = Policko(20, "BOOST", "", 0, 1, True, True, BLACK)
    pole14 = Policko(19, "Paríž", 26000, 26000, 1, True, True, BLACK)
    pole14.hire = pole12.price * 0.5 * pole12.upgrade
    pole15 = Policko(18, "Berlín", 24000, 24000, 1, True, True, BLACK)
    pole15.hire = pole12.price * 0.5 * pole12.upgrade
    pole16 = Policko(17, "Londýn", 22000, 22000, 1, True, True, BLACK)
    pole16.hire = pole12.price * 0.5 * pole12.upgrade
    pole17 = Policko(16, "CHANCE", "", 0, 1, True, True, BLACK)
    pole18 = Policko(15, "Ottawa", 20000, 20000, 1, True, True, BLACK)
    pole18.hire = pole18.price * 0.5 * pole18.upgrade
    pole19 = Policko(14, "Dallas", 18000, 18000, 1, True, True, BLACK)
    pole19.hire = pole19.price * 0.5 * pole19.upgrade
    pole20 = Policko(13, "L.A.", 17000, 17000, 1, True, True, BLACK)
    pole20.hire = pole20.price * 0.5 * pole20.upgrade
    pole21 = Policko(12, "CHANCE", "", 0, 1, True, True, BLACK)
    pole22 = Policko(23, "Sydney", 40000, 40000, 1, True, True, BLACK)
    pole22.hire = pole22.price * 0.5 * pole22.upgrade
    pole23 = Policko(22, "CHANCE", "", 0, 1, True, True, BLACK)
    pole24 = Policko(21, "Moskva", 30000, 30000, 1, True, True, BLACK)
    pole24.hire = pole24.price * 0.5 * pole24.upgrade

    run = True
    clock = pygame.time.Clock()

    kolko_hodil = 0

    changing_turns = True
    upgraded_this_round = False

    while run:

        clock.tick(FPS)

        # DISPLAY THINGS ON SURFACE
        draw_window(p1, p2, kolko_hodil, pole1, pole2, pole3, pole4, pole5, pole6, pole7, pole8, pole9, pole10, pole11, pole12, pole13, pole14, pole15, pole16, pole17, pole18, pole19, pole20, pole21, pole22, pole23, pole24, changing_turns)

        if p1.finance < 0:
            print("p1 prehral")
            player_win(p2)
            time.sleep(10)
            run = False
        if p2.finance < 0:
            print("p2 prehral")
            player_win(p1)
            time.sleep(10)
            run = False


        button_hod_clicked = False
        button_buy_clicked = False
        button_upgrade_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                button_hod_clicked, button_buy_clicked, button_upgrade_clicked = check_buttons(pos)

        # BUTTON HOD

        if button_hod_clicked:
            if changing_turns == True:
                p1.position, kolko_hodil, new_round = player_movement(p1.position)

                # is in BOOST
                if p1.position == 8 or p1.position == 20:
                    pass

                if p1.position in p2.bought_houses:
                    for x in Policko.houses:
                        if p1.position == x.position:
                            p1.finance -= x.hire
                            p2.finance += x.hire
                if new_round:
                    p1.finance += 10000

                upgraded_this_round = False
                changing_turns = False

                for x in Policko.houses:
                    if p1.position == x.position and x.name == "CHANCE":
                        chance_function(p1)
                    if p1.position == x.position and x.name == "BOOST":
                        changing_turns = True

            else:
                p2.position, kolko_hodil, new_round = player_movement(p2.position)

                if p2.position in p1.bought_houses:
                    for x in Policko.houses:
                        if p2.position == x.position:
                            p2.finance -= x.hire
                            p1.finance += x.hire
                if new_round:
                    p2.finance += 10000

                upgraded_this_round = False
                changing_turns = True

                for x in Policko.houses:
                    if p2.position == x.position and x.name == "CHANCE":
                        chance_function(p2)
                    if p2.position == x.position and x.name == "BOOST":
                        changing_turns = False

            # makeing pause after hod
            time.sleep(0)

        # BUTTON BUY

        if button_buy_clicked and changing_turns == False:
            purchase_is_valid = p1.buy_new_house(p1.position)
            testing, testing_price = test_if_house_is_bought(p1)
            if type(testing_price) == int:
                if p1.finance - testing_price > 0:
                    finance_good = True
                else:
                    finance_good = False

                # check if the property is already bought/ is valid
                if purchase_is_valid and finance_good and testing not in p2.bought_houses:
                    p1.bought_houses.append(testing)
                    Player.bought_houses_players.append(testing)
                    # changing finance balance of player
                    p1.change_in_balance(testing_price)

                print("player_1 " + str(p1.bought_houses))


        if button_buy_clicked and changing_turns == True:
            purchase_is_valid = p2.buy_new_house(p2.position)
            testing, testing_price = test_if_house_is_bought(p2)
            if type(testing_price) == int:
                if p2.finance - testing_price > 0:
                    finance_good = True
                else:
                    finance_good = False

                # check if the property is already bought/ is valid
                if purchase_is_valid and finance_good and testing not in p1.bought_houses:
                    p2.bought_houses.append(testing)
                    Player.bought_houses_players.append(testing)
                    # changing finance balance of player
                    p2.change_in_balance(testing_price)

                print("player_2 " + str(p2.bought_houses))

        if button_upgrade_clicked and changing_turns == False and upgraded_this_round == False:
            if p1.position in  p1.bought_houses:
                for x in Policko.houses:
                    if p1.position == x.position:
                        if p1.finance - x.hire >= 0:
                            p1.finance -= x.hire
                            x.upgrade *= 2
                            x.hire = x.price * 0.5 * x.upgrade
                            upgraded_this_round = True

        if button_upgrade_clicked and changing_turns == True and upgraded_this_round == False:
            if p2.position in  p2.bought_houses:
                for x in Policko.houses:
                    if p2.position == x.position:
                        if p2.finance - x.hire >= 0:
                            p2.finance -= x.hire
                            x.upgrade *= 2
                            x.hire = x.price * 0.5 * x.upgrade
                            upgraded_this_round = True


    pygame.quit()



if __name__ == '__main__':
    main()

