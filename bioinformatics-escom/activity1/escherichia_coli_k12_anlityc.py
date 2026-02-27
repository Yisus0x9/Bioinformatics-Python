### Cargar librerias
import sys
import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from collections import Counter

## RUTA AL DATASET Y DECLARACIÓN DE AMINOACIDOS POR SUS CARACTERISTICAS
FASTA_PATH = "bioinformatics-escom/datasets/proteins_ecoli_k12.fasta"
script_dir = f'{os.path.dirname(os.path.abspath(__file__))}/output'
positive_charge = set("KRH")
negative_charge = set("DE")
polar = set("STNQC")
non_polar = set("AVLIMFWPG")
aromatic = set("FWY")

## Función para cargar el conjunto de datos, muestra algunos de los datos y retorna los datos
def load_dataset(path):
    records = list(SeqIO.parse(path, "fasta"))
    print("Número de proteínas encontradas:", len(records))
    print("Mostrando algunas caracteristicas de los datos:")
    for r in records[:5]:
        print(r.id, "longitud", len(r.seq))
    return records

## Limpia una secuencia
def clean_sequence(seq):
    seq = seq.replace("*", "").replace("X", "")
    return re.sub(r"[^ACDEFGHIKLMNPQRSTVWY]", "", seq)

## Analisa una lista de secuencias de proteinas
## Investigar que es GRAVY
def analyze_proteins(records):
    rows = []
    for r in records:
        seq = clean_sequence(str(r.seq))
        if len(seq) == 0:
            continue

        pa = ProteinAnalysis(seq)
        aa_count = pa.count_amino_acids()
        row = {
            "id": r.id,
            "length": len(seq),
            "molecular_weight": pa.molecular_weight(),
            "isoelectric_point": pa.isoelectric_point(),
            "gravy": pa.gravy(),
            "cysteines": aa_count.get("C", 0),
            "perc_positive_charge": 100 * sum(aa_count.get(a, 0) for a in positive_charge) / len(seq),
            "perc_negative_charge": 100 * sum(aa_count.get(a, 0) for a in negative_charge) / len(seq),
            "perc_polar": 100 * sum(aa_count.get(a, 0) for a in polar) / len(seq),
            "perc_non_polar": 100 * sum(aa_count.get(a, 0) for a in non_polar) / len(seq),
            "perc_aromatic": 100 * sum(aa_count.get(a, 0) for a in aromatic) / len(seq),
        }
        rows.append(row)
    return rows

## Simula la digestión de la tripsina
## Investigar que es un peptido, tripsina y funcionamiento
def trypsin_digest(seq, min_len=3):
    peptides = []
    start = 0
    for i, aa in enumerate(seq):
        if aa in ("K", "R"):
            if i + 1 < len(seq) and seq[i + 1] == "P":
                continue
            pep = seq[start:i + 1]
            if len(pep) >= min_len:
                peptides.append(pep)
            start = i + 1
    last = seq[start:]
    if len(last) >= min_len:
        peptides.append(last)
    return peptides

def get_peptides(records):
    peptide_rows = []
    for r in records:
        seq = clean_sequence(str(r.seq))
        peptides = trypsin_digest(seq)
        for p in peptides:
            peptide_rows.append({
                "id": r.id,
                "peptide": p,
                "length": len(p)
            })
    return peptide_rows

## Crea un dataframe usando pandas, lo guarda en una ruta indicada y retorna el dataframe
def create_and_save_dataframe(rows, path="features.csv"):
    features = pd.DataFrame(rows)
    features.to_csv(f'{script_dir}/{path}', index=False)
    print("Archivo guardado exitosamente")
    return features

## Crea un histograma
def plot(dataframe, attr, xlabel, ylabel, title, bins=10, alpha=0.4):
    plt.figure()
    plt.hist(dataframe[attr], bins=bins, alpha=alpha)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(f'{script_dir}/{title}.jpg')
    plt.show()

records = load_dataset(FASTA_PATH)
rows = analyze_proteins(records)
dataframe = create_and_save_dataframe(rows)
plot(dataframe, "length", "Longitud (aa)","Frecuencia","Histograma de longitudes de las proteinas de E. coli")
plot(dataframe, "isoelectric_point", "pI","Frecuencia","Histograma del punto isoeléctrico")
plot(dataframe, "gravy","GRAVY","Frecuencia","Histograma de hidrofobicidad")
peptide_rows = get_peptides(records)
peptide_dataframe = create_and_save_dataframe(peptide_rows, "peptides.csv")
plot(peptide_dataframe, "length", "Longitud del péptido (aa)","Frecuencia","Histograma de longitud de péptidos")
peptides_per_protein = peptide_dataframe.groupby("id").size().reset_index(name="num_peptides")
data = dataframe.merge(peptides_per_protein, on="id")
print(data[["id", "length", "num_peptides"]].head())
plot(peptides_per_protein, "num_peptides", "Número de peptidos por proteina","Frecuencia","Distribución del número de peptidos por proteina")