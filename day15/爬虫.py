import subprocess
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# 数据队列（只保留最近 30 次的数据）
max_len = 30
gpu_util_list = deque(maxlen=max_len)
mem_used_list = deque(maxlen=max_len)
timestamps = deque(maxlen=max_len)

def get_gpu_data():
    try:
        result = subprocess.check_output([
            'nvidia-smi',
            '--query-gpu=utilization.gpu,memory.used',
            '--format=csv,noheader,nounits'
        ], encoding='utf-8')

        util, mem = result.strip().split(', ')
        return int(util), int(mem)
    except Exception as e:
        print(f"获取GPU信息失败: {e}")
        return 0, 0

def update(frame):
    import datetime
    util, mem = get_gpu_data()
    time_str = datetime.datetime.now().strftime("%H:%M:%S")

    gpu_util_list.append(util)
    mem_used_list.append(mem)
    timestamps.append(time_str)

    ax1.clear()
    ax2.clear()

    ax1.plot(timestamps, gpu_util_list, label="GPU 利用率 (%)", color="skyblue")
    ax2.plot(timestamps, mem_used_list, label="显存占用 (MB)", color="salmon")

    ax1.set_ylim(0, 100)
    ax2.set_ylim(0, 4096)  # 你的GPU是 4GB
    ax1.set_ylabel("利用率 (%)")
    ax2.set_ylabel("显存 (MB)")
    ax1.set_title("GPU 利用率")
    ax2.set_title("显存使用")

    for ax in [ax1, ax2]:
        ax.legend(loc="upper left")
        ax.grid(True)
        ax.tick_params(axis='x', labelrotation=45)

# 设置图表窗口
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
ani = animation.FuncAnimation(fig, update, interval=2000)  # 每 2 秒更新

plt.tight_layout()
plt.show()