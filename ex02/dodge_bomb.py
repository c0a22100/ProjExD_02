import random
import sys
import pygame as pg



WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400

    clock = pg.time.Clock()

    bd = pg.Surface((20, 20))  # 練習1
    pg.draw.circle(bd, (255, 0, 0), (10, 10), 10)
    bd.set_colorkey((0, 0, 0))
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    bd_rct = bd.get_rect()
    bd_rct.center = x, y
    vx, vy = +5, +5

    key_lst = dict()
    key_lst = {pg.K_UP:(0, -5), pg.K_DOWN:(0, +5), 
               pg.K_LEFT:(-5, 0), pg.K_RIGHT:(+5, 0)}

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])

        key_lst = pg.key.get_pressed()
        sum = [0, 0]
        if key_lst[pg.K_LEFT]:
            sum[0] -= 5
        if key_lst[pg.K_RIGHT]:
            sum[0] += 5
        if key_lst[pg.K_UP]:
            sum[1] -= 5
        if key_lst[pg.K_DOWN]:
            sum[1] += 5
        kk_rct.move_ip(sum)

        screen.blit(kk_img, kk_rct)
        
        bd_rct.move_ip(vx, vy)
        screen.blit(bd, bd_rct)

        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()