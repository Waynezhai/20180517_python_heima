#!/usr/bin/env python
#-*- coding:utf8 -*-
#################################################################
# FileName: hm_09_heroFlyForever.py
# Author: Wayne_zhy
# Mail: zhyzhaihuiyan@163.com
# Created Time: 2019-05-26 18:51:58
# Last Modified: 2019-05-26 18:52:02
#################################################################

import pygame

# 游戏的初始化
pygame.init()

# 创建游戏窗口
pygame.display.set_caption("Flying Hero")
screen = pygame.display.set_mode((480, 700))

# 绘制背景
bg = pygame.image.load(r'E:\Desktop\Server Constant\images\background.png')
screen.blit(bg, (0, 0))
# bg = pygame.image.load("./images/background.png")
# windows平台下，不能使用相对路径，且路径中不能出现中文

# 绘制英雄的飞机
hero = pygame.image.load(r'E:\Desktop\Server Constant\images\me1.png')
screen.blit(hero, (150, 300))

# 统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 106)

# 游戏循环---游戏的正式开始
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # tick方法指定代码的执行频率，参数表示1s刷新多少次
    clock.tick(60)

    # 修改飞机的位置
    hero_rect.y -= 1
    hero_rect.x += 1

    # 调用blit方法传图到窗口
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 调用update方法更新显示
    pygame.display.update()
    if hero_rect.y <= -126:
        hero_rect.y = 700
    if hero_rect.x >= 480:
        hero_rect.x = -102

pygame.quit()
