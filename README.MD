# Como rodar o desafio

Clonar esse repositório e vá para o diretório. \
` git clone git@github.com:ilitotor/desafio-nasa.git `

Copie os datasets para mesma pasta do projeto:\
https://ilito-semantix-test.s3-us-west-2.amazonaws.com/NASA_access_log_Aug95

https://ilito-semantix-test.s3-us-west-2.amazonaws.com/NASA_access_log_Jul95

**Opção 1** \
Caso já tenha o spark e a biblioteca pyspark instalada:
Apenas execute o arquivo `app.py`. \
ex: `python app.py`

**Opção 2** \
Caso não tenha, sugiro executar o código dentro de um Docker container:
1. build project container: \
`docker build -t pyspark --no-cache .`

2. Run:\
`docker run -it --rm pyspark`

3. To access the responses via terminal:\
Run:\
`docker ps`
Get the _Container ID_ then run:\
`docker exec -ti <container id> bash`

5. Then run:\
`python app.py`

## Perguntas e Respostas 
**Qual o objetivo do comando _cache_ em Spark?** 
Alterar o nível de armazenamento para _cache_ ajuda a tornar mais eficiente um código em cenários com muitas iterações, 
como por exemplo a leitura de um arquivo. Existem os níveis que podem tornar mais eficiente o uso da memória e CPU.

**O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce.
Por quê?** 
Porque o Spark executa operações utilizando cache em memória dos dados e não escrita em disco, como Mapreduce.  
**Qual é a função do SparkContext?**
Servir como portão de entrada das funcionalidades do Spark. É nele que são setadas as configurações de memória e processadores que serão utilizadas.

**Explique com suas palavras o que é Resilient Distributed Datasets (RDD).**
É a abstração de dados do Spark. Eles são imutáveis (readonly), para muda-los é necessário a criação de num novo RDD.
São lazy, portanto só são ativados quando há alguma ação. É uma coleção distribuída de elementos de chave e valor, 
como um dictionary em python, que é lida pelo Spark.

**GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?**
GroupByKey agroupa o resultado e, por não fazer o calculo de resultados parcais, pode transferir uma grande quantidade de dados, podem causar problemas de disco, memória ou network.
O reduceByKey combina dados de cada partição de uma combinação de consultas, trazendo os dados já filtrados.

**Explique o que o código Scala abaixo faz.**
```
1 val textFile = sc.textFile("hdfs://...")
2 val counts = textFile.flatMap(line => line.split(" "))
3 .map(word => (word, 1))
4 .reduceByKey(_ + _)
5 counts.saveAsTextFile("hdfs://...")
```

`linha 1` O código lê um arquivo texto do tipo hdfs e salva em uma variável _textFile_ \
`linha 2` Cria uma variável _count_ e quebra o arquivo em linhas \
`linha 3` Cria um mapa(key, value) com as palavras \
`linha 4` Agrega as chaves atraves da operação de soma \
`linha 5` Salva o resultado em outro arquivo texto do tipo hdfs


