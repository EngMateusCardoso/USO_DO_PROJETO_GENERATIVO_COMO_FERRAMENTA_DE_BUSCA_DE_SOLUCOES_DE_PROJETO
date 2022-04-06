# Uso do projeto generativo como ferramenta de busca de soluções de projeto

Olá!😆 Seja Bem vindo ao repositório do programa (ou projeto computacional) do meu Trabalho de Conclusão de Curso.🎓 <br/>
É um prazer tê-lo(a) aqui,🥰 este readme é feito com todo o carinho para você se situar neste trabalho.<br/>
Na seção de conceitos explico em poucas palavras o básico de alguns conceitos importantes para entender os desafios deste trabalho, é pouca coisa dá uma conferida.😉 <br/>
Em seguida conheça o Resumo e o Abstract do trabalho para ter uma visão mais geral. <br/>
Então conheça um pouco como o projeto funciona, aqui você vai ver prints dele funcionando passo-a-passo dos comandos e os resultados.<br/>
Conheça um breve resumo das linguagens utilizadas na seção Ferramentas. <br/>
Por fim entenda a estrutura do código principal em dynamo.<br/>
Navegue pelo readme na seção a baixo.

## Navegação

- [Ir para Conceitos](#conceitos)
- [Ir para Resumo](#resumo)
- [Ir para Abstract](#abstract)
- [Ir para Projeto](#projeto)
- [Ir para Ferramentas](#ferramentas)
- [Ir para Algoritmo](#o-algoritmo)

## Conceitos
#### **O que é Projeto Generativo?**
É a utilização de Algoritmos Evolutivos, e em especial Algoritmos Genéticos, como método de criação de soluções de projeto.
#### **O que são Algoritmos Genéticos?**
Como ferramenta de busca os Algoritmos Genéticos procura entre as opções de projeto, aqueles que melhor performam frente aos objetivos do projeto. Esse algoritmo de busca é inspirado nas teorias da Evolução das Espécies proposta por Darwin.
#### **Que tipo de projeto é aplicavél o projeto generativo?**
Usualmente projetos multiobjetivo. Em especial esse trabalho é aplicado a projeto de vigas de concreto armado. Pois naturalmente, propostas de estruturas de concreto armado envolvem problemas multiobjetivos, pois, devem apresentar uma solução adequada a arquitetura, ao mesmo tempo que atenda aos estados limites e minimize custos. Muitas vezes estes objetivos são conflitantes entre si, complicando a tarefa de escolher a melhor solução. Neste sentido o Projeto Generativo pode ser uma eficiente ferramenta auxiliar na exploração de opções de projeto na área de estruturas.

## Resumo
No contexto de avanço de métodos de automação e otimização de projetos, este trabalho dedica-se a avaliar o uso do projeto generativo como ferramenta de busca de soluções de projeto aplicado a vigas de concreto armado. Para tanto, apresenta conceitos básicos presentes no projeto generativo como o algoritmo genético, projeto computacional, otimização multiobjetivo e integração com o BIM. Em seguida, são detalhadas as condições do exemplo de aplicação, este, é desenvolvido para projetos no Revit, cujo projeto computacional é desenvolvida no Dynamo. O projeto computacional gera uma viga de concreto armado a partir de informações do Revit, e então avalia algumas de suas propriedades como custo, deslocamento vertical e comprimento da armadura. Por isso, o projeto computacional é dividido em estrutura de entrada, algoritmo gerador, algoritmo avaliador e estrutura de saída. O projeto generativo gerou os resultados esperados, operou corretamente com o projeto do Revit, desenhou a Fronteira de Pareto e explorou o espaço de projeto de acordo com a proposta de cada solucionador. Portanto, atestando o correto funcionamento da estrutura computacional paramétrica e constatando o desempenho do projeto generativo como ferramenta de busca de soluções de projeto.

## Abstract
Considering automation and optimization methods improvement, this project dedicates to evaluating the employing of Generative Design as a tool capable of finding design solutions to reinforced concrete beams. Therefore, it presents basic concepts of generative design as genetic algorithm, computational design, multi-objective optimization and integration with BIM. Then, the conditions of the applicated example are detailed to projects in Revit and the computational project is developed in Dynamo. The computational design generates a reinforced concrete beam from Revit’s information and analyzes some of its properties like cost, vertical displacement, and reinforcement length. Hence, the computational project is divided into input structure, genetic algorithm, evaluator algorithm and output structure. The generative project achieved expected results, collaborated correctly with the Revit project, plotted Pareto solutions, and explored the project space according to each solver’s characteristics. Ultimately, it was possible to attest the correct functioning of the parametric computational structure, as well as verify the performance of the generative design to search for design solutions.

## Projeto

## Ferramentas

## O Algoritmo
