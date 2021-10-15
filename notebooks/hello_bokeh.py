from bokeh.plotting import figure, output_notebook, output_file, show
from bokeh.models import GraphRenderer, Circle, MultiLine
from bokeh.models import Ellipse, GraphRenderer, StaticLayoutProvider
from bokeh.models import ColumnDataSource, Text, Plot

# プロットを作成
plot = figure(plot_width=400, plot_height=400)

# ネットワーク図のためのレンダラを作成
graph_renderer = GraphRenderer()

# (1) ネットワーク構造の定義
# ノードの定義
graph_renderer.node_renderer.data_source.data = {
    "index": ["A", "B", "C"],  # ノードID（必須）
    "my_color": ["gray", "red", "blue"],  # 任意の属性（スタイル設定などで使える）
}

# エッジの定義
graph_renderer.edge_renderer.data_source.data = {
    "start": ["A", "B"],  # ノードの始点リスト
    "end": ["B", "C"],  # ノードの終点リスト
}

# (2) ノード配置方法の定義
graph_layout = {"A": (0, 1), "B": (1, 0), "C": (-1, 0)}  # 各ノードのXY座標値が入った辞書
graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# (3) スタイルの設定
# ノードのスタイルの定義
graph_renderer.node_renderer.glyph = Circle(size=25, fill_color="my_color")

# エッジのスタイルの定義
graph_renderer.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_width=4)

# プロットにネットワーク図を追加
plot.renderers.append(graph_renderer)

# ファイルに保存
output_file("hello_bokeh.html")

# プロットを表示
show(plot)
