import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns;sns.set()

def plot_swears(swear_dict):
    data = {'freq': list(swear_dict.values()),'words' : list(swear_dict.keys())}
    df = pd.DataFrame.from_dict(data)
    plot = df.plot(x='words', y='freq', kind='bar')
    fig = plot.get_figure()
    return fig
