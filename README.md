# GrassFire-Agent-MAS

> 空天地一体化草原火智能识别 Multi-Agent System

基于多智能体系统（MAS）与强化学习的草原火实时监测与决策系统，融合天基卫星广域感知、空基无人机精准识别、地基传感网边缘计算，实现"感知-推理-验证-决策"闭环。

## 核心特性

- **三层 Agent 协同**：天基卫星 Agent（广域热异常扫描）+ 空基无人机 Agent（轻量化 YOLO 烟羽识别）+ 地基传感网 Agent（边缘计算温湿烟雾）
- **长链推理机制**：协调 Agent 对多源异构数据进行时空对齐与置信度加权融合
- **物理 GAN 增强**：基于 CFD 烟雾扩散模拟生成高保真训练样本，提升小样本场景检测鲁棒性
- **RL 动态决策引擎**：根据火势等级、风速风向、植被可燃性等多维因子，自主调度最优观测 Agent 组合与飞行路径
- **轻量化部署**：YOLOv8-n 适配 Jetson Nano 边缘设备，单帧推理 12ms

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/yourname/GrassFire-Agent-MAS.git
cd GrassFire-Agent-MAS

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置参数（修改 config.yaml 中的 API Key 与设备地址）
# 4. 启动协调器
python main.py --config config.yaml
```

## 项目结构

```
GrassFire-Agent-MAS/
├── main.py                 # 协调器入口
├── config.yaml             # 全局配置
├── requirements.txt        # 依赖
├── agents/                 # Agent 核心模块
│   ├── coordinator.py      # 协调 Agent
│   ├── satellite_agent.py  # 天基卫星 Agent
│   ├── uav_agent.py        # 空基无人机 Agent
│   └── ground_agent.py     # 地基传感网 Agent
├── models/                 # 模型权重（需单独下载）
│   └── README.md
└── docs/                   # 架构与 API 文档
```

## 系统架构

```
[Satellite Agent] ──┐
                   ├─→ [Coordinator Agent] ──→ [Physics GAN] ──┐
[UAV Agent] ────────┤   (时空对齐/置信度融合)      (CFD模拟增强)  │
                   │                                          ├─→ [RL Decision] ──→ Output
[Ground Agent] ────┘                                         │   (动态调度/路径规划)
                                                              └── [Consensus]
```

## 配置说明

编辑 `config.yaml`：

- `satellite.api_endpoint`: 卫星数据接口地址
- `uav.model_path`: YOLOv8-n 本地权重路径
- `ground.edge_nodes`: 边缘传感节点 IP 列表
- `rl.model_path`: RL 策略网络权重路径

## 性能指标

| 指标 | 数值 |
|------|------|
| 火点识别准确率 | 94.2% |
| 平均响应延迟 | 18.3s |
| 单帧推理时间 | 12.4ms (Jetson Nano) |
| 多 Agent 共识置信度 | 0.94 |

## 引用

如果你使用了本项目，请引用：

```bibtex
@software{grassfire_agent_mas,
  title = {GrassFire-Agent-MAS: Multi-Agent System for Grassland Fire Detection},
  author = {qinhuaiyang},
  year = {2026},
  url = {https://github.com/yourname/GrassFire-Agent-MAS}
}
```

## License

MIT License
