#!/usr/bin/env python3
"""
GrassFire-Agent-MAS 入口文件
启动协调器，运行空天地一体化草原火监测主循环
"""
import argparse
import yaml
from loguru import logger
from agents.coordinator import CoordinatorAgent


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="GrassFire-Agent-MAS Coordinator")
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to config file")
    parser.add_argument("--cycles", type=int, default=3, help="Number of coordination cycles to run")
    args = parser.parse_args()

    logger.info("=" * 60)
    logger.info("GrassFire-Agent-MAS Starting...")
    logger.info("=" * 60)

    # 加载配置
    config = load_config(args.config)
    logger.info(f"Config loaded from: {args.config}")
    logger.info(f"System: {config['system']['name']} v{config['system']['version']}")

    # 初始化协调器
    coordinator = CoordinatorAgent(config)
    logger.info("CoordinatorAgent initialized")
    logger.info(f"Active agents: Satellite={coordinator.satellite.enabled}, "
                f"UAV={coordinator.uav.enabled}, Ground={coordinator.ground.enabled}")

    # 运行主循环
    logger.info(f"Running {args.cycles} coordination cycle(s)...")
    result = coordinator.run(max_cycles=args.cycles)

    logger.info("=" * 60)
    logger.info("Run completed.")
    logger.info(f"Total cycles: {result['total_cycles']}")
    logger.info(f"System status: {result['system_status']}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
