import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_cytoscape as cyto
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ノードの配置方法を指定するドロップダウンを定義
drop_compo = dcc.Dropdown(
    id="drop-compo",
    style={"width": "150px", "fontSize": "28px"},
    clearable=False,
    value="gray",  # デフォルト値
    options=[
        {"label": "red", "value": "red"},
        {"label": "blue", "value": "blue"},
        {"label": "gray", "value": "gray"},
    ],
)

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
        # 背景色の初期状態はグレー
        {"selector": "node", "style": {"background-color": "gray"}},
        # ラベル = ノードのdata辞書の"id"キーを使う
        {"selector": "node", "style": {"content": "data(id)"}},
    ],
)

# ドロップダウンとネットワーク図を縦に並べて配置
app.layout = html.Div([drop_compo, cyto_compo])

# コールバックの定義
@app.callback(
    Output("cyto-compo", "stylesheet"),  # 出力項目: スタイルを変化させる
    [Input("drop-compo", "value")],  # 入力項目: ドロップダウンの値を受け取る
)
def update_stylesheet(new_color):
    # ドロップダウンで選択した値を使って、ノードの配置を変更
    new_stylesheet = [
        # 新しい背景色で更新
        {"selector": "node", "style": {"background-color": new_color}},
        # ラベルの表示設定はデフォルトのまま
        {"selector": "node", "style": {"content": "data(id)"}},
    ]
    return new_stylesheet


if __name__ == "__main__":
    app.run_server(debug=True)
