def clean_data(df):
    df = df.dropna(subset=['CustomerID'])
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    return df