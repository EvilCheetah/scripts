CONTRACT_COLUMNS = [
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


SPOT_COLUMNS = [
    'InvoiceNumber',
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


COLUMNS = {
    'Contract': CONTRACT_COLUMNS,
    'Spot':     SPOT_COLUMNS
}
