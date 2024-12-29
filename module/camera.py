import detect
import threading


class Camera:
    def __init__(self, opts: dict = None):
        self.camera_thread = None               # 摄像头线程
        self.camera_open = None                 # 摄像头是否打开
        self.detect_class = -1                  # 检测到的水果种类
        self.detect_count = [0, 0]              # 检测到的水果数量：[优质、劣质]
        self.stop_event = threading.Event()     # 线程停止标志

        # 传入目标检测模型参数
        self.opts = detect.parse_opt(**opts)

    def run_detection(self, window, stop_event):
        """启动摄像头检测"""
        self.camera_open = True
        self.camera_thread = threading.Thread(target=detect.main, args=(window, self.opts, stop_event), daemon=True)
        self.camera_thread.start()

    def refresh_camera(self, window, opts):
        """重启摄像头检测（修改检测模型参数/摄像头卡死时可用）"""
        # 中断当前窗口
        self.camera_open = False
        self.stop_event.set()
        self.camera_thread.join()

        # 传入新的参数
        self.opts = detect.parse_opt(**opts)
        self.stop_event.clear()
        self.run_detection(window, self.stop_event)
