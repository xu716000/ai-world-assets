# AI World - 游戏美术资源包

完整的等距视角游戏资源库，包含建筑、单位、地形、UI图标和战斗特效。

## 📋 资源总览（共 48 张）

### 第一批：核心资源 ⭐ (优先级最高)
- **建筑 (4)**: b_hq, b_powerplant, b_factory, b_dock
- **单位 (2)**: u_infantry, u_tank  
- **UI图标 (8)**: i_ore, i_metal, i_wood, i_fuel, i_power, i_pop, i_credit, i_gear

### 第二批：扩展资源
- **建筑 (10)**: b_house, b_barracks, b_lab, b_turret, b_storage, b_derrick, b_smelter, b_solar, b_drill, b_dockyard
- **单位 (4)**: u_mech, u_gunship, u_paratroop, u_raider

### 第三批：敌方版本 + 地形 + 特效
- **敌方建筑 (14)**: 所有建筑的红色版本 (添加 _e 后缀)
- **敌方单位 (2)**: u_infantry_e, u_tank_e
- **地形 (4)**: t_rock, t_ore, t_forest, t_oil
- **战斗特效 (7)**: bullet, muzzle_flash, spark, explosion, shake, hit_flash, debris

## 🎨 严格规范表

| 类别 | 尺寸 | 背景 | 描边 | 光源 | 风格 | 锚点 |
|-----|------|------|------|------|------|------|
| 建筑 | 128×128px | PNG RGBA透明 | 2px霓虹蓝/红 | 左上45° | 扁平+硬阴影 | 底边中心 |
| 单位 | 64×64px | PNG RGBA透明 | 2px霓虹蓝/红 | 左上45° | 扁平+硬阴影 | 底边中心 |
| 地形 | 64×80px | PNG RGBA透明 | 2px霓虹蓝/红 | 左上45° | 扁平+硬阴影 | 底边中心 |
| 图标 | 32×32px | PNG RGBA透明 | 2px霓虹蓝/红 | 左上45° | 扁平+硬阴影 | 底边中心 |
| 特效 | 自适应 | PNG RGBA透明 | 根据需要 | - | 硬核爆炸效果 | - |

### ❌ 严禁事项
```
✗ 渐变效果（只用色块）
✗ 文字和水印
✗ 复杂细节或高保真
✗ 软边阴影（只用硬阴影）
✗ 半透明过渡
```

### ✓ 必须要求
```
✓ 等距视角（Isometric）
✓ 纯色块 + 硬阴影
✓ 2px 霓虹描边
✓ 左上45°单一光源
✓ 底边中心锚点对齐
✓ PNG RGBA 无损
```

## 🎨 配色方案

### 🔵 蓝方（我方）
```
主色：    #0080FF (纯蓝)
亮色：    #00BFFF (亮蓝)
描边：    #0000FF (霓虹蓝)
阴影：    #001A4D (深蓝)
高亮：    #00FFFF (青蓝)
```

### 🔴 红方（敌方）
```
主色：    #CC0000 (深红)
亮色：    #FF4444 (亮红)
描边：    #FF0000 (霓虹红)
阴影：    #660000 (暗红)
高亮：    #FF6666 (淡红)
```

### ⚪ 中性资源
```
i_ore:     #00FFFF 蓝晶（主色）+ #0088FF 阴影
i_metal:   #E0E0E0 银灰（主色）+ #808080 阴影
i_wood:    #CD853F 棕色（主色）+ #8B4513 阴影
i_fuel:    #FFD700 黄金（主色）+ #B8A000 阴影
i_power:   #FFFF00 黄色 + #0080FF 蓝色闪电
i_pop:     #00FF00 绿色（主色）+ #008800 阴影
i_credit:  #FFB700 金色（主色）+ #997700 阴影
i_gear:    #A0A0A0 机械灰（主色）+ #606060 阴影
```

## 📁 项目结构

```
ai-world-assets/
│
├── 📦 assets/                          # 最终游戏资源目录
│   ├── buildings/                      # 建筑（14个）
│   │   ├── b_hq.png                   # 主基地
│   │   ├── b_powerplant.png           # 发电站
│   │   ├── b_factory.png              # 工厂
│   │   ├── b_dock.png                 # 船坞
│   │   ├── b_house.png                # 民居
│   │   ├── b_barracks.png             # 兵营
│   │   ├── b_lab.png                  # 研究所
│   │   ├── b_turret.png               # 防御塔
│   │   ├── b_storage.png              # 仓库
│   │   ├── b_derrick.png              # 油井
│   │   ├── b_smelter.png              # 冶炼厂
│   │   ├── b_solar.png                # 太阳能板
│   │   ├── b_drill.png                # 钻井
│   │   └── b_dockyard.png             # 造船厂
│   │
│   ├── buildings_enemy/                # 敌方建筑（14个）
│   │   ├── b_hq_e.png
│   │   ├── b_powerplant_e.png
│   │   └── ... (同上，红色版本)
│   │
│   ├── units/                          # 单位（6个）
│   │   ├── u_infantry.png             # 步兵
│   │   ├── u_tank.png                 # 坦克
│   │   ├── u_mech.png                 # 机甲
│   │   ├── u_gunship.png              # 炮艇
│   │   ├── u_paratroop.png            # 空降兵
│   │   └── u_raider.png               # 掠夺者
│   │
│   ├── units_enemy/                    # 敌方单位（6个）
│   │   ├── u_infantry_e.png
│   │   ├── u_tank_e.png
│   │   └── ... (同上，红色版本)
│   │
│   ├── terrain/                        # 地形（4个）
│   │   ├── t_rock.png                 # 岩石
│   │   ├── t_ore.png                  # 矿物
│   │   ├── t_forest.png               # 森林
│   │   └── t_oil.png                  # 油田
│   │
│   ├── icons/                          # UI图标（8个）
│   │   ├── i_ore.png                  # 矿石
│   │   ├── i_metal.png                # 金属
│   │   ├── i_wood.png                 # 木材
│   │   ├── i_fuel.png                 # 燃料
│   │   ├── i_power.png                # 电力
│   │   ├── i_pop.png                  # 人口
│   │   ├── i_credit.png               # 信用点
│   │   └── i_gear.png                 # 科技
│   │
│   └── effects/                        # 战斗特效（7个）
│       ├── bullet.png                 # 曳光弹
│       ├── muzzle_flash.png           # 炮口闪光
│       ├── spark.png                  # 命中火花
│       ├── explosion.png              # 爆炸
│       ├── shake.png                  # 震屏效果
│       ├── hit_flash.png              # 受击白闪
│       └── debris.png                 # 碎片
│
├── 📋 docs/
│   ├── ASSET_SPEC.md                  # 详细规范文档
│   ├── COLOR_PALETTE.md               # 颜色方案
│   ├── ISOMETRIC_GUIDE.md             # 等距视角教程
│   └── PRODUCTION_LOG.md              # 制作日志
│
├── 🔧 scripts/
│   ├── generate_assets.py             # 批量生成脚本
│   ├── validate_assets.py             # 资源验证脚本
│   ├── compress_assets.py             # 资源压缩脚本
│   └── color_palette.json             # 颜色配置
│
└── README.md                           # 本文件
```

## 🚀 快速开始

### 1. 复制到项目
```bash
# 克隆仓库
git clone https://github.com/xu716000/ai-world-assets.git

# 复制 assets 文件夹到游戏项目
cp -r ai-world-assets/assets/ /path/to/ai-world/
```

### 2. 验证资源
```bash
# 安装依赖
pip install pillow

# 运行验证脚本
python scripts/validate_assets.py
```

### 3. 在游戏中使用
```javascript
// 伪代码示例
const hqBuilding = new Building({
  sprite: 'assets/buildings/b_hq.png',
  width: 128,
  height: 128,
  anchor: {x: 0.5, y: 1.0}  // 底边中心
});

const infantryUnit = new Unit({
  sprite: 'assets/units/u_infantry.png',
  width: 64,
  height: 64,
  anchor: {x: 0.5, y: 1.0}
});
```

## 📊 制作进度

- [ ] **第一批** - 12个核心资源 
  - [ ] 建筑 (4): b_hq, b_powerplant, b_factory, b_dock
  - [ ] 单位 (2): u_infantry, u_tank
  - [ ] 图标 (8): i_ore, i_metal, i_wood, i_fuel, i_power, i_pop, i_credit, i_gear

- [ ] **第二批** - 14个扩展资源
  - [ ] 建筑 (10): b_house, b_barracks, b_lab, b_turret, b_storage, b_derrick, b_smelter, b_solar, b_drill, b_dockyard
  - [ ] 单位 (4): u_mech, u_gunship, u_paratroop, u_raider

- [ ] **第三批** - 36个完整资源
  - [ ] 敌方建筑 (14)
  - [ ] 敌方单位 (2)
  - [ ] 地形 (4)
  - [ ] 战斗特效 (7)

## 🎬 美术制作指南

### 推荐工具
- **Aseprite** - 最佳选择（支持像素画、分层）
- **Piskel** - 免费在线工具
- **Krita** - 专业绘画软件
- **ImageMagick** - 批量处理脚本

### 制作流程
1. **参考 3D 模型** → 参照提供的参考图
2. **粗稿** → 绘制基本形状 (40×40px 草图)
3. **精细化** → 添加细节和纹理 (目标尺寸)
4. **添加描边** → 2px 外描边 (Outline)
5. **阴影** → 左上45°硬阴影，占总高度15%
6. **导出** → PNG RGBA，无损

### 等距视角比例
```
标准等距角度：30-60-90 三角形
宽度：高度 = 2:1
建筑：128×128 (宽：高 = 1:1 显示)
单位：64×64
地形：64×80 (加高度差)
```

## 📦 文件规范清单

- [ ] 所有图片 PNG RGBA 格式
- [ ] 尺寸精确 (不含透明边框)
- [ ] 2px 霓虹描边完整
- [ ] 硬阴影清晰可见
- [ ] 锚点底边中心对齐
- [ ] 文件名小写 + 下划线
- [ ] 无渐变、无文字、无水印

## 📞 技术支持

- **格式问题**: 检查 PNG RGBA 设置
- **尺寸错误**: 使用验证脚本检查
- **颜色不对**: 参考 `docs/COLOR_PALETTE.md`
- **效果要求**: 查看参考图 (Image 1-3)

---

**项目版本**: v1.0-beta  
**制作日期**: 2026-09-12  
**资源总数**: 48 张  
**目标完成**: 2026-09-30

🎮 **Ready to make this game beautiful!**
