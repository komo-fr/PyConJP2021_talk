import dash
import dash_cytoscape as cyto
import dash_html_components as html

# Dashインスタンスの生成
app = dash.Dash(__name__)

# Cytoscapeコンポーネントの生成
cyto_compo = cyto.Cytoscape(
    id="hello-dash-cyto",
    style={"width": "400px", "height": "400px"},
    # (1) ネットワークの構成要素の定義
    elements=[
        # ノードの定義
        {"data": {"id": "A", "my_color": "gray"}},
        {"data": {"id": "B", "my_color": "red"}},
        {"data": {"id": "C", "my_color": "blue"}},
        # エッジの定義
        {"data": {"source": "A", "target": "B", "label": "A - B"}},
        {"data": {"source": "B", "target": "C", "label": "B - C"}},
    ],
    # (2) ノード配置方法の定義
    # Cytoscape.jsで用意されているアルゴリズムを利用できる
    layout={"name": "grid"},
    # (3) スタイルの定義
    stylesheet=[
        # ノード全体に対するスタイル指定（グループセレクタ）
        # 背景色 = ノードのdata辞書の"my_color"キーを使う
        {"selector": "node", "style": {"background-color": "data(my_color)"}},
        # ラベル = ノードのdata辞書の"id"キーを使う
        {"selector": "node", "style": {"content": "data(id)"}},
    ],
)

# Cytoscapeコンポーネントをレイアウトに渡す
app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    # サーバの起動
    app.run_server(debug=True)
