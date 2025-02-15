import pandas as pd
from configu.app import App

def GenerateReportVentas(app: App):
    conn = app.bd.getConection()
    query_ventas = "SELECT postal_code, product_id, quantity, sales_amount FROM VENTAS;"
    query_postal = "SELECT code, pais FROM POSTALCODE;"

    df_ventas = pd.read_sql_query(query_ventas, conn)
    df_postal = pd.read_sql_query(query_postal, conn)

    df_merged = df_ventas.merge(df_postal, left_on="postal_code", right_on="code", how="left")

    df_pais_gasto = df_merged.groupby("pais")["sales_amount"].sum().reset_index()

    pais_menor_gasto = df_pais_gasto.nsmallest(1, "sales_amount")

    fecha = "14-02"
    path = f"/workspaces/workspacepy0125v22/proyecto_final/files/data-{fecha}.csv"
    df_pais_gasto.to_csv(path, index=False)

    sendMail(app, path)

    print(f"📉 País con menor gasto: {pais_menor_gasto.iloc[0]['pais']} con ${pais_menor_gasto.iloc[0]['sales_amount']:.2f}.")
    

def sendMail(app, file_path):
    app.mail.send_email('from@example.com', 'Informe de Ventas', 'Adjunto el informe de ventas.', file_path)

