from collections import defaultdict
from decimal import Decimal
from functools import reduce
from pathlib import Path
from typing import Literal

import pandas as pd
import numpy as np
from tabulate import tabulate

from columns import COLUMNS


def get_payment_data(
    file_path: str | Path,
    report_type: Literal['Contract', 'Spot']
) -> pd.DataFrame:
    '''
    Returns an Excel spreadsheet as a Pandas DataFrame with the appropriate columns
    '''
    file = pd.ExcelFile(file_path)
    df   = pd.read_excel(file, sheet_name = 'Payment Details', names = COLUMNS[report_type])
    df   = df.replace({ np.nan: None })

    return df


def print_payments(
    file_path: str | Path,
    report_type: Literal['Contract', 'Spot']
) -> None:
    '''
    Prints the payment details and total from a specified payment spreadsheet
    
    Payment spreadsheets can be accessed at the following URL:
    https://relay.amazon.com/financials/settlements/v1?tab=payments
    '''
    print()

    TRIPS = defaultdict(lambda: Decimal(0))
    
    df = get_payment_data(file_path, report_type)

    for row in df.itertuples(index = False, name = 'PaymentEntry'):
        TRIPS[row.BlockID or row.TripID or row.LoadID] += Decimal(row.GrossPay or 0)

    # Remove rows where the Summary column contains None (originally NaN) 
    TRIPS.pop(None)

    print(tabulate(
        tabular_data = [(key, '${:,.2f}'.format(value)) for key, value in TRIPS.items()],
        headers      = ('Trip ID', 'Total Pay'),
        colalign     = ('left', 'right')
    ))

    total = reduce(lambda a, b: a + b, TRIPS.values())
    print(f'\n\tTotal: ${total:,.2f}\n')
