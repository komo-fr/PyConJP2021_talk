import dash
import dash_cytoscape as cyto
import dash_html_components as html
import pandas as pd
import networkx as nx

app = dash.Dash(__name__)

# NetworkXを使って空手データの読み込み
G = nx.karate_club_graph()

# NetworkXのGraphオブジェクト ⇨ Cytoscape用のデータ形式
cy_data = nx.readwrite.json_graph.cytoscape_data(G)

# Cytoscapeのデータ形式 ⇨ Dash Cytoscapeのデータ形式
def convert_data_dict(data_dict):
    # 辞書内の値をすべて文字列に変換する
    return {k: str(v) for k, v in data_dict.items()}


# Dash Cytoscape V0.3.0の場合
# ノード・エッジのデータ辞書に数字があるとエラーになるため、文字列に変換する
node_data = [
    {"data": convert_data_dict(node["data"])} for node in cy_data["elements"]["nodes"]
]
edge_data = [
    {"data": convert_data_dict(edge["data"])} for edge in cy_data["elements"]["edges"]
]

cyto_compo = cyto.Cytoscape(
    id="networkx2cytoscape",
    style={"width": "600px", "height": "400px"},
    layout={"name": "cose"},
    elements=node_data + edge_data,  # 変換後のデータを指定
    stylesheet=[{"selector": "node", "style": {"content": "data(id)"}}],
)

app.layout = html.Div([cyto_compo])

if __name__ == "__main__":
    app.run_server(debug=True)
