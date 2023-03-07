#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame
import sys

# 初始化 Pygame
pygame.init()

# 游戏尺寸
WIDTH = 600
HEIGHT = 600

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 定义字体
FONT = pygame.font.SysFont('Arial', 100)

# 设置游戏窗口
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# 定义游戏板
board = [' ' for _ in range(9)]

# 定义当前玩家和计数器
current_player = 'X'
counter = 0

# 绘制游戏界面
def draw_board():
    win.fill(WHITE)
    # 绘制横线
    pygame.draw.line(win, BLACK, (0, 200), (600, 200), 10)
    pygame.draw.line(win, BLACK, (0, 400), (600, 400), 10)
    # 绘制竖线
    pygame.draw.line(win, BLACK, (200, 0), (200, 600), 10)
    pygame.draw.line(win, BLACK, (400, 0), (400, 600), 10)
    # 绘制游戏状态
    if game_over():
        if winner() == 'X':
            text = FONT.render('X wins!', True, GREEN)
        elif winner() == 'O':
            text = FONT.render('O wins!', True, BLUE)
        else:
            text = FONT.render('Draw!', True, BLACK)
        win.blit(text, (150, 250))
    # 绘制棋子
    for i in range(9):
        x = i % 3 * 200
        y = i // 3 * 200
        if board[i] == 'X':
            pygame.draw.line(win, GREEN, (x + 50, y + 50), (x + 150, y + 150), 10)
            pygame.draw.line(win, GREEN, (x + 150, y + 50), (x + 50, y + 150), 10)
        elif board[i] == 'O':
            pygame.draw.circle(win, BLUE, (x + 100, y + 100), 50, 10)

# 判断游戏是否结束
def game_over():
    return winner() != None or counter == 9

# 判断胜利者
def winner():
    global board
    # 横向胜利
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != ' ':
            return board[i]
    # 竖向胜利
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return board[i]
 # 斜向胜利
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return board[2]
    return None


# In[ ]:




