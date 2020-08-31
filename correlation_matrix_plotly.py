## X is a pandas dataframe with the columns to compute the correlation matrix

import plotly.figure_factory as ff

corrs = X.corr()

fig = ff.create_annotated_heatmap(
    z=corrs.values,
    x=list(corrs.columns),
    y=list(corrs.index),
    annotation_text=corrs.round(2).values,
    showscale=True
)

fig.show()
