'''
Function:
    经典坦克大战小游戏
'''
import os
import cfg
import pygame
from modules import *

'''主函数'''


def main(cfg):
    # 游戏初始化
    pygame.init()
    # 用于加载声音对象和控制播放
    pygame.mixer.init()
    # 设置屏幕大小
    screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
    # 设置标题
    pygame.display.set_caption(cfg.TITLE)
    # 加载游戏素材
    sounds = {}
    for key, value in cfg.AUDIO_PATHS.items():
        sounds[key] = pygame.mixer.Sound(value)
        # 设置声音音量，0~1，0时静音，1时音量最大
        sounds[key].set_volume(1)
    # 开始界面
    is_dual_mode = gameStartInterface(screen, cfg)
    # 关卡数
    levelfilepaths = [os.path.join(cfg.LEVELFILEDIR, filename) for filename in sorted(os.listdir(cfg.LEVELFILEDIR))]
    # 主循环
    for idx, levelfilepath in enumerate(levelfilepaths):
        # 关卡切换
        switchLevelIterface(screen, cfg, idx + 1)
        game_level = GameLevel(idx + 1, levelfilepath, sounds, is_dual_mode, cfg)
        is_win = game_level.start(screen)
        # 如果游戏结束，退出循环
        if not is_win: break
    is_quit_game = gameEndIterface(screen, cfg, is_win)
    return is_quit_game


'''run'''
if __name__ == '__main__':
    while True:
        is_quit_game = main(cfg)
        if is_quit_game:
            break