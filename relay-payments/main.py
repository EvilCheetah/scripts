import pandas as pd

columns = [
    'InvoiceNumber',
    'CalendarWeek',
    'ContractID',
    'BlockID',
    'TripID',
    'LoadID',
    'StartDate',
    'EndDate',
    'RunDomicile',
    'OperatorType',
    'Equipment',
    'Distance',
    'ItemType',
    'ProgramType',
    'BaseRate',
    'FuelSurcharge',
    'Tolls',
    'Detention',
    'TONU',
    'Others',
    'GrossPay',
    'Comments',
]


def main():
    file = pd.ExcelFile('Week 28 - July 7 — July 13 - Contract.xlsx')
    df   = pd.read_excel(file, sheet_name = 'Payment Details', names = columns)

    df.columns = columns

    for row in df.itertuples(index = False, name = 'PaymentEntry'):
        print(f'Block: {row.BlockID} - ${row.BaseRate}')


if __name__ == '__main__':
    try:
        main()
    
    except KeyboardInterrupt:
        print('Program was Terminated...')
