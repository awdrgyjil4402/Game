import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 0, 255)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "LEGEND OF PENGUINS python edition"
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_HEALTH = 780
PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'penguin.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 0)

# Weapon settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 500,
                     'bullet_lifetime': 500,
                     'rate': 1000,
                     'kickback': 200,
                     'spread': 20,
                     'damage': 5,
                     'bullet_size': 'lg',
                     'bullet_count': 50}
WEAPONS['shotgun'] = {'bullet_speed': 400,
                      'bullet_lifetime': 1000000,
                      'rate': 1000,
                      'kickback': 300,
                      'spread': 0,
                      'damage': 50,
                      'bullet_size': 'xl',
                      'bullet_count': 1}

# Mob settings
MOB_IMG = 'ManBlue_hold.png'
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 600
MOB_DAMAGE = 50
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400

# Effects
MUZZLE_FLASHES = ['smoke_01.png', 'smoke_02.png', 'smoke_03.png',
                  'smoke_04.png', 'smoke_05.png', 'smoke_06.png',
                  'smoke_07.png', 'smoke_08.png', 'smoke_09.png',
                  'smoke_10.png']
SPLAT = 'splat green.png'
FLASH_DURATION = 50
DAMAGE_ALPHA = [i for i in range(0, 255, 55)]
NIGHT_COLOR = (20, 20, 20)
LIGHT_RADIUS = (500, 500)
LIGHT_MASK = "light_350_med.png"

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Items
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'hitpro.png'}
HEALTH_PACK_AMOUNT = 62
BOB_RANGE = 10
BOB_SPEED = 0.3

# Sounds
BG_MUSIC = 'Happy Tune.wav'
PLAYER_HIT_SOUNDS = ['penguin_RIP 03.wav', 'penguin_RIP 02.wav']
ZOMBIE_MOAN_SOUNDS = None
ZOMBIE_HIT_SOUNDS = ['pain/8.wav']
WEAPON_SOUNDS = {'pistol': ['pistol.wav'],
                 'shotgun': ['shotgun.wav']}
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav',}