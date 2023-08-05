from .read_historical_excel import ReadHistoricalExcel


class Preprocess:
    @staticmethod
    def execute():
        ReadHistoricalExcel().execute()
