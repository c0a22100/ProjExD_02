import random
import time
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}


def check_bound(rect: pg.Rect) -> tuple[bool, bool]:
    """
    こうかとんRect，爆弾Rectが画面外 or 画面内かを判定する関数
    引数：こうかとんRect or 爆弾Rect
    戻り値：横方向，縦方向の判定結果タプル（True：画面内／False：画面外）
    """
    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right:  # 横方向判定
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:  # 縦方向判定
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_imgf = pg.transform.flip(kk_img, True, False)  # kk_imgを左右反転させる

    # 追加課題1.1
    outimg = {
        "[0, 0]": pg.transform.rotozoom(kk_img, 0, 2),
        "[0, -5]": pg.transform.rotozoom(kk_imgf, 90, 2),
        "[5, -5]": pg.transform.rotozoom(kk_imgf, 45, 2),
        "[5, 0]": pg.transform.rotozoom(kk_imgf, 0, 2),
        "[5, 5]": pg.transform.rotozoom(kk_imgf, -45, 2),
        "[0, 5]": pg.transform.rotozoom(kk_imgf, -90, 2),
        "[-5, 5]": pg.transform.rotozoom(kk_img, 45, 2),
        "[-5, 0]": pg.transform.rotozoom(kk_img, 0, 2),
        "[-5, -5]": pg.transform.rotozoom(kk_img, -45, 2)
    }

    kk_img = pg.transform.rotozoom(kk_img, 0, 2)
    # こうかとんSurface（kk_img）からこうかとんRect（kk_rct）を抽出する
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bd_img = pg.Surface((20, 20))  # 練習１
    bd_img.set_colorkey((0, 0, 0))  # 黒い部分を透明にする
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    # 爆弾Surface（bd_img）から爆弾Rect（bd_rct）を抽出する
    bd_rct = bd_img.get_rect()
    # 爆弾Rectの中心座標を乱数で指定する
    bd_rct.center = x, y 
    vx, vy = +5, +5  # 練習２

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        if kk_rct.colliderect(bd_rct):  # 練習５

            # 追加課題3途中
            
            
            kk_sad = pg.image.load("ex02/fig/8.png")
            kk_sad = pg.transform.rotozoom(kk_sad, 0, 2)
            screen.blit(kk_sad, kk_rct)
            time.sleep(5)
          

            print("ゲームオーバー")
            return   # ゲーム オーバー 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]  # 合計移動量
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
 
        screen.blit(bg_img, [0, 0])
        
        #追加機能1.2
        outimg_key = str((sum_mv))  # outimg_keyでsum_mvを文字列に変換する
        screen.blit(outimg[outimg_key], kk_rct)
        print(kk_rct)
        # キーがouting_keyである値(rotozoomしたSurface)をScreen.blitの第一引数に入力する

        
        bd_rct.move_ip(vx, vy)  # 練習２
        yoko, tate = check_bound(bd_rct)
        if not yoko:  # 横方向に画面外だったら
            vx *= -1
        if not tate:  # 縦方向に範囲外だったら
            vy *= -1
        screen.blit(bd_img, bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
