import json
import pandas as pd
import plotly
import plotly.express as px


def compare_crops_height(crop_1, crop_2, tray_position, treatment):
    df = pd.read_csv("/Users/mohammedsohilshaikh/Desktop/Venturit/Photosynq/Data/Plantye.csv")
    df['Crop'] = df['Crop '].str.strip()
    df['Tray_position'] = df['Tray_position '].str.strip()
    df['Treatment'] = df['Treatment '].str.strip()

    df_temp = df.loc[(df['Crop'].isin([crop_1, crop_2])) & (df['Tray_position'] == tray_position) & (
            df['Treatment'] == treatment)]

    fig = px.line(df_temp, x="day ", y="height__avg   ", facet_col="Crop",
                  width=1000, height=400)

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
    )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


def compare_crops_area(crop_1, crop_2, tray_position, treatment):
    df = pd.read_csv("/Users/mohammedsohilshaikh/Desktop/Venturit/Photosynq/Data/Plantye.csv")
    df['Crop'] = df['Crop '].str.strip()
    df['Tray_position'] = df['Tray_position '].str.strip()
    df['Treatment'] = df['Treatment '].str.strip()

    df_temp = df.loc[(df['Crop'].isin([crop_1, crop_2])) & (df['Tray_position'] == tray_position) & (
            df['Treatment'] == treatment)]

    fig = px.scatter(df_temp, x="day ", y="area_3d__avg   ", facet_col="Crop",
                     width=1000, height=400)

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
    )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


def compare_crops_greennes(crop_1, crop_2, tray_position, treatment):
    df = pd.read_csv("/Users/mohammedsohilshaikh/Desktop/Venturit/Photosynq/Data/Plantye.csv")
    df['Crop'] = df['Crop '].str.strip()
    df['Tray_position'] = df['Tray_position '].str.strip()
    df['Treatment'] = df['Treatment '].str.strip()

    df_temp = df.loc[(df['Crop'].isin([crop_1, crop_2])) & (df['Tray_position'] == tray_position) & (
            df['Treatment'] == treatment)]

    fig = px.bar(df_temp, x="day ", y="greenness_aver__avg ", facet_col="Crop",
                 width=1000, height=400)

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
    )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


def compare_tray_positions_height(tray_position_1, tray_position_2, treatment_ctp, crop_ctp):
    df = pd.read_csv("/Users/mohammedsohilshaikh/Desktop/Venturit/Photosynq/Data/Plantye.csv")
    df['Crop'] = df['Crop '].str.strip()
    df['Tray_position'] = df['Tray_position '].str.strip()
    df['Treatment'] = df['Treatment '].str.strip()
    print(tray_position_1, tray_position_2, treatment_ctp, crop_ctp)
    df_temp = df.loc[(df['Tray_position'].isin([tray_position_1, tray_position_2])) & (df['Crop'] == crop_ctp) & (
            df['Treatment'] == treatment_ctp)]

    print(df_temp['Tray_position'].unique())

    fig = px.line(df_temp, x="day ", y="height__avg   ", facet_col="Tray_position",
                  width=1000, height=400)

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
    )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


def compare_tray_positions_area(tray_position_1, tray_position_2, treatment_ctp, crop_ctp):
    df = pd.read_csv("/Users/mohammedsohilshaikh/Desktop/Venturit/Photosynq/Data/Plantye.csv")
    df['Crop'] = df['Crop '].str.strip()
    df['Tray_position'] = df['Tray_position '].str.strip()
    df['Treatment'] = df['Treatment '].str.strip()
    print(tray_position_1, tray_position_2, treatment_ctp, crop_ctp)
    df_temp = df.loc[(df['Tray_position'].isin([tray_position_1, tray_position_2])) & (df['Crop'] == crop_ctp) & (
            df['Treatment'] == treatment_ctp)]

    print(df_temp['Tray_position'].unique())

    fig = px.scatter(df_temp, x="day ", y="area_3d__avg   ", facet_col="Tray_position",
                     width=1000, height=400)

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
    )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


def compare_tray_positions_greennes(tray_position_1, tray_position_2, treatment_ctp, crop_ctp):
    df = pd.read_csv("/Users/mohammedsohilshaikh/Desktop/Venturit/Photosynq/Data/Plantye.csv")
    df['Crop'] = df['Crop '].str.strip()
    df['Tray_position'] = df['Tray_position '].str.strip()
    df['Treatment'] = df['Treatment '].str.strip()
    print(tray_position_1, tray_position_2, treatment_ctp, crop_ctp)
    df_temp = df.loc[(df['Tray_position'].isin([tray_position_1, tray_position_2])) & (df['Crop'] == crop_ctp) & (
            df['Treatment'] == treatment_ctp)]

    print(df_temp['Tray_position'].unique())

    fig = px.bar(df_temp, x="day ", y="greenness_aver__avg ", facet_col="Tray_position",
                 width=1000, height=400)

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
    )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


def compare_treatments_height(treatment_1, treatment_2, tray_position_ct, crop_ct):
    df = pd.read_csv("/Users/mohammedsohilshaikh/Desktop/Venturit/Photosynq/Data/Plantye.csv")
    df['Crop'] = df['Crop '].str.strip()
    df['Tray_position'] = df['Tray_position '].str.strip()
    df['Treatment'] = df['Treatment '].str.strip()

    df_temp = df.loc[(df['Treatment'].isin([treatment_1, treatment_2])) & (df['Crop'] == crop_ct) & (
            df['Tray_position'] == tray_position_ct)]

    fig = px.line(df_temp, x="day ", y="height__avg   ", facet_col="Treatment",
                  width=1000, height=400)

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
    )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


def compare_treatments_area(treatment_1, treatment_2, tray_position_ct, crop_ct):
    df = pd.read_csv("/Users/mohammedsohilshaikh/Desktop/Venturit/Photosynq/Data/Plantye.csv")
    df['Crop'] = df['Crop '].str.strip()
    df['Tray_position'] = df['Tray_position '].str.strip()
    df['Treatment'] = df['Treatment '].str.strip()

    df_temp = df.loc[(df['Treatment'].isin([treatment_1, treatment_2])) & (df['Crop'] == crop_ct) & (
            df['Tray_position'] == tray_position_ct)]

    fig = px.scatter(df_temp, x="day ", y="area_3d__avg   ", facet_col="Treatment",
                     width=1000, height=400)

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
    )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


def compare_treatments_greennes(treatment_1, treatment_2, tray_position_ct, crop_ct):
    df = pd.read_csv("/Users/mohammedsohilshaikh/Desktop/Venturit/Photosynq/Data/Plantye.csv")
    df['Crop'] = df['Crop '].str.strip()
    df['Tray_position'] = df['Tray_position '].str.strip()
    df['Treatment'] = df['Treatment '].str.strip()

    df_temp = df.loc[(df['Treatment'].isin([treatment_1, treatment_2])) & (df['Crop'] == crop_ct) & (
            df['Tray_position'] == tray_position_ct)]

    fig = px.bar(df_temp, x="day ", y="greenness_aver__avg ", facet_col="Treatment",
                 width=1000, height=400)

    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="LightSteelBlue",
    )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


def heightChart(crop='Lt63', tray_position='A7', treatment='Control'):
    # df = pd.DataFrame(px.data.gapminder())
    # if mode == 'Before':
    #     df_temp = df.loc[(df['country'] == country) & (df['year'] < 1980)]
    # elif mode == 'After':
    #     df_temp = df.loc[(df['country'] == country) & (df['year'] > 1980)]
    # else:
    #     df_temp = df.loc[(df['country'] == country)]

    df = pd.read_csv("/Users/mohammedsohilshaikh/Desktop/Venturit/Photosynq/Data/Plantye.csv")
    df['Crop '] = df['Crop '].str.strip()
    df['Tray_position '] = df['Tray_position '].str.strip()
    df['Treatment '] = df['Treatment '].str.strip()

    if treatment == 'all':
        df_temp = df.loc[(df['Crop '] == crop) & (df['Tray_position '] == tray_position)]
        fig = px.line(df_temp, x="day ", y='height__avg   ', color='Treatment ', width=1000, height=500,
                      title='Height Growth Over Time')
    else:
        df_temp = df.loc[
            (df['Crop '] == crop) & (df['Tray_position '] == tray_position) & (df['Treatment '] == treatment)]
        fig = px.line(df_temp, x="day ", y='height__avg   ', width=1000, height=500, title='Height Growth Over Time')
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


def areaChart(crop='Lt63', tray_position='A7', treatment='Control'):
    # df = pd.DataFrame(px.data.gapminder())
    # if mode == 'Before':
    #     df_temp = df.loc[(df['country'] == country) & (df['year'] < 1980)]
    # elif mode == 'After':
    #     df_temp = df.loc[(df['country'] == country) & (df['year'] > 1980)]
    # else:
    #     df_temp = df.loc[(df['country'] == country)]

    df = pd.read_csv("/Users/mohammedsohilshaikh/Desktop/Venturit/Photosynq/Data/Plantye.csv")
    df['Crop '] = df['Crop '].str.strip()
    df['Tray_position '] = df['Tray_position '].str.strip()
    df['Treatment '] = df['Treatment '].str.strip()

    if treatment == 'all':
        df_temp = df.loc[(df['Crop '] == crop) & (df['Tray_position '] == tray_position)]
        fig = px.scatter(df_temp, x="day ", y='area_3d__avg   ', color='Treatment ', width=1000, height=500,
                         title='Area Growth Over Time')
    else:
        df_temp = df.loc[
            (df['Crop '] == crop) & (df['Tray_position '] == tray_position) & (df['Treatment '] == treatment)]
        fig = px.scatter(df_temp, x="day ", y='area_3d__avg   ', width=1000, height=500, title='Area Growth Over Time')
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json


def barChart(variety='Italian Basil'):
    df = pd.read_csv("/Users/mohammedsohilshaikh/Desktop/Venturit/Photosynq/Data/Metabolites.csv")
    df['Variety'] = df['Variety'].str.strip()

    df_temp = df.loc[(df['Variety'] == variety) & (df['Rep'] == 1)]
    fig = px.bar(df_temp, x="Treatment ", y='Vitamin C mg.100g FW-1', width=1000, height=500,
                 title='Height Growth Over Time')
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json