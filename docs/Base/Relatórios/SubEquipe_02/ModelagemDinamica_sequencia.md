# Diagrama de Sequência 

## 1. Introdução

O **Diagrama de Sequência** é um artefato de modelagem dinâmica utilizado para representar como diferentes participantes interagem ao longo de um cenário, destacando a ordem das mensagens trocadas entre eles. Nesse tipo de diagrama, cada participante é representado por uma linha de vida (*lifeline*), permitindo acompanhar como a execução evolui ao longo do tempo.

No projeto **Streaming de Vídeo**, o Diagrama de Sequência foi utilizado para detalhar o cenário **“Carregar e reproduzir um vídeo”**, concentrando-se no momento em que o usuário seleciona um conteúdo e a aplicação precisa recuperar os dados necessários, preparar a área de reprodução, configurar o player e obter a mídia.

O recorte foi mantido propositalmente específico. Elementos como pesquisa, filtros, autenticação, comentários, reações, inscrições e transmissão ao vivo não fazem parte deste diagrama, pois já são tratados em outros fluxos ou não são necessários para compreender o comportamento desta interação.

A construção do modelo buscou manter coerência com os artefatos anteriores do projeto. O [**modelagem BPMN**](https://unbarqdsw2026-2-turma02.github.io/2026.2_T02_G3_ProjetoStreamingVideo_Entrega_01/#/Base/Relat%C3%B3rios/1.2.SubEquipe_02/modelagem_bpmn) ajudou a identificar o fluxo de carregamento e reprodução; a [**engenharia reversa**](https://unbarqdsw2026-2-turma02.github.io/2026.2_T02_G3_ProjetoStreamingVideo_Entrega_01/#/Base/Relat%C3%B3rios/1.2.SubEquipe_02/Engenharia_reversa) forneceu evidências sobre a estrutura do frontend, o player e os mecanismos de recuperação de mídia; o [**Diagrama de Classes**](Base/Relatórios/SubEquipe_02/1.ModelagemEstatica.md) contribuiu com a compreensão das responsabilidades do domínio; e o [**Diagrama de Componentes**](Base/Relatórios/SubEquipe_02/ModelagemEstatica_componentes.md)  serviu como principal referência para definir os participantes arquiteturais utilizados no cenário.


## 2. Metodologia

A elaboração do Diagrama de Sequência partiu da definição de um cenário específico: **carregar e iniciar a reprodução de um vídeo já selecionado pelo usuário**.

A equipe evitou transformar o diagrama em uma reprodução literal do código. Por isso, as mensagens foram escritas como **abstrações arquiteturais**, representando responsabilidades e interações relevantes sem inventar métodos TypeScript ou detalhes internos que não foram confirmados durante a análise.

O processo de construção seguiu quatro decisões principais:

1. definir os participantes a partir da arquitetura já consolidada no Diagrama de Componentes;
2. limitar o cenário ao carregamento e reprodução do vídeo;
3. representar explicitamente os caminhos alternativos de falha;
4. diferenciar atividades sequenciais de comportamentos que podem ocorrer sem uma ordem obrigatória.

Os participantes utilizados foram mantidos exatamente como definidos na arquitetura:

- **Usuário**;
- **Shell e Roteamento**;
- **Reprodução e Interações**;
- **Recursos Compartilhados**;
- **Servidor/API PeerTube**;
- **PeerTube Player**;
- **Entrega de Mídia HLS / P2P**.

Os elementos **Angular SPA** e **PeerTube Frontend** aparecem apenas como agrupamentos visuais. Eles organizam os participantes no diagrama, mas não representam linhas de vida independentes.

Da mesma forma, **IPlayer**, **IPeerTubeREST** e **IStreamingMedia** são tratados como contratos arquiteturais e, por isso, não foram transformados em participantes do Diagrama de Sequência.



## 3. Diagrama de Sequência

O diagrama abaixo apresenta o cenário **“Carregar e reproduzir um vídeo”**.


![Diagrama de Sequência — Carregar e reproduzir um vídeo](../../../assets/WhatsApp%20Image%202026-09-17%20at%2021.48.14.jpeg)



## 4. Cenário Modelado

O fluxo começa depois que o usuário já decidiu qual vídeo deseja assistir. A partir desse ponto, o diagrama detalha como a aplicação organiza a navegação, consulta os dados do conteúdo, configura o player e solicita os recursos necessários para iniciar a reprodução.

### 4.1. Entrada no cenário

O **Usuário** seleciona o vídeo e navega para a área de reprodução.

O **Shell e Roteamento** recebe essa ação e ativa a área de **Reprodução e Interações**, encaminhando o identificador do vídeo necessário para continuar o processo.

A responsabilidade de **Shell e Roteamento** permanece restrita à organização da navegação. Ele não consulta os dados do vídeo nem controla diretamente a reprodução.

### 4.2. Obtenção dos dados do vídeo

Após receber o identificador, **Reprodução e Interações** solicita aos **Recursos Compartilhados** os dados necessários para preparar a página.

Os **Recursos Compartilhados** fazem a comunicação com o **Servidor/API PeerTube**, solicitando os detalhes e recursos complementares necessários.

Nesse ponto, o modelo utiliza um fragmento `alt`, pois existem dois resultados relevantes.

No caminho de sucesso:

- o **Servidor/API PeerTube** retorna os dados;
- os **Recursos Compartilhados** entregam os resultados para **Reprodução e Interações**;
- a página e as opções de reprodução são preparadas;
- o **PeerTube Player** é configurado.

No caminho de falha:

- os **Recursos Compartilhados** propagam a falha;
- **Reprodução e Interações** apresenta ao usuário uma mensagem de erro ou indisponibilidade;
- essa ocorrência do cenário é encerrada.

Essa separação é importante porque uma falha impeditiva na obtenção dos dados não deve continuar para as etapas de player ou mídia.

### 4.3. Configuração do Player

Quando os dados necessários estão disponíveis, **Reprodução e Interações** prepara a página e envia ao **PeerTube Player** as informações necessárias para carregar o vídeo.

A mensagem indica o uso do contrato **IPlayer**, mas esse contrato não é representado como uma linha de vida. Ele apenas identifica a interface arquitetural envolvida na comunicação.

A configuração do player não significa que a mídia já esteja pronta para reprodução. Por esse motivo, o diagrama separa a configuração do player da obtenção efetiva dos recursos de mídia.



## 5. Concorrência entre Manifesto e Solicitação de Reprodução

Após o carregamento do vídeo no **PeerTube Player**, o diagrama utiliza um fragmento `par`.

Esse fragmento representa duas atividades que não precisam ser interpretadas como uma sequência rígida:

- **obtenção do manifesto HLS**;
- **solicitação de reprodução**.

### 5.1. Obtenção do manifesto

O **PeerTube Player** solicita o manifesto HLS à **Entrega de Mídia HLS / P2P**, que retorna o manifesto necessário para orientar a obtenção da mídia.

### 5.2. Solicitação de reprodução

Paralelamente, a solicitação de reprodução pode seguir dois caminhos.

No caso de **autoplay habilitado e aceito**, o próprio **PeerTube Player** inicia a solicitação de reprodução automática.

Quando é necessário início manual:

- o **PeerTube Player** disponibiliza o controle **Play**;
- o **Usuário** aciona o controle.

O uso do fragmento `par` evita afirmar que o manifesto obrigatoriamente precisa ser totalmente retornado antes que a intenção de reprodução seja tratada.


## 6. Obtenção e Reprodução da Mídia

Depois do fragmento paralelo, o **PeerTube Player** solicita os recursos iniciais de mídia à **Entrega de Mídia HLS / P2P**.

Novamente, o modelo utiliza um fragmento `alt`.

### 6.1. Mídia obtida com sucesso

Quando os dados de mídia são obtidos corretamente:

- a **Entrega de Mídia HLS / P2P** retorna os dados necessários;
- o **PeerTube Player** apresenta ao usuário a reprodução iniciada.

### 6.2. Falha de mídia

Quando a mídia não pode ser obtida normalmente, o **PeerTube Player** tenta uma recuperação ou um *fallback* de reprodução.

Esse trecho foi mantido em nível arquitetural, sem representar algoritmos internos de HLS, P2P ou detalhes específicos de implementação.

Dentro desse caminho existe um segundo fragmento `alt`.

Se uma **fonte alternativa estiver disponível**:

- o Player solicita a fonte alternativa;
- a entrega de mídia retorna o recurso;
- a reprodução é apresentada ao usuário.

Se **nenhuma fonte puder ser utilizada**:

- o usuário recebe a indicação de que a reprodução está indisponível ou ocorreu um erro.


## 7. Fragmentos Combinados Utilizados

O Diagrama de Sequência utiliza fragmentos combinados para representar situações em que o fluxo não é simplesmente linear.

| Fragmento | Uso no modelo |
|---|---|
| `alt` | Representa caminhos alternativos e mutuamente exclusivos. |
| `par` | Representa comportamentos que podem ocorrer sem uma ordem sequencial obrigatória entre si. |

Os principais fragmentos `alt` representam:

- dados necessários disponíveis × falha impeditiva;
- autoplay × reprodução manual;
- mídia obtida com sucesso × falha de mídia;
- fonte alternativa disponível × nenhuma fonte utilizável.

O fragmento `par` foi utilizado para representar a **obtenção do manifesto** e a **solicitação de reprodução** sem impor uma sequência não sustentada entre essas duas atividades.

## 8. Decisões de Modelagem

Algumas decisões foram adotadas para manter o diagrama coerente com os demais artefatos e evitar excesso de complexidade.

### 8.1. Participantes arquiteturais

Foram utilizadas responsabilidades arquiteturais já consolidadas no Diagrama de Componentes, em vez de classes concretas ou arquivos do código.

Isso mantém o Diagrama de Sequência em um nível compatível com a arquitetura documentada.

### 8.2. Contratos não são participantes

As interfaces **IPlayer**, **IPeerTubeREST** e **IStreamingMedia** representam contratos entre componentes. Como não possuem responsabilidade independente no cenário, não foram modeladas como lifelines.

### 8.3. Serviços Core fora do recorte

Os **Serviços Core** não participam deste cenário porque não foi identificada uma interação necessária que justificasse sua presença no fluxo modelado.

Adicionar esse participante apenas para reproduzir todos os elementos do Diagrama de Componentes deixaria o modelo mais complexo sem acrescentar informação ao cenário.

### 8.4. Mensagens abstratas

Mensagens como “consultar dados necessários”, “solicitar detalhes” e “carregar vídeo com opções” não representam assinaturas reais de métodos.

Elas descrevem responsabilidades arquiteturais e permitem que o modelo permaneça válido mesmo sem assumir detalhes de implementação não comprovados.


## 9. Justificativa e Senso Crítico do Modelo

### 9.1. Por que utilizar o Diagrama de Sequência

O Diagrama de Sequência foi escolhido porque o cenário precisava mostrar **como diferentes partes da arquitetura colaboram ao longo do tempo**.

Enquanto o Diagrama de Componentes mostra quais elementos existem e quais dependências possuem, o Diagrama de Sequência permite observar como esses elementos participam de uma ocorrência concreta do sistema.

No caso de “Carregar e reproduzir um vídeo”, essa perspectiva é importante porque o comportamento envolve:

- navegação;
- recuperação de dados;
- configuração do player;
- solicitação de reprodução;
- obtenção de mídia;
- tratamento de falhas;
- tentativa de recuperação.

### 9.2. Pontos fortes

Um ponto forte do modelo é a separação entre **falhas de dados** e **falhas de mídia**.

Uma falha na obtenção dos dados impede a continuação do cenário antes mesmo de o player participar. Já uma falha de mídia ocorre depois que o player foi configurado e pode permitir tentativa de recuperação.

Essa diferença deixa o comportamento mais preciso.

Outro ponto importante é o uso do fragmento `par`, que evita impor uma ordem rígida entre a obtenção do manifesto e a solicitação de reprodução.

O modelo também mantém separadas as responsabilidades do frontend, do player, da API e da infraestrutura de entrega de mídia, tornando mais fácil relacionar o comportamento com o Diagrama de Componentes.

### 9.3. Limitações

O diagrama não pretende representar todas as chamadas internas realizadas durante a reprodução.

Foram omitidos intencionalmente:

- algoritmos P2P;
- detalhes internos de HLS;
- codecs;
- detalhes de RxJS;
- métodos concretos do frontend;
- lógica interna do backend;
- detalhes de implantação.

Também não é possível concluir, apenas pelo diagrama, como cada mecanismo de recuperação é implementado.

A representação mostra o **comportamento arquitetural relevante para o cenário**, e não uma rastreabilidade linha a linha do código.


## 10. Participações e Trabalho em Equipe

### 10.1. Processo de Construção

A elaboração do Diagrama de Sequência ocorreu de forma colaborativa.

A equipe começou definindo qual parte do fluxo de consumo de vídeo deveria ser detalhada. A partir dos artefatos anteriores, foram consolidados os participantes e discutidas as mensagens necessárias para representar o carregamento e a reprodução sem adicionar elementos que não estavam sustentados pela arquitetura.

Durante a revisão, a equipe também analisou os caminhos de erro e percebeu a necessidade de diferenciar:

- falha na obtenção dos dados;
- falha na obtenção da mídia;
- tentativa de recuperação com fonte alternativa.

Outro refinamento importante foi a utilização do fragmento `par` para evitar representar a obtenção do manifesto e a solicitação de reprodução como etapas obrigatoriamente sequenciais.

### 10.2. Registro da Reunião

A reunião utilizada para elaboração e revisão do Diagrama de Sequência foi gravada como forma de registrar o processo e manter a rastreabilidade das decisões tomadas pela equipe.

**Registro da reunião:** [Acessar vídeo da reunião](./Atas/Atas_subequipe_2.md)

### 10.3. Quadro de Participações

| Integrante | Participação |
|---|---|
| [Enzo Menali](https://github.com/menali17) | Participação nas discussões, definição do cenário, revisão do fluxo e documentação da modelagem. |
| [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | Participação nas discussões, elaboração e revisão do diagrama, análise da rastreabilidade e documentação. |
| [Lucas Oliveira](https://github.com/dev-LucasDpaula) | Participação nas discussões, validação dos participantes, revisão dos fragmentos e documentação. |
| [Paulo Vitor Gomes](https://github.com/gpaulovit) | Participação nas discussões, validação do fluxo e revisão coletiva da modelagem. |

---

## 11. Referências

- **SERRANO, Milene.** *Arquitetura e Desenho de Software — Aula: Modelagem UML Dinâmica*. Universidade de Brasília (UnB). Material didático da disciplina.

- **OBJECT MANAGEMENT GROUP (OMG).** *OMG Unified Modeling Language (OMG UML), Version 2.5.1*. 2017. Disponível em:  
  <https://www.omg.org/spec/UML/2.5.1>  
  Acesso em: 17 set. 2026.

---

## 12. Bibliografia Consultada

- **UML-DIAGRAMS.** *UML Sequence Diagrams Overview*. Disponível em:  
  <https://www.uml-diagrams.org/sequence-diagrams.html>  
  Acesso em: 17 set. 2026.

---

## 13. Histórico de Versão

| Data | Versão | Descrição | Autor(es) | Revisores |
|---|---|---|---|---|
| 17/09/2026 | 1.0 | Criação inicial da documentação do Diagrama de Sequência “Carregar e reproduzir um vídeo”. | [Enzo Menali](https://github.com/menali17), [Geovanna Umbelino](https://github.com/GeovannaUmbelino), [Lucas Oliveira](https://github.com/dev-LucasDpaula) e [Paulo Vitor Gomes](https://github.com/gpaulovit) | [Pedro Américo](https://github.com/dev-americo) e [Gabriel Diniz](https://github.com/GabrielDiniz12) |
