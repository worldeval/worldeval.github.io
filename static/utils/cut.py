from moviepy import VideoFileClip
import os

def trim_video_to_81_frames(video_path):
    # 打开视频文件
    clip = VideoFileClip(video_path)
    
    # 获取视频的基本信息
    fps = clip.fps
    duration_for_81_frames = 81 / fps
    
    # 计算输出视频的文件名
    base_name = os.path.basename(video_path)
    name, ext = os.path.splitext(base_name)
    output_name = f"{name}_trimmed{ext}"
    output_path = os.path.join(os.path.dirname(video_path), output_name)
    
    # 如果视频帧数大于81，进行裁剪
    if clip.duration > duration_for_81_frames:
        # 裁剪视频
        trimmed_clip = clip.subclipped(0, duration_for_81_frames)
        
        # 保存视频
        trimmed_clip.write_videofile(output_path)
        
        # 释放资源
        trimmed_clip.close()
    
    clip.close()
    print(f"视频已保存为: {output_path}")

# 定义要处理的视频文件路径列表
video_paths = [
    # 'static/videos/bussing_table/scuess/brown_bowl_pi0_real_frame_0.mp4',
    # 'static/videos/bussing_table/scuess/brown_mug_pi0_real_frame_0.mp4',
    # 'static/videos/collect_toy/scuess/pika_pi0_real_frame_0.mp4',
    'static/videos/place_cup/scuess/place_cup_dex_real_dou.mp4',
    # 'static/videos/handover_block/scuess/dex_real_frame_100.mp4',
    # 'static/videos/bussing_table/scuess/green_mug_pi0_real_frame_0.mp4',
    # 'static/videos/bussing_table/fail/green_plate_pi0_real_frame_0_fail.mp4',
    # 'static/videos/bussing_table/fail/brown_mug_pi0_real_frame_0_fail.mp4',
    # 'static/videos/collect_toy/fail/pika_pi0_real_frame_0_fail.mp4',
    # 'static/videos/place_cup/fail/place_cup_dex_real_fail_double.mp4',
    # 'static/videos/handover_block/fail/dex_real_frame_100_fail.mp4',
    # 'static/videos/bussing_table/fail/green_mug_pi0_real_10_frame_0_fail.mp4'
    # 可以添加更多视频路径
]

# 遍历处理每个视频
for video_path in video_paths:
    print(f"正在处理视频: {video_path}")
    trim_video_to_81_frames(video_path)
    print("处理完成")