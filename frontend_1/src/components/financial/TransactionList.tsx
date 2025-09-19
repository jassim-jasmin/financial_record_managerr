import { useGetRecordsQuery } from '../../store/api/recordsApi'
import { DataGrid, GridColDef } from '@mui/x-data-grid'
import { formatCurrency, formatDate } from '../../utils/formatters'

const columns: GridColDef[] = [
  { field: 'date', headerName: 'Date', width: 150, valueFormatter: (params) => formatDate(new Date(params.value)) },
  { field: 'description', headerName: 'Description', width: 200 },
  { field: 'amount', headerName: 'Amount', width: 120, valueFormatter: (params) => formatCurrency(params.value) },
  { field: 'category', headerName: 'Category', width: 130 }
]

export const TransactionList = () => {
  const { data: records = [], isLoading } = useGetRecordsQuery({})

  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={records}
        columns={columns}
        loading={isLoading}
        pageSizeOptions={[5, 10]}
        checkboxSelection
      />
    </div>
  )
}