@echo off
REM AI World Assets - Quick Start Script (Windows)
REM 快速启动游戏美术资源生成

setlocal enabledelayedexpansion

echo ==========================================
echo 🎨 AI World - 游戏美术资源包生成器 (Windows)
echo ==========================================
echo.

REM 检查 Python 环境
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未找到 Python
    echo 请先安装 Python 3.7 或更高版本
    echo 下载: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✓ Python 版本检查通过
python --version

echo.
echo 📦 检查依赖...
pip list | findstr "Pillow" >nul 2>&1
if errorlevel 1 (
    echo 安装 Pillow...
    pip install Pillow
)

echo.
echo ==========================================
echo 🚀 开始生成资源...
echo ==========================================
echo.

REM 运行生成脚本
python generate_assets.py

REM 检查是否成功
if errorlevel 1 (
    echo.
    echo ❌ 资源生成失败
    echo 请检查错误日志
    pause
    exit /b 1
)

echo.
echo ==========================================
echo ✅ 资源生成完成!
echo ==========================================
echo.
echo 📦 打包文件: AI统治世界_assets_v1.zip
echo 📁 解压位置: ai-world\assets\
echo.
echo 接下来的步骤:
echo 1. 将 AI统治世界_assets_v1.zip 复制到游戏目录
echo 2. 解压文件到 ai-world\assets\
echo 3. 刷新游戏即可!
echo.
pause
