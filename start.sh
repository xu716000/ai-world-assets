#!/bin/bash
# AI World Assets - Quick Start Script
# 快速启动游戏美术资源生成

echo "=========================================="
echo "🎨 AI World - 游戏美术资源包生成器"
echo "=========================================="
echo ""

# 检查 Python 环境
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到 Python 3"
    echo "请先安装 Python 3.7 或更高版本"
    exit 1
fi

echo "✓ Python 版本检查通过"
python3 --version

# 检查依赖
echo ""
echo "📦 检查依赖..."
pip3 list | grep -q "Pillow" || pip3 install Pillow

echo ""
echo "=========================================="
echo "🚀 开始生成资源..."
echo "=========================================="
echo ""

# 运行生成脚本
python3 generate_assets.py

# 检查是否成功
if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✅ 资源生成完成!"
    echo "=========================================="
    echo ""
    echo "📦 打包文件: AI统治世界_assets_v1.zip"
    echo "📁 解压位置: ai-world/assets/"
    echo ""
    echo "接下来的步骤:"
    echo "1. cp AI统治世界_assets_v1.zip /path/to/ai-world/"
    echo "2. unzip AI统治世界_assets_v1.zip"
    echo "3. 刷新游戏即可!"
    echo ""
else
    echo ""
    echo "❌ 资源生成失败"
    echo "请检查错误日志"
    exit 1
fi
