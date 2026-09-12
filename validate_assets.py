#!/usr/bin/env python3
"""
AI World Assets Validator
资源文件验证脚本 - 检查所有生成的资源是否符合规范
"""

import os
from PIL import Image
from pathlib import Path
import json

# ============================================================================
# 验证规范
# ============================================================================
ASSET_SPECS = {
    "buildings": {
        "size": (128, 128),
        "path": "assets/buildings",
        "count": 14,
    },
    "buildings_enemy": {
        "size": (128, 128),
        "path": "assets/buildings_enemy",
        "count": 14,
    },
    "units": {
        "size": (64, 64),
        "path": "assets/units",
        "count": 4,
    },
    "units_enemy": {
        "size": (64, 64),
        "path": "assets/units_enemy",
        "count": 4,
    },
    "terrain": {
        "size": (64, 80),
        "path": "assets/terrain",
        "count": 4,
    },
    "icons": {
        "size": (32, 32),
        "path": "assets/icons",
        "count": 8,
    },
}

# ============================================================================
# 验证函数
# ============================================================================
def validate_file_format(filepath):
    """检查文件格式是否为 PNG RGBA"""
    try:
        img = Image.open(filepath)
        if img.format != 'PNG':
            return False, f"格式错误: {img.format} (应为 PNG)"
        if img.mode not in ['RGBA', 'LA', 'PA']:
            return False, f"颜色模式错误: {img.mode} (应为 RGBA)"
        return True, "✓ PNG RGBA 格式正确"
    except Exception as e:
        return False, f"打开文件失败: {str(e)}"


def validate_dimensions(filepath, expected_size):
    """检查尺寸是否符合规范"""
    try:
        img = Image.open(filepath)
        if img.size != expected_size:
            return False, f"尺寸错误: {img.size} (应为 {expected_size})"
        return True, f"✓ 尺寸正确 {expected_size}"
    except Exception as e:
        return False, f"检查失败: {str(e)}"


def validate_transparency(filepath):
    """检查是否有透明通道"""
    try:
        img = Image.open(filepath)
        if img.mode != 'RGBA':
            return False, "缺少透明通道（需要 RGBA）"
        
        # 检查是否至少有一些透明像素
        if img.mode == 'RGBA':
            alpha = img.split()[-1]
            min_alpha = alpha.getextrema()[0]
            if min_alpha == 255:  # 完全不透明
                return False, "图像完全不透明（应有透明背景）"
        
        return True, "✓ 透明通道正确"
    except Exception as e:
        return False, f"检查失败: {str(e)}"


def validate_file_size(filepath):
    """检查文件大小（警告超大文件）"""
    try:
        size_kb = os.path.getsize(filepath) / 1024
        if size_kb > 500:
            return False, f"文件过大: {size_kb:.1f}KB (建议 < 500KB)"
        elif size_kb > 200:
            return "warning", f"⚠ 文件较大: {size_kb:.1f}KB (可考虑压缩)"
        return True, f"✓ 文件大小良好: {size_kb:.1f}KB"
    except Exception as e:
        return False, f"检查失败: {str(e)}"


def validate_filename(filename, expected_prefix):
    """检查文件名规范"""
    if not filename.lower().endswith('.png'):
        return False, f"文件名后缀错误: {filename} (应为 .png)"
    
    name = filename[:-4]  # 去掉 .png
    if not name.islower() or not all(c.isalnum() or c == '_' for c in name):
        return False, f"文件名格式错误: {filename} (应为小写字母+下划线)"
    
    return True, f"✓ 文件名规范"


# ============================================================================
# 主验证流程
# ============================================================================
def validate_assets():
    """验证所有资源"""
    
    print("=" * 70)
    print("🔍 AI World 资源验证工具")
    print("=" * 70)
    print()
    
    total_pass = 0
    total_fail = 0
    total_warn = 0
    
    results = {}
    
    for category, spec in ASSET_SPECS.items():
        print(f"\n📂 检查: {category}")
        print("-" * 70)
        
        category_pass = 0
        category_fail = 0
        category_warn = 0
        
        path = spec["path"]
        if not os.path.exists(path):
            print(f"❌ 目录不存在: {path}")
            total_fail += 1
            results[category] = {"status": "FAIL", "reason": "目录不存在"}
            continue
        
        files = sorted([f for f in os.listdir(path) if f.endswith('.png')])
        
        if len(files) != spec["count"]:
            print(f"⚠ 文件数量不符: {len(files)} 个 (应为 {spec['count']} 个)")
            category_warn += 1
            total_warn += 1
        
        for filename in files:
            filepath = os.path.join(path, filename)
            print(f"\n  📄 {filename}")
            
            # 检查文件名
            fname_ok, fname_msg = validate_filename(filename, category)
            if fname_ok:
                print(f"    ✓ {fname_msg}")
            else:
                print(f"    ❌ {fname_msg}")
                category_fail += 1
                total_fail += 1
                continue
            
            # 检查格式
            fmt_ok, fmt_msg = validate_file_format(filepath)
            print(f"    {'✓' if fmt_ok else '❌'} {fmt_msg}")
            if not fmt_ok:
                category_fail += 1
                total_fail += 1
                continue
            
            # 检查尺寸
            dim_ok, dim_msg = validate_dimensions(filepath, spec["size"])
            print(f"    {'✓' if dim_ok else '❌'} {dim_msg}")
            if not dim_ok:
                category_fail += 1
                total_fail += 1
                continue
            
            # 检查透明度
            trans_ok, trans_msg = validate_transparency(filepath)
            print(f"    {'✓' if trans_ok else '❌'} {trans_msg}")
            if not trans_ok:
                category_fail += 1
                total_fail += 1
                continue
            
            # 检查文件大小
            size_status, size_msg = validate_file_size(filepath)
            if size_status == "warning":
                print(f"    ⚠ {size_msg}")
                category_warn += 1
                total_warn += 1
            elif size_status:
                print(f"    ✓ {size_msg}")
            else:
                print(f"    ❌ {size_msg}")
                category_fail += 1
                total_fail += 1
            
            category_pass += 1
            total_pass += 1
        
        # 类别总结
        print(f"\n  📊 {category} 总结:")
        print(f"     ✓ 通过: {category_pass}")
        print(f"     ❌ 失败: {category_fail}")
        if category_warn > 0:
            print(f"     ⚠ 警告: {category_warn}")
        
        results[category] = {
            "status": "PASS" if category_fail == 0 else "FAIL",
            "pass": category_pass,
            "fail": category_fail,
            "warnings": category_warn,
        }
    
    # 总体结果
    print("\n" + "=" * 70)
    print("📊 验证总结")
    print("=" * 70)
    print(f"✓ 通过: {total_pass}")
    print(f"❌ 失败: {total_fail}")
    if total_warn > 0:
        print(f"⚠ 警告: {total_warn}")
    print()
    
    if total_fail == 0:
        print("✅ 所有资源验证通过!")
        print("📦 可以安全打包并部署到游戏项目")
        return True
    else:
        print("❌ 发现问题，请修复后重新检查")
        return False


def check_manifest():
    """检查资源清单是否存在"""
    if os.path.exists("assets/manifest.json"):
        try:
            with open("assets/manifest.json", 'r') as f:
                manifest = json.load(f)
            print("\n📋 资源清单:")
            print(f"   版本: {manifest.get('version')}")
            print(f"   总数: {manifest.get('total_assets')} 个资源")
            return True
        except Exception as e:
            print(f"\n⚠ 清单文件读取失败: {e}")
            return False
    return False


if __name__ == "__main__":
    success = validate_assets()
    check_manifest()
    
    print("\n" + "=" * 70)
    if success:
        print("🚀 下一步: python3 generate_assets.py 并打包成 ZIP")
    else:
        print("⚠ 请修复上述问题后再次运行本脚本")
    print("=" * 70)
