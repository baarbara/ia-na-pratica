import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Exemplo simples com dataset local
# dataset_example.csv deve ser uma tabela: Usuario,Produto1,Produto2,Produto3,...

def carregar_dados(caminho="dataset_example.csv"):
    df = pd.read_csv(caminho).set_index("Usuario")
    return df

def calcular_similaridade(df):
    sim = cosine_similarity(df)
    return pd.DataFrame(sim, index=df.index, columns=df.index)

def main():
    df = carregar_dados()
    recom = calcular_similaridade(df)
    print("Matriz de similaridade entre usuários:")
    print(recom)

if __name__ == "__main__":
    main()
