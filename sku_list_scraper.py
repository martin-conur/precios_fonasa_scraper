import subprocess, json
import pandas as pd

sp = subprocess.run(
    [
        'curl',
        '--request', 'POST', 'https://medicamentos.fonasa.cl/buscador-farmacias/buscarMedicamentos',
        '--header', 'Content-Type: application/json',
        '--data-raw', '{"tipoBusqueda":"1","texto":"","latitud":-33.4843354,"longitud":-70.6216794,"distancia":100000}'
    ],
    capture_output=True
)

output = json.loads(sp.stdout.decode())

pd.DataFrame(output["listadoMedicamentos"]).to_csv("outputs/skus.csv", index=False)