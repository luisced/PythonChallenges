import csv

Captura_gasto = {
    "id": 1,
    "name": "Captura_gasto",
    "concept_detail": "Detalle del concepto",
    "capture_date": "2020-01-01",
    "monto": 100,
    "total": 1000,
    "iva": 1,
    "creation_date": "2020-01-01",
    "last_update": "2020-01-01",
    "state": 1,
    "folio": "1sdafsdf",
}


def captura_gasto_to_excel(gastos, csv_path):

    with open(csv_path, mode='w') as captura_gastos_file:
        captura_gastos_writer = csv.writer(
            captura_gastos_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )

    captura_gastos_writer.writerow(
        ['id', 'name', 'concept_detail', 'capture_date', 'monto', 'total', 'iva', 'creation_date', 'last_update', 'state', 'folio', 'Gastos', 'Honorarios', 'Empresas', 'Impuestos', 'Despachos', 'Deudor', 'Documentos'])

    for gasto in gastos:
        captura_gastos_writer.writerow([
            gasto.id,
            gasto.name,
            gasto.concept_detail,
            gasto.capture_date,
            gasto.monto,
            gasto.total,
            gasto.iva,
            gasto.creation_date,
            gasto.last_update,
            gasto.state,
            gasto.folio,
            gasto.Gastos,
            gasto.Honorarios,
            gasto.Empresas,
            gasto.Impuestos,
            gasto.Despachos,
            gasto.Deudor,
            gasto.Documentos

        ])


captura_gasto_to_excel(Captura_gasto, "captura_gasto.csv")
