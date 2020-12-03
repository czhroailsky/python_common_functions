""" order a sequence of rows in a pandas dataframe """

# x: input dataframe, must be in order already

# example
# tqdm.pandas()
# time_serie.sort_values(by=['year_month'], ascending=True).groupby('id').progress_apply(add_position)

def add_position(x):
    x['position'] = np.arange(1, len(x) + 1)
    return x

""" complete a serie of dates """

# year_month: string of the date, for example '2019-01'
# n: number of months to add to the lower-bound year_month

lower_bound_period = year_month
lower_bound_period = pd.Period(lower_bound_period, 'M')
    
months = []
for i in range(n):
    months.append( str(max_mnt + pd.offsets.MonthEnd( i + 1)) ) # save in string datatype

   
## X is a pandas dataframe with the columns to compute the correlation matrix, with plotly

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

## from categorical to numerical

pd.Categorical(df[ predictor ]).codes
