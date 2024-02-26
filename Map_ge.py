from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo,Map
from pyecharts.globals import ChartType, SymbolType
from read import scenic_dict
c = (
        Geo()
        .add_schema(maptype="威海")
        .add_coordinate_json('data.json')
        .add(
            "景区",
            [list(z) for z in zip(list(scenic_dict.values()), [1]*13)],
            type_=ChartType.EFFECT_SCATTER,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            # visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="威海景点地图"),
        )
    )
c.render('my_chart.html')