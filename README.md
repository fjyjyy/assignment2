# 第一章：分工list

**组长**：吴珂珂  
**组员**：吴江晓，张浩，彭珊珊，吴昊，薛政宇

## 分工情况

### 第一小组：新能源汽车刹车失灵事件
- **成员**：吴昊，薛政宇
- **任务分工**：
  - **吴昊**：负责代码的生成及运行
  - **薛政宇**：负责详细步骤的整理

### 第二小组：基于人工智能职位数据的多维度分析未来趋势
- **成员**：吴江晓，张浩，彭珊珊
- **任务分工**：
  - **吴江晓**：负责代码的生成及运行
  - **张浩**：负责详细步骤的整理
  - **彭珊珊**：负责详细步骤的整理

### 吴珂珂：负责统筹进度，整合作品。
---

# 第二章：代码及详细步骤

## 第一组：新能源汽车刹车失灵事件

### 代码

```python
import requests
import json
import csv
import random
import time

BASE_URL = "https://m.weibo.cn/api/container/getIndex"
QUERY = "231522type=1&q=刹车失灵"
HEADERS_LIST = [
    # 常见User-Agent，可自行扩展
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
]

def get_comments(page):
    headers = {
        "User-Agent": random.choice(HEADERS_LIST),
        "Accept": "application/json"
    }
    params = {
        "containerid": QUERY,
        "page_type": "searchall",
        "page": page
    }
    try:
        resp = requests.get(BASE_URL, headers=headers, params=params, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"请求失败，状态码: {resp.status_code}")
            return None
    except Exception as e:
        print(f"请求异常: {e}")
        return None

def parse_comments(json_data):
    comments = []
    if not json_data:
        return comments
    try:
        cards = json_data.get("data", {}).get("cards", [])
        for card in cards:
            if card.get("card_type") == 9:
                mblog = card.get("mblog", {})
                # 评论内容
                text = mblog.get("text", "")
                # 用户信息
                user = mblog.get("user", {})
                user_id = user.get("id", "")
                # 点赞数
                attitudes_count = mblog.get("attitudes_count", 0)
                # 发布时间
                created_at = mblog.get("created_at", "")
                # 设备来源
                source = mblog.get("source", "")
                comments.append([user_id, text, attitudes_count, created_at, source])
    except Exception as e:
        print(f"解析异常: {e}")
    return comments

def save_to_csv(data, filename):
    with open(filename, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["用户ID", "评论内容", "点赞数", "发布时间", "设备来源"])
        writer.writerows(data)

def main():
    all_comments = []
    for page in range(1, 101):
        print(f"正在爬取第{page}页...")
        json_data = get_comments(page)
        comments = parse_comments(json_data)
        if not comments:
            print("本页无数据，跳过。")
        else:
            all_comments.extend(comments)
        time.sleep(random.uniform(1, 3))
    save_to_csv(all_comments, "weibo_comments.csv")
    print("爬取完成，数据已保存为 weibo_comments.csv")

if __name__ == "__main__":
    main()
```
### 关键步骤截图
#### 1. 选择支持大模型的IDE（VS Code + GitHub Copilot）
操作步骤：

安装 VS Code 并登录 GitHub 账号。

在扩展商店中搜索并安装 GitHub Copilot。

新建一个Python文件（weibo_crawler.py）。

#### 2. 舆情事件与目标平台选择
事件：“某新能源汽车刹车失灵事件”
平台：微博（数据易获取，API友好）
目标链接：微博话题页 https://m.weibo.cn/search?containerid=231522type%3D1%26q%3D{关键词} （替换为实际事件关键词，如“刹车失灵”）。

#### 3. 爬虫开发：爬取微博话题评论
完整提示词（Copilot输入）
![image](https://github.com/user-attachments/assets/3a3011b6-5300-4fa9-a0b6-067116412320)

完整爬虫代码

![image](https://github.com/user-attachments/assets/94e13508-5519-4b5a-84d2-c1f7df9bfc9e)
![image](https://github.com/user-attachments/assets/df877742-407c-4441-b5a4-6aaba5852c8c)
#### 4. 数据爬取结果截图
生成的 weibo_comments.csv 示例数据：
![image](https://github.com/user-attachments/assets/7386b9e0-a545-4a20-9330-53245dc92116)
#### 5. Jupyter数据可视化分析
1. 基础设置与数据加载
![image](https://github.com/user-attachments/assets/e0c5fd70-66d2-44f5-8d88-b94fd110ec19)

2. 数据清洗

![image](https://github.com/user-attachments/assets/7e9be2b0-ba5e-4157-bd20-9dd00ca39301)

3. 可视化代码

图表1：24小时评论分布

![image](https://github.com/user-attachments/assets/5e65c52e-270d-418f-84bc-43ce42fc0bd0)

图表2：点赞数分布（过滤极端值）

![image](https://github.com/user-attachments/assets/6dd08c7c-d452-440b-883c-7a1adb560adc)

图表3：每日评论趋势

![image](https://github.com/user-attachments/assets/27bc1ea1-31c1-4c91-a7bc-72704ced0dae)

图表4：设备来源分布

![image](https://github.com/user-attachments/assets/c1c10d84-6d4a-4946-b68e-844581cb8f14)

图表5：最活跃用户TOP10

![image](https://github.com/user-attachments/assets/762448f2-9bf2-4d64-9beb-e8d5ce4c03cf)
![image](https://github.com/user-attachments/assets/29daefc6-4265-4742-a324-d71022210442)

## 第二组：基于人工智能职位数据的多维度分析未来趋势

### 代码

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>DS 数据分析看板</title>
    <!-- 引入 ECharts 库 -->
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
    <!-- 引入词云图插件 -->
    <script src="https://cdn.jsdelivr.net/npm/echarts-wordcloud@2.0.0/dist/echarts-wordcloud.min.js"></script>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #051c3a;
            color: #fff;
        }

        .dashboard-container {
            max-width: 1600px;
            margin: 0 auto;
        }

        .dashboard-header {
            text-align: center;
            margin-bottom: 30px;
        }

        .dashboard-title {
            font-size: 32px;
            margin: 0;
            color: #fff;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
        }

        .kpi-container {
            display: flex;
            justify-content: space-between;
            margin-bottom: 30px;
        }

        .kpi-card {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 20px;
            width: 19%;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s;
        }

        .kpi-card:hover {
            transform: translateY(-5px);
        }

        .kpi-title {
            font-size: 16px;
            color: #a8c7ff;
            margin-bottom: 10px;
        }

        .kpi-value {
            font-size: 28px;
            font-weight: bold;
            color: #fff;
        }

        .chart-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 30px;
        }

        .chart-container {
            width: 48%;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .chart-title {
            font-size: 18px;
            margin-bottom: 15px;
            color: #a8c7ff;
            text-align: center;
        }

        .conclusion-container {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
        }

        .conclusion-title {
            font-size: 20px;
            margin-bottom: 15px;
            color: #a8c7ff;
        }

        .conclusion-list {
            list-style-type: none;
            padding: 0;
        }

        .conclusion-list li {
            margin-bottom: 10px;
            line-height: 1.6;
        }
    </style>
</head>

<body>
    <div class="dashboard-container">
        <div class="dashboard-header">
            <h1 class="dashboard-title">DS 数据分析看板</h1>
            <p>基于人工智能职位数据的多维度分析</p>
        </div>

        <!-- KPI 指标卡片 -->
        <div class="kpi-container">
            <div class="kpi-card">
                <div class="kpi-title">总职位数量</div>
                <div class="kpi-value">200</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">平均薪资 (元/月)</div>
                <div class="kpi-value">12,500</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">最高薪资 (元/月)</div>
                <div class="kpi-value">200,000</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">最低薪资 (元/月)</div>
                <div class="kpi-value">3,000</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-title">职位分布城市</div>
                <div class="kpi-value">30+</div>
            </div>
        </div>

        <!-- 图表区域 -->
        <div class="chart-row">
            <div class="chart-container">
                <div class="chart-title">薪资分布 (柱状图)</div>
                <div id="salaryDistribution" style="width: 100%; height: 400px;"></div>
            </div>
            <div class="chart-container">
                <div class="chart-title">学历要求比例 (饼图)</div>
                <div id="educationDistribution" style="width: 100%; height: 400px;"></div>
            </div>
        </div>

        <div class="chart-row">
            <div class="chart-container">
                <div class="chart-title">职位数量趋势 (折线图)</div>
                <div id="jobTrend" style="width: 100%; height: 400px;"></div>
            </div>
            <div class="chart-container">
                <div class="chart-title">工作经验要求 (堆叠柱状图)</div>
                <div id="experienceDistribution" style="width: 100%; height: 400px;"></div>
            </div>
        </div>

        <div class="chart-row">
            <div class="chart-container">
                <div class="chart-title">技能要求词云图</div>
                <div id="skillWordCloud" style="width: 100%; height: 400px;"></div>
            </div>
            <div class="chart-container">
                <div class="chart-title">薪资与经验关系散点图</div>
                <div id="salaryExperienceScatter" style="width: 100%; height: 400px;"></div>
            </div>
        </div>

        <!-- 分析结论 -->
        <div class="conclusion-container">
            <h3 class="conclusion-title">分析结论</h3>
            <ul class="conclusion-list">
                <li>人工智能领域职位需求呈现多元化，主要集中在一线及新一线城市，其中北京、上海、深圳、杭州等城市职位数量占比较高。</li>
                <li>薪资水平跨度较大，从 3,000 元/月至 200,000 元/月不等，反映出不同职位层级和专业技能要求的巨大差异。高级专家和研究岗位的薪资明显高于初级职位。</li>
                <li>学历要求以大学本科和硕士研究生为主，表明人工智能行业对专业教育背景有较高要求。随着行业技术发展，对博士学历的需求也在逐渐增加。</li>
                <li>工作经验要求呈现两极化，部分职位对经验要求不限，而部分高级和专家职位则要求 3-5 年甚至 5-10 年的相关工作经验。</li>
                <li>从技能要求来看，Python、机器学习、深度学习、数据分析等是需求量较大的技能，掌握这些技能的人才在就业市场上更具竞争力。</li>
                <li>薪资与工作经验呈现正相关关系，但也存在一定的离散性，说明薪资水平还受到公司规模、行业领域、具体职位等多种因素的影响。</li>
            </ul>
        </div>
    </div>

    <script>
        // 初始化图表
        const salaryDistributionChart = echarts.init(document.getElementById('salaryDistribution'));
        const educationDistributionChart = echarts.init(document.getElementById('educationDistribution'));
        const jobTrendChart = echarts.init(document.getElementById('jobTrend'));
        const experienceDistributionChart = echarts.init(document.getElementById('experienceDistribution'));
        const skillWordCloudChart = echarts.init(document.getElementById('skillWordCloud'));
        const salaryExperienceScatterChart = echarts.init(document.getElementById('salaryExperienceScatter'));

        // 薪资分布柱状图
        salaryDistributionChart.setOption({
            color: ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272'],
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            xAxis: {
                type: 'category',
                data: ['3K-5K', '5K-8K', '8K-10K', '10K-15K', '15K-20K', '20K-30K', '30K-50K', '50K+'],
                axisLabel: {
                    color: '#a8c7ff'
                }
            },
            yAxis: {
                type: 'value',
                axisLabel: {
                    color: '#a8c7ff'
                }
            },
            series: [{
                name: '职位数量',
                type: 'bar',
                data: [15, 20, 25, 40, 35, 28, 22, 15],
                barWidth: '40%',
                itemStyle: {
                    borderRadius: [5, 5, 0, 0]
                }
            }]
        });

        // 学历要求比例饼图
        educationDistributionChart.setOption({
            tooltip: {
                trigger: 'item'
            },
            legend: {
                orient: 'vertical',
                right: '5%',
                top: 'center',
                textStyle: {
                    color: '#a8c7ff'
                }
            },
            series: [{
                name: '学历要求',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 10,
                    borderColor: '#051c3a',
                    borderWidth: 2
                },
                label: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: '16',
                        fontWeight: 'bold',
                        color: '#fff'
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                    { value: 40, name: '大学本科', itemStyle: { color: '#5470c6' } },
                    { value: 30, name: '硕士研究生', itemStyle: { color: '#91cc75' } },
                    { value: 15, name: '博士研究生', itemStyle: { color: '#fac858' } },
                    { value: 8, name: '大学专科', itemStyle: { color: '#ee6666' } },
                    { value: 7, name: '无学历要求', itemStyle: { color: '#73c0de' } }
                ]
            }]
        });

        // 职位数量趋势折线图（假设数据）
        jobTrendChart.setOption({
            color: ['#5470c6'],
            tooltip: {
                trigger: 'axis'
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
                axisLabel: {
                    color: '#a8c7ff'
                }
            },
            yAxis: {
                type: 'value',
                axisLabel: {
                    color: '#a8c7ff'
                }
            },
            series: [{
                name: '职位数量',
                type: 'line',
                data: [120, 132, 101, 134, 160, 130, 145, 180, 160, 170, 180, 190],
                smooth: true,
                lineStyle: {
                    width: 4
                },
                areaStyle: {
                    opacity: 0.2
                }
            }]
        });

        // 工作经验要求堆叠柱状图
        experienceDistributionChart.setOption({
            color: ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272'],
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            legend: {
                data: ['不限经验', '1-3年', '3-5年', '5-10年', '10年以上'],
                textStyle: {
                    color: '#a8c7ff'
                }
            },
            xAxis: {
                type: 'category',
                data: ['1月', '2月', '3月', '4月', '5月', '6月'],
                axisLabel: {
                    color: '#a8c7ff'
                }
            },
            yAxis: {
                type: 'value',
                axisLabel: {
                    color: '#a8c7ff'
                }
            },
            series: [
                {
                    name: '不限经验',
                    type: 'bar',
                    stack: 'total',
                    data: [30, 35, 32, 36, 38, 40]
                },
                {
                    name: '1-3年',
                    type: 'bar',
                    stack: 'total',
                    data: [25, 20, 23, 27, 25, 28]
                },
                {
                    name: '3-5年',
                    type: 'bar',
                    stack: 'total',
                    data: [20, 22, 18, 21, 23, 22]
                },
                {
                    name: '5-10年',
                    type: 'bar',
                    stack: 'total',
                    data: [15, 18, 16, 19, 16, 15]
                },
                {
                    name: '10年以上',
                    type: 'bar',
                    stack: 'total',
                    data: [10, 8, 11, 9, 8, 7]
                }
            ]
        });

        // 技能要求词云图
        skillWordCloudChart.setOption({
            tooltip: {
                show: true
            },
            series: [{
                type: 'wordCloud',
                gridSize: 20,
                sizeRange: [12, 60],
                rotationRange: [-90, 90],
                shape: 'circle',
                textStyle: {
                    color: function() {
                        // 随机颜色
                        return 'rgb(' + [
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160)
                        ].join(',') + ')';
                    },
                    emphasis: {
                        shadowBlur: 10,
                        shadowColor: '#333'
                    }
                },
                data: [
                    { name: 'Python', value: 10000 },
                    { name: '机器学习', value: 8000 },
                    { name: '深度学习', value: 7500 },
                    { name: '数据分析', value: 7000 },
                    { name: '人工智能', value: 6500 },
                    { name: '算法', value: 6000 },
                    { name: 'TensorFlow', value: 5500 },
                    { name: 'PyTorch', value: 5000 },
                    { name: '自然语言处理', value: 4500 },
                    { name: '计算机视觉', value: 4000 },
                    { name: '大数据', value: 3500 },
                    { name: 'Hadoop', value: 3000 },
                    { name: 'Spark', value: 3000 },
                    { name: 'SQL', value: 2500 },
                    { name: 'Linux', value: 2000 },
                    { name: 'Java', value: 1800 },
                    { name: 'C++', value: 1500 },
                    { name: 'R语言', value: 1500 },
                    { name: '数据挖掘', value: 1200 },
                    { name: '统计学', value: 1200 }
                ]
            }]
        });

        // 薪资与经验关系散点图
        salaryExperienceScatterChart.setOption({
            tooltip: {
                trigger: 'item',
                formatter: function(params) {
                    return '经验: ' + params.data[0] + '年<br>薪资: ' + params.data[1] + 'K/月';
                }
            },
            xAxis: {
                type: 'value',
                name: '工作经验(年)',
                min: 0,
                max: 15,
                axisLabel: {
                    color: '#a8c7ff'
                }
            },
            yAxis: {
                type: 'value',
                name: '薪资(K/月)',
                min: 0,
                max: 100,
                axisLabel: {
                    color: '#a8c7ff'
                }
            },
            series: [{
                name: '薪资与经验关系',
                type: 'scatter',
                data: [
                    [1, 10], [1, 12], [1, 15], [2, 15], [2, 18], [2, 20],
                    [3, 20], [3, 22], [3, 25], [4, 25], [4, 28], [4, 30],
                    [5, 30], [5, 35], [5, 40], [6, 35], [6, 40], [6, 45],
                    [7, 40], [7, 45], [7, 50], [8, 45], [8, 50], [8, 55],
                    [9, 50], [9, 55], [9, 60], [10, 55], [10, 60], [10, 70],
                    [11, 60], [11, 70], [11, 80], [12, 70], [12, 80], [12, 90],
                    [13, 80], [13, 90], [13, 100], [14, 90], [14, 100], [15, 100]
                ],
                symbolSize: function(data) {
                    // 根据数据大小调整点的大小
                    return data[1] / 5;
                },
                itemStyle: {
                    color: function(params) {
                        // 根据经验年限设置颜色
                        const years = params.data[0];
                        if (years < 3) return '#5470c6';
                        if (years < 5) return '#91cc75';
                        if (years < 8) return '#fac858';
                        return '#ee6666';
                    },
                    opacity: 0.8
                }
            }]
        });

        // 窗口大小变化时重新调整图表
        window.addEventListener('resize', function() {
            salaryDistributionChart.resize();
            educationDistributionChart.resize();
            jobTrendChart.resize();
            experienceDistributionChart.resize();
            skillWordCloudChart.resize();
            salaryExperienceScatterChart.resize();
        });
    </script>
</body>

</html>
```
### 关键步骤截图

1.用八爪鱼爬取数据

![image](https://github.com/user-attachments/assets/a1b15a50-68b4-4287-9b53-070a1d52858d)
![image](https://github.com/user-attachments/assets/3fe5e232-94a5-4d7f-86ff-0969c91b6dab)
![image](https://github.com/user-attachments/assets/e4d1a0e3-881e-402c-9fb7-6ccdf75d3c08)
![image](https://github.com/user-attachments/assets/0322c4f3-5817-4ae5-8000-31c4d4e6b2dc)

2.收集完成的数据：例图

![image](https://github.com/user-attachments/assets/609908bd-dfa7-4e54-bf58-6657bca97c9d)

3.用这些数据来完成舆情报告的分析以及前端的完成

![image](https://github.com/user-attachments/assets/4675de0d-a6ee-46f6-a040-fac4e5a6270b)
![image](https://github.com/user-attachments/assets/7ec99ac5-8e66-4542-aa93-f30d06e1b891)
![image](https://github.com/user-attachments/assets/70d2c33b-4d71-451d-b6f8-d229aa27b28a)

