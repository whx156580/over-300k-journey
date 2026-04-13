import matplotlib.pyplot as plt
import numpy as np

def generate_radar_chart(categories, values, title="30W+ 复合型人才能力雷达图"):
    """
    生成能力雷达图并保存。
    """
    # 处理中文字体，根据系统环境调整
    plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
    plt.rcParams['axes.unicode_minus'] = False

    num_vars = len(categories)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # 雷达图需闭合
    values += values[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    # 填充颜色与线条
    ax.fill(angles, values, color='teal', alpha=0.3)
    ax.plot(angles, values, color='teal', linewidth=2)
    
    # 设置刻度标签
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12)
    
    # 设置纵轴范围 (1-100)
    ax.set_ylim(0, 100)
    ax.set_yticklabels([20, 40, 60, 80, 100], color="grey", size=10)
    
    plt.title(title, size=16, color='teal', y=1.1)
    
    output_file = "capability_radar.png"
    plt.savefig(output_file)
    print(f"✅ 雷达图已生成并保存为: {output_file}")
    plt.show()

if __name__ == "__main__":
    # 示例数据 (候选人自评/面试官评分)
    categories = [
        '自动化框架', 'CI/CD 门禁', '质量度量', '全链路压测', 
        '后端高并发', '前端架构', 'MLOps', '大模型应用', 'AIOps'
    ]
    # 请根据实际评估结果修改以下分值 (0-100)
    scores = [90, 85, 80, 85, 80, 75, 70, 85, 75]
    
    generate_radar_chart(categories, scores)
