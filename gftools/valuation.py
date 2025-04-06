import requests
import pandas as pd
from gftools.financials import GuruStockAnnualTenK


class GuruAnnualMarketValue():

    def __init__(self, **kwargs):
        self.token = kwargs.get('token', 'error')
        self.ticker = kwargs.get('ticker', 'error')
        self.api_data_df = GuruStockAnnualTenK(ticker=self.ticker, token=self.token).api_data_df
        self.api_data_df_nrm = self._normalized()

        return


    def _normalized(self):
        df1 = self.api_data_df
        df2 = pd.DataFrame()

        # Build New Dataframe with Normalized Column names
        if any(df1.columns == 'Fiscal Year'):
            df2['fiscal_year'] = df1['Fiscal Year']

        # Per Share
        if any(df1.columns == 'per_share_data_array.Revenue per Share'):
            df2['pershare_revenue'] = df1['per_share_data_array.Revenue per Share']

        if any(df1.columns == 'per_share_data_array.Earnings per Share (Diluted)'):
            df2['pershare_earnings'] = df1['per_share_data_array.Earnings per Share (Diluted)']

        if any(df1.columns == 'per_share_data_array.Dividends per Share'):
            df2['pershare_dividends'] = df1['per_share_data_array.Dividends per Share']

        if any(df1.columns == 'per_share_data_array.Free Cash Flow per Share'):
            df2['pershare_fcf'] = df1['per_share_data_array.Free Cash Flow per Share']

        if any(df1.columns == 'per_share_data_array.Operating Cash Flow per Share'):
            df2['pershare_cfo'] = df1['per_share_data_array.Operating Cash Flow per Share']

        if any(df1.columns == 'per_share_data_array.FFO per Share'):
            df2['pershare_ffo'] = df1['per_share_data_array.FFO per Share']


        # Valuation
        if any(df1.columns == 'valuation_and_quality.Market Cap'):
            df2['market_cap'] = df1['valuation_and_quality.Market Cap']


        if any(df1.columns == 'valuation_and_quality.Enterprise Value'):
            df2['enterprise_value'] = df1['valuation_and_quality.Enterprise Value']

        if any(df1.columns == 'valuation_and_quality.Highest Stock Price'):
            df2['pershare_high_price'] = df1['valuation_and_quality.Highest Stock Price']

        if any(df1.columns == 'valuation_and_quality.Lowest Stock Price'):
            df2['pershare_low_price'] = df1['valuation_and_quality.Lowest Stock Price']

        if any(df1.columns == 'Shares Outstanding (Basic Average)'):
            df2['shares_out_bop'] = df1['Shares Outstanding (Basic Average)']

        if any(df1.columns == 'valuation_and_quality.Shares Outstanding (EOP)'):
            df2['shares_out_eop'] = df1['valuation_and_quality.Shares Outstanding (EOP)']

        if any(df1.columns == 'valuation_and_quality.Shares Buyback Ratio %'):
            df2['shares_buyback_ratio'] = df1['valuation_and_quality.Shares Buyback Ratio %']

        if any(df1.columns == 'valuation_and_quality.Buyback Yield %'):
            df2['shares_buyback_yield'] = df1['valuation_and_quality.Buyback Yield %']


        # Drop TTM Data
        df2 = df2.loc[df2['fiscal_year'] != 'TTM']

        # Normalize Fiscal Year
        fy_pattern = r"([\d]{4})-"
        month_pattern = r"-([\d]{2})"

        df2['fiscal_year'] = df1['Fiscal Year'].str.extract(fy_pattern)
        df2['fiscal_month'] = df1['Fiscal Year'].str.extract(month_pattern)


        return df2

