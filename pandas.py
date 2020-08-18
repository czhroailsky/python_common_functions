""" order a sequence of rows in a pandas dataframe """

# x: input dataframe, must be in order already

# example
# tqdm.pandas()
# time_serie.sort_values(by=['year_month'], ascending=True).groupby('id').progress_apply(add_position)

def add_position(x):
    x['position'] = np.arange(1, len(x) + 1)
    return x
