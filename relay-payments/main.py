from collections import defaultdict
from decimal import Decimal
from functools import reduce

import pandas as pd
import numpy as np

from columns import COLUMNS


TRIPS = defaultdict(lambda: Decimal(0))


def main() -> None:
    file = pd.ExcelFile('Week 28 - July 7 — July 13 - Contract.xlsx')
    df   = pd.read_excel(file, sheet_name = 'Payment Details', names = COLUMNS)
    df   = df.replace({ np.nan: None })

    for row in df.itertuples(index = False, name = 'PaymentEntry'):
        TRIPS[row.BlockID or row.TripID or row.LoadID] += Decimal(row.GrossPay or 0)

    # Remove rows where the Summary column contains None (originally NaN) 
    TRIPS.pop(None)

    for trip_id, pay_amount in TRIPS.items():
        print(f'Trip: {trip_id} - ${pay_amount:,.2f}')

    total = reduce(lambda a, b: a + b, TRIPS.values())
    print(f'\tTotal: ${total:,.2f}')


if __name__ == '__main__':
    try:
        main()
    
    except KeyboardInterrupt:
        print('Program was Terminated...')
