# Documentação das Reuniões - Equipe 2(Atas)

Esta seção reúne os registros das reuniões realizadas pela equipe 2 durante a etapa de modelagem do projeto ****Streaming de Vídeo****. As atas têm como objetivo documentar as principais discussões, decisões e atividades realizadas ao longo da construção dos diagramas, contribuindo para a rastreabilidade do processo de modelagem.

****Link para a playlist das gravações:**** [Acessar playlist](https://www.youtube.com/playlist?list=PLJmRMHC-Q6d0)

- [Ata 01 — Alinhamento e planejamento](#ata-de-reunião-01)

- [Ata 02 — Diagrama de Classes](#ata-de-reunião-02)

- [Ata 03 — Diagrama de Componentes](#ata-de-reunião-03)

- [Ata 04 — Diagrama de Atividades](#ata-de-reunião-04)

- [Ata 05 — A definir](#ata-de-reunião-05)

---

## Ata de Reunião 01

****Data:**** 15/09/2026  

****Reunião nº:**** 01  

****Assunto:**** Alinhamento da equipe e planejamento da etapa de modelagem

### 1. Gravação

****Registro da reunião:**** [Acessar vídeo](https://youtu.be/nrQ8Q0Y11N0)

### 2. Participantes

| Membro | Presença |
|---|---|
| Enzo Menali | ✅ |
| Geovanna Umbelino | ✅ |
| Lucas Oliveira | ✅ |
| Paulo Vitor Gomes | ✅ |





### 3. Pauta da Reunião

- Alinhamento inicial da equipe para a etapa de modelagem;

- Discussão sobre os tipos de diagramas que seriam desenvolvidos;

- Pesquisa sobre os diagramas e suas aplicações no projeto;

- Definição inicial da organização do trabalho;

- Análise dos artefatos já produzidos na entrega anterior.

### 4. Tópicos Discutidos

#### 4.1. Alinhamento da Equipe

O grupo iniciou a reunião discutindo os objetivos da etapa de modelagem e como os integrantes poderiam se organizar para realizar as atividades. Foram compartilhadas ideias sobre os artefatos que poderiam contribuir para representar o sistema de forma clara e coerente.

#### 4.2. Escolha dos Diagramas

A equipe discutiu diferentes possibilidades de modelagem e definiu os principais diagramas que seriam desenvolvidos durante a entrega. A escolha considerou o tipo de informação que cada diagrama poderia representar e sua utilidade para compreender diferentes perspectivas do sistema.

Foram definidos, inicialmente:

- ****Diagrama de Classes****, para representar a estrutura estática e os principais elementos do domínio;

- ****Diagrama de Componentes****, para representar a organização estrutural dos principais componentes e suas dependências;

- ****Diagrama de Atividades****, para representar fluxos e comportamentos do sistema;

- Um quarto artefato de modelagem, a ser definido posteriormente pela equipe.

#### 4.3. Pesquisa e Fundamentação

Durante a reunião, os integrantes também realizaram pesquisas para compreender melhor as características e objetivos de cada diagrama. Essa etapa foi utilizada para justificar as escolhas realizadas e garantir que os modelos fossem adequados ao contexto do projeto.

Também foram considerados artefatos produzidos anteriormente, como ****Rich Picture****, ****BPMN**** e ****engenharia reversa****, para apoiar a compreensão do domínio e manter a rastreabilidade entre as diferentes etapas do projeto.

### 5. Decisões

- Desenvolvimento de diferentes diagramas para representar perspectivas complementares do sistema;

- Utilização dos artefatos da entrega anterior como apoio para a modelagem;

- Construção dos diagramas de forma colaborativa durante reuniões da equipe;

- Registro das reuniões para manter a rastreabilidade das decisões.

### 6. Observações

A reunião teve caráter de planejamento e alinhamento, servindo como base para as reuniões seguintes, nas quais cada diagrama seria desenvolvido e documentado.

---

## Ata de Reunião 02

****Data:**** 16/09/2026  

****Reunião nº:**** 02  

****Assunto:**** Elaboração e documentação do Diagrama de Classes

### 1. Gravação

****Registro da reunião:**** [Acessar vídeo](https://youtu.be/S1EAqT-zMeQ)

### 2. Participantes

| Membro | Presença |
|---|---|
| Enzo Menali | ✅ |
| Geovanna Umbelino | ✅ |
| Lucas Oliveira | ✅ |
| Paulo Vitor Gomes | ✅ |

### 3. Pauta da Reunião

- Revisão dos objetivos do Diagrama de Classes;

- Identificação das principais classes do sistema;

- Definição de atributos, operações e relacionamentos;

- Definição de multiplicidades, generalizações e enumerações;

- Elaboração do diagrama;

- Construção da documentação associada.

### 4. Tópicos Discutidos

#### 4.1. Levantamento das Classes

A equipe analisou o domínio da plataforma ****Streaming de Vídeo**** e identificou as principais entidades que deveriam ser representadas no modelo. Entre elas foram discutidas classes relacionadas a usuários, perfis, canais, conteúdos, vídeos, transmissões ao vivo e interações realizadas na plataforma.

Os artefatos produzidos anteriormente, especialmente o ****Rich Picture****, a ****modelagem BPMN**** e a ****engenharia reversa****, foram utilizados como apoio para identificar e validar elementos relevantes do domínio.

#### 4.2. Relacionamentos e Estrutura

Após a definição das classes principais, foram discutidos seus relacionamentos, responsabilidades e multiplicidades. A equipe também analisou a utilização de generalização entre diferentes tipos de conteúdo e o uso de enumerações para representar valores específicos do domínio.

#### 4.3. Elaboração e Documentação

O diagrama foi construído de forma colaborativa e passou por ajustes durante a reunião. Paralelamente, foi iniciada a documentação do modelo, contendo introdução, metodologia, descrição das classes e relacionamentos, justificativa, senso crítico e rastreabilidade.

### 5. Decisões

- Utilização de ****Conteúdo**** como classe abstrata;

- Especialização de ****Conteúdo**** em ****Vídeo**** e ****Transmissão ao Vivo****;

- Separação das responsabilidades de ****Usuário**** e ****Perfil****;

- Representação de inscrições, comentários, reações e moderação como elementos próprios do domínio;

- Uso de enumerações para representar estados, papéis, visibilidade e tipos de reação.

### 6. Resultado da Reunião

Ao final da reunião, foi obtida uma versão consolidada do ****Diagrama de Classes****, acompanhada de sua documentação inicial.

---

## Ata de Reunião 03

****Data:**** 16/09/2026

****Reunião nº:**** 03  

****Assunto:**** Elaboração e documentação do Diagrama de Componentes

### 1. Gravação

****Registro da reunião:**** [Acessar vídeo](https://youtu.be/-wcdkkIxdW4)

### 2. Participantes

| Membro | Presença |

|---|---|

| Enzo Menali | ✅ |

| Geovanna Umbelino | ✅ |

| Lucas Oliveira | ✅ |

| Paulo Vitor Gomes | ✅ |

### 3. Pauta da Reunião

- Revisão dos objetivos do Diagrama de Componentes;

- Identificação dos principais componentes da solução;

- Discussão das responsabilidades de cada componente;

- Definição das dependências e interfaces;

- Elaboração e organização visual do diagrama;

- Documentação das decisões de modelagem.

### 4. Tópicos Discutidos

#### 4.1. Identificação dos Componentes

A equipe discutiu quais partes da solução deveriam ser representadas como componentes, buscando manter o diagrama em um nível de abstração adequado e evitando misturar detalhes excessivos de implementação.

Foram analisadas principalmente as divisões relacionadas à ****interface****, ao ****núcleo da aplicação**** e aos ****recursos compartilhados****, considerando as responsabilidades e dependências existentes entre essas partes.

#### 4.2. Dependências e Interfaces

Os integrantes discutiram como os componentes se comunicam e quais serviços são oferecidos ou requeridos por cada parte do sistema. O objetivo foi representar as dependências de forma clara, mantendo coerência com a arquitetura da plataforma.

#### 4.3. Elaboração e Documentação

O diagrama foi construído e revisado coletivamente, com ajustes na organização visual e na descrição das responsabilidades de cada componente. A documentação foi elaborada em paralelo para registrar as decisões e justificativas adotadas.

### 5. Decisões

- Manter o diagrama focado na visão estrutural dos componentes;

- Evitar representar detalhes de classes ou fluxos internos que pertencem a outros modelos;

- Evidenciar as dependências entre os principais componentes;

- Utilizar a documentação para explicar as decisões que não ficam totalmente explícitas no diagrama.

### 6. Resultado da Reunião

Ao final da reunião, a equipe consolidou uma versão inicial do ****Diagrama de Componentes**** e de sua documentação.

---

## Ata de Reunião 04

****Data:**** 17/09/2026  

****Reunião nº:**** 04  

****Assunto:**** Elaboração e documentação do Diagrama de Atividades

### 1. Gravação

****Registro da reunião:**** [Acessar vídeo](https://www.youtube.com/watch?v=upC7Cf2dITU)

### 2. Participantes

| Membro | Presença |
|---|---|
| Enzo Menali | ✅ |
| Geovanna Umbelino | ✅ |
| Lucas Oliveira | ✅ |
| Paulo Vitor Gomes | ✅ |

### 3. Pauta da Reunião

- Definição do processo a ser representado;

- Identificação das atividades e decisões do fluxo;

- Definição de início, término e possíveis caminhos alternativos;

- Construção do Diagrama de Atividades;

- Revisão do fluxo;

- Elaboração da documentação.

### 4. Tópicos Discutidos

#### 4.1. Definição do Fluxo

A equipe analisou os processos do sistema e definiu qual fluxo seria representado no ****Diagrama de Atividades****. A escolha considerou a relevância do processo para o funcionamento da plataforma e sua capacidade de demonstrar comportamentos e decisões do sistema.

#### 4.2. Atividades e Decisões

Foram identificadas as principais etapas do processo, incluindo pesquisa, aplicação de filtros, seleção do vídeo, carregamento da mídia, reprodução e possíveis interações.

Também foram modelados caminhos alternativos, como erro no carregamento, escolha de outro vídeo e decisões relacionadas à autenticação para registrar determinadas interações.

Como apoio à construção, a equipe utilizou a **modelagem BPMN**, o **Diagrama de Classes** e o **Diagrama de Componentes**, buscando manter coerência entre os processos, os elementos do domínio e a organização da solução.

#### 4.3. Construção e Revisão

O diagrama foi elaborado de forma colaborativa e revisado pela equipe para verificar se o fluxo estava coerente e se as decisões estavam representadas de maneira compreensível.

### 5. Decisões

- Representar apenas as atividades relevantes para o fluxo selecionado;

- Utilizar decisões e caminhos alternativos quando necessários;

- Manter coerência com os processos previamente modelados;

- Evitar inserir detalhes estruturais que pertencem aos diagramas estáticos.

### 6. Resultado da Reunião

A reunião resultou em uma primeira versão do ****Diagrama de Atividades****, posteriormente revisada e documentada pela equipe.

---

## Ata de Reunião 05

**Data:** 17/09/2026  
**Reunião nº:** 05  
**Assunto:** Elaboração e revisão do Diagrama de Sequência

### 1. Gravação

**Registro da reunião:** [Acessar vídeo](https://www.youtube.com/watch?v=EXnYy4yXWaA)

### 2. Participantes

| Membro | Presença |
|---|---|
| Enzo Menali | ✅ |
| Geovanna Umbelino | ✅ |
| Lucas Oliveira | ✅ |
| Paulo Vitor Gomes | ✅ |

### 3. Pauta da Reunião

- Definição do último artefato de modelagem;
- Discussão sobre a finalidade do Diagrama de Sequência;
- Definição do cenário a ser representado;
- Identificação e validação dos participantes arquiteturais;
- Elaboração do Diagrama de Sequência;
- Revisão dos fluxos de sucesso e falha;
- Definição dos fragmentos combinados `alt` e `par`;
- Revisão da documentação;
- Revisão geral da entrega.

### 4. Tópicos Discutidos

Durante a reunião, a equipe definiu que o último artefato de modelagem dinâmica seria o **Diagrama de Sequência**, utilizando como cenário principal **“Carregar e reproduzir um vídeo”**.

Inicialmente, foi discutido o objetivo do modelo e seu nível de abstração. A equipe optou por representar as interações entre responsabilidades arquiteturais, sem transformar o diagrama em uma reprodução direta do código-fonte. Dessa forma, as mensagens foram descritas como abstrações arquiteturais, evitando a criação de métodos, classes ou participantes não confirmados nos artefatos anteriores.

Foram definidos os seguintes participantes:

- Usuário;
- Shell e Roteamento;
- Reprodução e Interações;
- Recursos Compartilhados;
- Servidor/API PeerTube;
- PeerTube Player;
- Entrega de Mídia HLS / P2P.

Também foi reforçado que **Angular SPA** e **PeerTube Frontend** seriam utilizados apenas como agrupamentos visuais, e não como linhas de vida independentes.

A equipe discutiu o fluxo principal desde a seleção do vídeo até o início da reprodução. O fluxo definido contempla:

- seleção do vídeo pelo usuário;
- navegação para a área de reprodução;
- consulta dos dados necessários;
- comunicação com a API do PeerTube;
- preparação da página de reprodução;
- configuração do PeerTube Player;
- obtenção do manifesto HLS;
- solicitação de reprodução;
- obtenção dos recursos iniciais de mídia;
- apresentação da reprodução ao usuário.

Também foram discutidos os diferentes caminhos alternativos do cenário. Um ponto importante foi a diferenciação entre **falha na obtenção dos dados do vídeo** e **falha na obtenção da mídia**.

No primeiro caso, a equipe definiu que uma falha impeditiva na obtenção dos dados deve encerrar aquela ocorrência do cenário, sem permitir que o fluxo alcance o PeerTube Player.

Já no caso de falha na obtenção da mídia, foi mantida a possibilidade de recuperação, permitindo que o Player tente uma fonte alternativa antes de informar a indisponibilidade ao usuário.

Outro ponto revisado foi a relação entre a obtenção do manifesto HLS e a solicitação de reprodução. A equipe optou por utilizar um fragmento `par`, pois não havia evidência suficiente para representar essas duas atividades como uma sequência obrigatória.

Também foram definidos os caminhos de reprodução automática e reprodução manual, utilizando um fragmento `alt` para representar:

- autoplay habilitado e aceito;
- início manual por meio do controle Play.

Por fim, a equipe revisou o diagrama completo, corrigiu os fragmentos combinados e iniciou a documentação do artefato, mantendo a coerência com o Diagrama de Componentes e com os demais modelos já produzidos na entrega.

### 5. Decisões

Durante a reunião, foram tomadas as seguintes decisões:

1. Utilizar o **Diagrama de Sequência** como último artefato de modelagem da subequipe.

2. Modelar o cenário **“Carregar e reproduzir um vídeo”**.

3. Utilizar somente os participantes arquiteturais já consolidados nos artefatos anteriores.

4. Manter **Angular SPA** e **PeerTube Frontend** apenas como agrupamentos visuais.

5. Não representar contratos como `IPlayer`, `IPeerTubeREST` e `IStreamingMedia` como linhas de vida.

6. Não incluir **Serviços Core** no cenário, por não haver interação necessária que justificasse sua participação.

7. Utilizar mensagens em nível arquitetural, sem inventar métodos TypeScript ou detalhes internos de implementação.

8. Representar a falha na obtenção dos dados por meio de um fragmento `alt`, encerrando o fluxo nesse ramo antes da participação do PeerTube Player.

9. Utilizar um fragmento `par` para representar a obtenção do manifesto HLS e a solicitação de reprodução sem impor uma ordem sequencial obrigatória.

10. Representar autoplay e início manual por meio de um fragmento `alt`.

11. Representar a obtenção da mídia por meio de outro fragmento `alt`, separando o caminho de sucesso do caminho de falha.

12. Manter o mecanismo de recuperação/fallback no caminho de falha da mídia.

13. Evitar a inclusão de elementos fora do escopo, como autenticação, comentários, reações, pesquisa, filtros, transmissão ao vivo, codecs e detalhes internos de P2P.

14. Utilizar o Diagrama de Componentes e os demais artefatos anteriores como base para manter a coerência arquitetural.

### 6. Resultado da Reunião

Ao final da reunião, a equipe concluiu a definição e a revisão do **Diagrama de Sequência — Carregar e reproduzir um vídeo**.

O artefato passou a representar:

- o fluxo principal de carregamento e reprodução;
- a obtenção dos dados do vídeo;
- a configuração do PeerTube Player;
- a obtenção do manifesto HLS;
- os caminhos de autoplay e reprodução manual;
- a solicitação e obtenção da mídia;
- o tratamento de falhas na obtenção dos dados;
- o tratamento de falhas na obtenção da mídia;
- o mecanismo de recuperação/fallback;
- o encerramento correto dos fluxos de erro;
- a utilização dos fragmentos `alt` e `par`.

Após a revisão coletiva, o diagrama foi considerado coerente com os demais artefatos arquiteturais produzidos pela equipe e ficou definido como o último artefato de modelagem da Subequipe 02.

---

## Histórico de Versão

| Data | Versão | Descrição | Autor(es) | Revisores|
|---|---|---|---| --- |
| 17/09/2026 | 1.0 | Criação inicial da documentação das reuniões da etapa de modelagem. | [Enzo Menali](https://github.com/menali17), [Geovanna Umbelino](https://github.com/GeovannaUmbelino), [Lucas Oliveira](https://github.com/dev-LucasDpaula) e [Paulo Vitor Gomes](https://github.com/gpaulovit)             |   [Pedro Américo](https://github.com/dev-americo)  |
| 18/09/2026 | 1.1 | Adicionando os links dos vídeos. | [Enzo Menali](https://github.com/menali17), [Geovanna Umbelino](https://github.com/GeovannaUmbelino), [Lucas Oliveira](https://github.com/dev-LucasDpaula) e [Paulo Vitor Gomes](https://github.com/gpaulovit)             |   [Pedro Américo](https://github.com/dev-americo)  |
