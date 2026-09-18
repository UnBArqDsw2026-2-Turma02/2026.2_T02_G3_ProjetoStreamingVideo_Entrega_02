# Diagrama de Componentes

## 1. Introdução

O **Diagrama de Componentes** foi utilizado no projeto **Streaming de Vídeo** para representar a organização arquitetural da aplicação em blocos de maior granularidade. Diferentemente do Diagrama de Classes, que detalha elementos do domínio e suas relações, este modelo concentra-se em **módulos, componentes, interfaces e dependências** entre partes da solução.

A representação foi construída a partir da estrutura do frontend e de suas integrações, destacando o **Angular SPA**, os módulos funcionais, os recursos compartilhados, os serviços centrais e os sistemas externos responsáveis por reprodução, API e entrega de mídia.

A elaboração do diagrama também manteve relação com artefatos desenvolvidos anteriormente no projeto. O  [**Rich Picture**](https://unbarqdsw2026-2-turma02.github.io/2026.2_T02_G3_ProjetoStreamingVideo_Entrega_01/#/Base/Relat%C3%B3rios/1.2.SubEquipe_02/richpicture), o [**modelagem BPMN**](https://unbarqdsw2026-2-turma02.github.io/2026.2_T02_G3_ProjetoStreamingVideo_Entrega_01/#/Base/Relat%C3%B3rios/1.2.SubEquipe_02/modelagem_bpmn), a [**engenharia reversa**](https://unbarqdsw2026-2-turma02.github.io/2026.2_T02_G3_ProjetoStreamingVideo_Entrega_01/#/Base/Relat%C3%B3rios/1.2.SubEquipe_02/Engenharia_reversa) e o [**Diagrama de Classes**](Base/Relatórios/SubEquipe_02/1.ModelagemEstatica.md) serviram como fontes de apoio para compreender responsabilidades, fluxos e elementos que deveriam ser agrupados em uma visão arquitetural de mais alto nível.

Com isso, o diagrama busca facilitar a compreensão de como as principais partes do frontend se organizam e de quais serviços ou interfaces cada uma depende para cumprir suas responsabilidades.

## 2. Metodologia

A elaboração do Diagrama de Componentes partiu da análise conjunta da arquitetura já existente e dos artefatos produzidos anteriormente pela equipe.

Primeiro, foram observados os elementos identificados pela **engenharia reversa** e pelo **Diagrama de Classes**, buscando reconhecer quais responsabilidades poderiam ser agrupadas em módulos de maior nível. Em seguida, o **Rich Picture** e o **BPMN** foram utilizados como apoio para conferir se os agrupamentos definidos eram coerentes com o contexto e com os fluxos do sistema.

A equipe então organizou a solução em três perspectivas principais:

- **estrutura interna do frontend**, representada pelo Angular SPA e seus componentes;
- **módulos funcionais**, responsáveis pelas diferentes capacidades da aplicação;
- **integrações externas**, representadas por interfaces requeridas e oferecidas.

Durante a reunião de modelagem, os integrantes revisaram os agrupamentos, as dependências e o nível de abstração adotado, buscando evitar tanto um diagrama excessivamente genérico quanto uma representação detalhada demais.



## 3. Diagrama de Componentes

O diagrama abaixo apresenta a modelagem estática elaborada para a visão de componentes do projeto **Streaming de Vídeo**.

![Diagrama de Componentes](../../../assets/WhatsApp%20Image%202026-09-15%20at%2022.41.03%20(2).jpeg)

---

## 4. Visão Arquitetural Representada

O diagrama apresenta o frontend como um sistema organizado em diferentes níveis de responsabilidade. O **Angular SPA** concentra a aplicação cliente, enquanto os elementos internos são distribuídos entre navegação, funcionalidades, recursos reutilizáveis e serviços globais.

### 4.1. Organização Interna do Frontend

O **Shell e Roteamento** funciona como ponto de organização da navegação e do carregamento das rotas da aplicação.

Os **Módulos Funcionais** concentram as funcionalidades principais da plataforma:

- **Identidade e Acesso**, relacionado à autenticação e autorização;
- **Descoberta e Busca**, relacionado à localização e exploração de conteúdos;
- **Reprodução e Interações**, responsável pelo consumo de mídia e interação durante a reprodução;
- **Espaço do Usuário**, relacionado às funcionalidades pessoais do usuário;
- **Publicação e Gestão de Vídeos**, responsável pela criação e administração dos conteúdos publicados.

Além desses módulos, o frontend possui **Recursos Compartilhados**, usados para elementos reutilizáveis, e **Serviços Core**, que concentram serviços de uso global na aplicação.

### 4.2. Integrações Externas

O frontend depende de três integrações principais:

- **Servidor / API PeerTube**, responsável por disponibilizar serviços acessados pela interface `IPeerTubeREST`;
- **PeerTube Player**, responsável por oferecer a interface `IPlayer`;
- **Entrega de Mídia HLS / P2P**, responsável por disponibilizar a interface `IStreamingMedia`.

Essas integrações deixam explícito que determinadas responsabilidades não pertencem ao frontend, mas são fornecidas por componentes ou sistemas externos.

### 4.3. Interfaces e Dependências

O uso das interfaces **IPeerTubeREST**, **IPlayer** e **IStreamingMedia** foi importante para deixar claro no modelo **quem requer e quem oferece determinado serviço**.

Os módulos internos não precisam conhecer todos os detalhes de implementação dos sistemas externos; o diagrama mostra apenas os pontos de dependência necessários para o funcionamento da aplicação. Essa decisão reduz o acoplamento conceitual da representação e deixa mais evidente a separação de responsabilidades entre frontend, reprodução e infraestrutura de mídia.

### 4.4. Nível de Abstração Adotado

A equipe optou por representar componentes em um nível intermediário de abstração. O objetivo foi mostrar a estrutura arquitetural sem transformar o diagrama em uma representação de classes, arquivos ou detalhes de implementação.

Por esse motivo, elementos como componentes específicos de interface, classes internas, métodos e estruturas de banco de dados não aparecem no modelo. Essas informações são tratadas em outros artefatos da documentação.

## 5. Justificativa e Senso Crítico do Modelo

### 5.1. Por que este diagrama foi utilizado

O Diagrama de Componentes foi adotado porque a equipe precisava de uma visão que mostrasse **como a aplicação está dividida em partes maiores** e de que forma essas partes se conectam.

Enquanto outros artefatos descrevem processos ou elementos do domínio, este diagrama ajuda a compreender a distribuição das responsabilidades entre módulos internos e sistemas externos. Isso é especialmente relevante no projeto por existirem integrações distintas para API, reprodução e entrega de mídia.

### 5.2. Decisões consideradas adequadas

A separação entre **Módulos Funcionais**, **Recursos Compartilhados** e **Serviços Core** evita concentrar responsabilidades diferentes em um único bloco e torna a arquitetura mais compreensível.

Outro ponto importante foi representar explicitamente as interfaces externas. Dessa forma, o diagrama não mostra apenas que existe uma integração, mas também qual serviço é requerido ou oferecido em cada relação.

O uso do **Diagrama de Classes** como apoio também contribuiu para essa organização, pois permitiu partir de responsabilidades já identificadas no domínio e agrupá-las em estruturas arquiteturais maiores.

### 5.3. Limitações e possíveis refinamentos

O modelo não representa o comportamento interno de cada componente, nem a sequência de chamadas entre eles. Também não detalha bibliotecas, arquivos, componentes visuais ou mecanismos internos de persistência.

Essas ausências são intencionais, pois o foco do diagrama é a organização estrutural da solução.

Em versões futuras, caso seja necessário aprofundar a arquitetura, o modelo poderá detalhar novas integrações, subdividir módulos muito amplos ou explicitar interfaces adicionais entre componentes internos.

## 6. Participações e Trabalho em Equipe

### 6.1. Processo de Construção

A modelagem foi construída de forma colaborativa. Durante a reunião da equipe, os integrantes discutiram quais componentes deveriam ser representados, qual seria o nível de detalhamento adequado e como as dependências entre os módulos poderiam ser modeladas de forma clara e coerente.

Após essa definição inicial, o diagrama passou por ajustes relacionados à organização visual, refinamento dos agrupamentos e revisão da documentação, até chegar à versão consolidada.

### 6.2. Registro da Reunião

A reunião utilizada na construção e validação do diagrama foi gravada para manter o registro e a rastreabilidade das decisões tomadas pela equipe.

**Registro da reunião:** [Acessar vídeo da reunião](./Atas/Atas_subequipe_2.md)

### 6.3. Quadro de Participações

| Integrante | Participação |
|---|---|
| [Enzo Menali](https://github.com/menali17) | Participação nas discussões, definição das ideias, elaboração, documentação e revisão coletiva da modelagem. |
| [Geovanna Umbelino](https://github.com/GeovannaUmbelino) | Participação nas discussões, definição das ideias, elaboração, documentação e revisão coletiva da modelagem. |
| [Lucas Oliveira](https://github.com/dev-LucasDpaula) | Participação nas discussões, definição das ideias, elaboração, documentação e revisão coletiva da modelagem. |
| [Paulo Vitor Gomes](https://github.com/gpaulovit) | Participação nas discussões, definição das ideias e revisão coletiva da modelagem. |

---

## 7. Referências

- **SERRANO, Milene.** *Arquitetura e Desenho de Software — Aula: Modelagem UML Estática*. Universidade de Brasília (UnB). Material didático da disciplina.

- **OBJECT MANAGEMENT GROUP (OMG).** *OMG Unified Modeling Language (OMG UML), Version 2.5.1*. 2017. Disponível em:  
  <https://www.omg.org/spec/UML/2.5.1>  
  Acesso em: 17 set. 2026.



## 8. Bibliografia 

- **IBM.** *Component Diagrams*. IBM Documentation. Disponível em:  
  <https://www.ibm.com/docs/>  
  Acesso em: 17 set. 2026.

- **UML-DIAGRAMS.** *UML Component Diagrams Overview*. Disponível em:  
  <https://www.uml-diagrams.org/component-diagrams-overview.html>  
  Acesso em: 17 set. 2026.

---

## 9. Histórico de Versão

| Data | Versão | Descrição | Autor(es) | Revisores |
|---|---|---|---|---|
| 17/09/2026 | 1.0 | Criação inicial da documentação do Diagrama de Componentes. | [Enzo Menali](https://github.com/menali17), [Geovanna Umbelino](https://github.com/GeovannaUmbelino), [Lucas Oliveira](https://github.com/dev-LucasDpaula) e [Paulo Vitor Gomes](https://github.com/gpaulovit) | [Pedro Américo](https://github.com/dev-americo) e [Gabriel Diniz](https://github.com/GabrielDiniz12) |
