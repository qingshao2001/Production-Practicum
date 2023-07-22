import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

df = pd.read_csv("酷狗说书播放数据.csv", names=["名称", "播放量"])
list_x = list(df["名称"])
list_y = list(df["播放量"])

c = (
    Bar(init_opts=opts.InitOpts(width="1350px", height="550px"))
        .add_xaxis(list_x)
        .add_yaxis("播放量", list_y, color=Faker.rand_color(), )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="酷狗听书播放量"),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} 万"),
        ),
    )
        .render("酷狗听书播放量.html")
)
