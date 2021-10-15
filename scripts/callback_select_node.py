import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_cytoscape as cyto
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ネットワーク図の定義
cyto_compo = cyto.Cytoscape(
    id="cyto-compo",
    style={"width": "400px", "height": "400px"},
    # (1) ネットワークの構成要素の定義
    elements=[
        # ノードの定義
        {"data": {"id": "A", "name": "Alice", "club": "科学部"}},
        {"data": {"id": "B", "name": "Bob", "club": "美術部"}},
        {"data": {"id": "C", "name": "Carol", "club": "ボクシング部"}},
        # エッジの定義
        {"data": {"source": "A", "target": "B", "label": "A - B"}},
        {"data": {"source": "B", "target": "C", "label": "B - C"}},
    ],
    # (2) ノード配置方法の定義
    layout={"name": "circle"},
    # (3) スタイルの定義
    stylesheet=[
        # ノード全体に対するスタイル指定（グループセレクタ）
        # ラベル = ノードのdata辞書の"id"キーを使う
        {"selector": "node", "style": {"content": "data(id)"}},
    ],
)

# タップしたノードの情報を表示するためのDiv領域を作成
div_info = html.Div(
    id="div_info-compo",
    children="ここにタップしたノードの情報が表示されます",
    style={
        "background-color": "#CCCCCC",
        "width": 700,
        "height": 50,
        "font-size": "30px",
    },
)

# ドロップダウンとネットワーク図を縦に並べて配置
app.layout = html.Div([div_info, cyto_compo])

# コールバックの定義
@app.callback(
    Output("div_info-compo", "children"),  # 出力項目
    [Input("cyto-compo", "selectedNodeData")],  # 入力項目
)
def callback_select(node_data_dict):
    if node_data_dict is None:
        # 画面表示時にはNoneが渡されるので、デフォルト値を返す
        return "ここにタップしたノードの情報が表示されます"
    # タップしたノードのデータ辞書をそのまま返す
    return str(node_data_dict)


if __name__ == "__main__":
    app.run_server(debug=True)
