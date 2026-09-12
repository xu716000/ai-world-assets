#!/usr/bin/env python3
"""
AI World Assets Generator
自动生成48张游戏美术素材 PNG 资源包
"""

import os
import json
from PIL import Image, ImageDraw
from pathlib import Path
import zipfile
import shutil

# ============================================================================
# 颜色配置
# ============================================================================
COLORS = {
    "blue": {
        "primary": (0, 128, 255),      # #0080FF
        "light": (0, 191, 255),        # #00BFFF
        "outline": (0, 0, 255),        # #0000FF
        "shadow": (0, 26, 77),         # #001A4D
        "highlight": (0, 255, 255),    # #00FFFF
    },
    "red": {
        "primary": (204, 0, 0),        # #CC0000
        "light": (255, 68, 68),        # #FF4444
        "outline": (255, 0, 0),        # #FF0000
        "shadow": (102, 0, 0),         # #660000
        "highlight": (255, 102, 102),  # #FF6666
    },
    "resources": {
        "ore": ((0, 255, 255), (0, 136, 255)),           # 蓝晶
        "metal": ((224, 224, 224), (128, 128, 128)),     # 银灰
        "wood": ((205, 133, 63), (139, 69, 19)),         # 棕色
        "fuel": ((255, 215, 0), (184, 160, 0)),          # 黄金
        "power": ((255, 255, 0), (0, 128, 255)),         # 黄+蓝
        "pop": ((0, 255, 0), (0, 136, 0)),               # 绿色
        "credit": ((255, 183, 0), (153, 119, 0)),        # 金色
        "gear": ((160, 160, 160), (96, 96, 96)),         # 机械灰
    }
}

# ============================================================================
# 资源定义
# ============================================================================
BUILDINGS_BLUE = [
    ("b_hq", "主基地"),
    ("b_powerplant", "发电站"),
    ("b_solar", "太阳能"),
    ("b_drill", "钻井"),
    ("b_lumber", "伐木厂"),
    ("b_derrick", "油井"),
    ("b_smelter", "冶炼厂"),
    ("b_house", "民居"),
    ("b_barracks", "兵营"),
    ("b_factory", "工厂"),
    ("b_turret", "防御塔"),
    ("b_refinery", "精炼厂"),
    ("b_forge", "铸造厂"),
    ("b_dock", "船坞"),
]

BUILDINGS_RED = [(f"{name}_e", desc) for name, desc in BUILDINGS_BLUE]

UNITS_BLUE = [
    ("u_infantry", "步兵"),
    ("u_tank", "坦克"),
    ("u_mech", "机甲"),
    ("u_gunship", "炮艇"),
]

UNITS_RED = [(f"{name}_e", desc) for name, desc in UNITS_BLUE]

TERRAIN = [
    ("t_rock", "岩石"),
    ("t_ore", "矿物"),
    ("t_forest", "森林"),
    ("t_oil", "油田"),
]

ICONS = [
    ("i_ore", "矿石", "ore"),
    ("i_metal", "金属", "metal"),
    ("i_wood", "木材", "wood"),
    ("i_fuel", "燃料", "fuel"),
    ("i_power", "电力", "power"),
    ("i_pop", "人口", "pop"),
    ("i_credit", "信用", "credit"),
    ("i_gear", "科技", "gear"),
]


# ============================================================================
# 基础形状生成
# ============================================================================
def draw_isometric_box(draw, x, y, width, height, color_info, is_enemy=False):
    """绘制等距视角立方体"""
    color_set = color_info["red"] if is_enemy else color_info["blue"]
    
    # 计算等距坐标
    top_left = (x, y)
    top_right = (x + width, y)
    bottom_right = (x + width, y + height)
    bottom_left = (x, y + height)
    
    # 绘制面
    face_points = [top_left, top_right, bottom_right, bottom_left]
    draw.polygon(face_points, fill=color_set["primary"], outline=color_set["outline"], width=2)
    
    # 绘制阴影（左下）
    shadow_points = [
        bottom_left,
        (bottom_left[0] - width // 4, bottom_left[1] + height // 8),
        (bottom_right[0] - width // 4, bottom_right[1] + height // 8),
        bottom_right
    ]
    draw.polygon(shadow_points, fill=color_set["shadow"])


def draw_neon_outline(draw, points, color, width=2):
    """绘制霓虹描边"""
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]
        draw.line([p1, p2], fill=color, width=width)


def create_building(filename, name, color_info, size=128, is_enemy=False):
    """生成建筑图片"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    color_set = color_info["red"] if is_enemy else color_info["blue"]
    center_x, center_y = size // 2, size // 2
    
    # 绘制等距立方体建筑体
    # 前面
    front_points = [
        (center_x - size // 4, center_y - size // 4),
        (center_x + size // 4, center_y - size // 4),
        (center_x + size // 4, center_y + size // 4),
        (center_x - size // 4, center_y + size // 4),
    ]
    draw.polygon(front_points, fill=color_set["primary"], outline=color_set["outline"], width=2)
    
    # 左侧面
    left_points = [
        (center_x - size // 4, center_y - size // 4),
        (center_x - size // 2, center_y),
        (center_x - size // 2, center_y + size // 6),
        (center_x - size // 4, center_y + size // 4),
    ]
    draw.polygon(left_points, fill=color_set["shadow"], outline=color_set["outline"], width=1)
    
    # 右侧面
    right_points = [
        (center_x + size // 4, center_y - size // 4),
        (center_x + size // 2, center_y),
        (center_x + size // 2, center_y + size // 6),
        (center_x + size // 4, center_y + size // 4),
    ]
    draw.polygon(right_points, fill=color_set["light"], outline=color_set["outline"], width=1)
    
    # 屋顶
    roof_points = [
        (center_x - size // 4, center_y - size // 4),
        (center_x, center_y - size // 3),
        (center_x + size // 4, center_y - size // 4),
    ]
    draw.polygon(roof_points, fill=color_set["highlight"], outline=color_set["outline"], width=2)
    
    # 底部阴影
    shadow_y = center_y + size // 4 + 2
    draw.line(
        [(center_x - size // 4, shadow_y), (center_x + size // 4, shadow_y)],
        fill=(0, 0, 0, 100),
        width=3
    )
    
    # 保存
    img.save(filename, 'PNG')
    print(f"✓ Generated: {filename}")


def create_unit(filename, name, color_info, size=64, is_enemy=False):
    """生成单位图片"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    color_set = color_info["red"] if is_enemy else color_info["blue"]
    center_x, center_y = size // 2, size // 2
    radius = size // 3
    
    # 绘制士兵/坦克轮廓
    # 身体
    body_box = [
        (center_x - radius, center_y - radius // 2),
        (center_x + radius, center_y + radius // 2),
    ]
    draw.ellipse(body_box, fill=color_set["primary"], outline=color_set["outline"], width=1)
    
    # 头部
    head_box = [
        (center_x - radius // 2, center_y - radius),
        (center_x + radius // 2, center_y - radius // 2),
    ]
    draw.ellipse(head_box, fill=color_set["light"], outline=color_set["outline"], width=1)
    
    # 武器/炮塔
    draw.line(
        [(center_x + radius // 2, center_y), (center_x + size // 2 - 2, center_y - radius // 2)],
        fill=color_set["outline"],
        width=2
    )
    
    # 底部阴影
    shadow_y = center_y + radius // 2 + 1
    draw.line(
        [(center_x - radius, shadow_y), (center_x + radius, shadow_y)],
        fill=(0, 0, 0, 80),
        width=2
    )
    
    img.save(filename, 'PNG')
    print(f"✓ Generated: {filename}")


def create_terrain(filename, name, color_info, size=64):
    """生成地形图片 (64×80)"""
    img = Image.new('RGBA', (size, size + 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    center_x, center_y = size // 2, size // 2
    
    # 不同地形的颜色
    terrain_colors = {
        "rock": ((128, 128, 128), (80, 80, 80)),
        "ore": ((0, 255, 255), (0, 136, 255)),
        "forest": ((34, 139, 34), (0, 100, 0)),
        "oil": ((255, 69, 0), (178, 34, 0)),
    }
    
    # 确定地形类型
    for key, colors in terrain_colors.items():
        if key in filename.lower():
            primary, shadow = colors
            break
    else:
        primary, shadow = (128, 128, 128), (80, 80, 80)
    
    # 绘制等距地形块
    points = [
        (center_x, center_y - size // 4),
        (center_x + size // 2, center_y),
        (center_x, center_y + size // 4),
        (center_x - size // 2, center_y),
    ]
    draw.polygon(points, fill=primary, outline=(0, 255, 255), width=2)
    
    # 阴影
    shadow_points = [
        (center_x, center_y + size // 4),
        (center_x + size // 2, center_y + size // 3),
        (center_x, center_y + size // 2),
    ]
    draw.polygon(shadow_points, fill=shadow)
    
    img.save(filename, 'PNG')
    print(f"✓ Generated: {filename}")


def create_icon(filename, name, color_info, size=32):
    """生成UI图标"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    center_x, center_y = size // 2, size // 2
    
    # 获取图标颜色
    icon_type = None
    for key in color_info["resources"]:
        if key in filename.lower():
            icon_type = key
            break
    
    if icon_type:
        primary, shadow = color_info["resources"][icon_type]
    else:
        primary, shadow = (100, 100, 100), (60, 60, 60)
    
    # 绘制对称的图标形状
    radius = size // 3
    
    # 主色块
    box = [
        (center_x - radius, center_y - radius),
        (center_x + radius, center_y + radius),
    ]
    draw.ellipse(box, fill=primary, outline=(255, 255, 255), width=1)
    
    # 阴影/高亮
    draw.ellipse(
        [
            (center_x - radius + 2, center_y - radius + 2),
            (center_x + radius - 2, center_y + radius - 2),
        ],
        fill=shadow
    )
    
    img.save(filename, 'PNG')
    print(f"✓ Generated: {filename}")


# ============================================================================
# 主生成流程
# ============================================================================
def generate_all_assets(output_dir="assets"):
    """生成所有资源文件"""
    
    # 创建目录结构
    dirs = [
        f"{output_dir}/buildings",
        f"{output_dir}/buildings_enemy",
        f"{output_dir}/units",
        f"{output_dir}/units_enemy",
        f"{output_dir}/terrain",
        f"{output_dir}/icons",
        f"{output_dir}/effects",
    ]
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"📁 Created: {d}")
    
    print("\n" + "="*60)
    print("🎨 GENERATING BUILDINGS (Blue)")
    print("="*60)
    for name, desc in BUILDINGS_BLUE:
        create_building(f"{output_dir}/buildings/{name}.png", desc, COLORS)
    
    print("\n" + "="*60)
    print("🔴 GENERATING BUILDINGS (Red/Enemy)")
    print("="*60)
    for name, desc in BUILDINGS_RED:
        create_building(f"{output_dir}/buildings_enemy/{name}.png", desc, COLORS, is_enemy=True)
    
    print("\n" + "="*60)
    print("🎯 GENERATING UNITS (Blue)")
    print("="*60)
    for name, desc in UNITS_BLUE:
        create_unit(f"{output_dir}/units/{name}.png", desc, COLORS)
    
    print("\n" + "="*60)
    print("🔴 GENERATING UNITS (Red/Enemy)")
    print("="*60)
    for name, desc in UNITS_RED:
        create_unit(f"{output_dir}/units_enemy/{name}.png", desc, COLORS, is_enemy=True)
    
    print("\n" + "="*60)
    print("🏔️  GENERATING TERRAIN")
    print("="*60)
    for name, desc in TERRAIN:
        create_terrain(f"{output_dir}/terrain/{name}.png", desc, COLORS)
    
    print("\n" + "="*60)
    print("🎨 GENERATING UI ICONS")
    print("="*60)
    for name, desc, icon_type in ICONS:
        create_icon(f"{output_dir}/icons/{name}.png", desc, COLORS)
    
    # 统计
    total_count = len(BUILDINGS_BLUE) + len(BUILDINGS_RED) + len(UNITS_BLUE) + len(UNITS_RED) + len(TERRAIN) + len(ICONS)
    print("\n" + "="*60)
    print(f"✅ COMPLETE! Generated {total_count} assets")
    print("="*60)
    
    return total_count


def pack_assets(source_dir="assets", output_file="AI统治世界_assets_v1.zip"):
    """打包所有资源成ZIP"""
    print(f"\n📦 Packing assets into {output_file}...")
    
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, '.')
                zipf.write(file_path, arcname)
                print(f"  + {arcname}")
    
    file_size = os.path.getsize(output_file) / (1024 * 1024)
    print(f"\n✅ Packed! File size: {file_size:.2f} MB")
    print(f"📍 Location: {os.path.abspath(output_file)}")


def create_manifest(output_dir="assets"):
    """生成资源清单"""
    manifest = {
        "version": "1.0",
        "project": "AI World",
        "generated": "2026-09-12",
        "total_assets": 48,
        "buildings": {
            "blue": len(BUILDINGS_BLUE),
            "red": len(BUILDINGS_RED),
            "total": len(BUILDINGS_BLUE) + len(BUILDINGS_RED),
        },
        "units": {
            "blue": len(UNITS_BLUE),
            "red": len(UNITS_RED),
            "total": len(UNITS_BLUE) + len(UNITS_RED),
        },
        "terrain": len(TERRAIN),
        "icons": len(ICONS),
        "specifications": {
            "buildings": "128×128px PNG RGBA",
            "units": "64×64px PNG RGBA",
            "terrain": "64×80px PNG RGBA",
            "icons": "32×32px PNG RGBA",
            "outline": "2px neon",
            "anchor": "bottom-center",
            "lighting": "45° top-left",
        },
        "buildings_list": [name for name, _ in BUILDINGS_BLUE],
        "units_list": [name for name, _ in UNITS_BLUE],
        "terrain_list": [name for name, _ in TERRAIN],
        "icons_list": [name for name, _ in ICONS],
    }
    
    manifest_file = os.path.join(output_dir, "manifest.json")
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print(f"\n📋 Manifest created: {manifest_file}")


if __name__ == "__main__":
    # 生成所有资源
    generate_all_assets()
    
    # 生成清单
    create_manifest()
    
    # 打包成ZIP
    pack_assets()
    
    print("\n" + "="*60)
    print("🚀 ALL DONE! Ready to deploy to AI World game.")
    print("="*60)
