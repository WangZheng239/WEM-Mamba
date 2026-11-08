import sys
import os
import importlib.util

def load_core_module():
    pyc_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "core_model.pyc")
    
    if not os.path.exists(pyc_path):
        raise FileNotFoundError(f"未找到核心模块: {pyc_path}")
    
    spec = importlib.util.spec_from_file_location("core_model", pyc_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# 加载核心模块
core = load_core_module()
DWT_Mamba_AttentionOptimized = core.DWT_Mamba_AttentionOptimized

if __name__ == "__main__":
    import torch
    print("成功加载二进制模块！")
    model = DWT_Mamba_AttentionOptimized(num_classes=2)
    print(f"模型总参数量: {sum(p.numel() for p in model.parameters()):,}")