import numpy as np

def evaluate_performance(df, trading_days_per_year=252,name):

    df = pd.DataFrame(
    index = metrics,
    columns = [name])
    
    # Calculate Annualized Return
    annualized_return = df['Portfolio Daily Returns'].mean() * trading_days_per_year
    
    # Calculate Cumulative Return
    cumulative_return = df['Portfolio Cumulative Returns'].iloc[-1]
    
    # Calculate the Annual volatility metric
    annual_volatility = (df['Portfolio Daily Returns'].std() * np.sqrt(252))
    
    # Calculate the Sharpe ratio
    sharpe = (df['Portfolio Daily Returns'].mean() * 252) / (
        df['Portfolio Daily Returns'].std() * np.sqrt(252))
    
    # Calculate the Sortino ratio
    # Start by calculating the downside return values

    # Create a DataFrame that contains the Portfolio Daily Returns column
    sortino_ratio_df = df[['Portfolio Daily Returns']].copy()

    # Create a column to hold downside return values
    sortino_ratio_df.loc[:,'Downside Returns'] = 0

    # Find Portfolio Daily Returns values less than 0, 
    # square those values, and add them to the Downside Returns column
    sortino_ratio_df.loc[sortino_ratio_df['Portfolio Daily Returns'] < 0, 
                             'Downside Returns'] = sortino_ratio_df['Portfolio Daily Returns']**2

    # Calculate the annualized return value
    #annualized_return = sortino_ratio_df['Portfolio Daily Returns'].mean() * 252

    # Calculate the annualized downside standard deviation value
    downside_standard_deviation = np.sqrt(sortino_ratio_df['Downside Returns'].mean()) * np.sqrt(252)

    # Divide the annualized return value by the downside standard deviation value
    sortino_ratio = annualized_return/downside_standard_deviation
  
    
    
    # Assign the values to the corresponding rows in portfolio_evaluation_df
    name.loc['Annualized Return'] = annualized_return
    name.loc['Cumulative Returns'] = cumulative_return
    name.loc['Annual Volatility'] = annual_volatility
    name.loc['Sharpe Ratio'] = sharpe
    name.loc['Sortino Ratio'] = sortino_ratio    
    
    return annualized_return, cumulative_return, annual_volatility, sharpe, sortino_ratio
