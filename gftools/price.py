import requests
import pandas as pd


class GuruPriceHistory:

    def __init__(self, **kwargs):
        self.token = kwargs.get('token', 'error')
        self.ticker = kwargs.get('ticker', 'error')
        self.api_data = self._api_data()
        self.api_data_type = type(self._api_data)
        self.api_data_df = self._api_data_df()
        self.api_data_df_nrm = self._normalized()


    def _api_data(self):
        return requests.get(f'https://api.gurufocus.com/public/user/{str(self.token)}/stock/{str(self.ticker)}/price').json()


    def _api_data_df(self):

        price_list = self.api_data
        price_df = pd.DataFrame(price_list, columns=['date', 'share_price'])
        price_df['date'] = pd.to_datetime(price_df['date'])

        return price_df

    def _normalized(self):

        price_list = self.api_data
        price_df = pd.DataFrame(price_list, columns=['date', 'share_price'])
        price_df['date'] = pd.to_datetime(price_df['date'])

        return price_df