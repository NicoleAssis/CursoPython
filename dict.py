contatos = {
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "3333-2221"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome":"Gui"}

contatos["guilherme@gmail.com"] # {"nome": "Guilherme", "telefone"}
copia["guilherme@gmail.com"] # {"nome": "Gui"}

#values, count, index, del, pop, remove
dict.fromkeys(["nome","telefone"])
contatos.get("chave")
contatos.setdefault("idade",2)