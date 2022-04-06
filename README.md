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
Para aplicação do solucionador genético foi idealizado um projeto arquitetônico conceitual no Revit 2021. Este projeto tem o papel de simular as condições e restrições das vigas em um projeto real.
### Projeto demonstrativo
O projeto consiste em um ambiente de 3,0 x 2,5 m de dimensões internas e 3,0 m de altura, como na Figura a seguir. Os elementos arquitetônicos que vão restringir o modelo são os pilares de 20 x 30 cm, as paredes de 20 cm de espessura, uma porta de 2,1 m de altura e uma janela de 90 cm de altura com peitoril de 1,5 m. Esses elementos limitam as dimensões de base e altura das vigas exploradas.
<br/><br/>
![image](https://user-images.githubusercontent.com/93548287/162079599-984953c1-5ded-49a5-9983-8a287f14eae8.png) <br/><br/>
As vigas foram nomeadas de V1, V2, V3 e V4 conforme a Figura a seguir. O carregamento das vigas é extraído de uma planilha de Excel. As informações de carregamento obtidas no Excel são: a carga permanente, g em kN/m; a carga variável, q em kN/m; os momentos negativos nas extremidades da viga, M1 e M2 em kNm. A Figura 24 mostra o modelo de carregamento considerado. <br/><br/>
![image](https://user-images.githubusercontent.com/93548287/162079701-7a1e7b43-c7c8-442c-bdfa-d6e8681f65c3.png) <br/><br/>
Os carregamentos e solicitações referentes as vigas exploradas podem ser verificadas na Tabela a seguir: <br/>
Vigas |	V1	| V2
------ | --- | -----
g (kN/m) |	30 |	40
q (kN/m) |	20 |	40
M1 (kNm) |	50 |	80
M2 (kNm) |	100 |	80

Construiu-se uma estrutura paramétrica para que, ao ser executada, o projetista faça a seleção da viga que será explorada, suas restrições geométricas (limitações de altura de largura) e a escolha do solucionador. Após o processamento são apresentadas pelo algoritmo as opções de projeto e depois da exploração das opções o algoritmo integra a opção escolhida ao restante do projeto.
### Aplicação

Após exportada a estrutura fica disponível na biblioteca do Generative Design. A biblioteca é acessada na aba Gerenciar, no ambiente de Projeto generativo, pelo botão de Criar estudo, Figura 39:
<br/><br/>Figura 39 - Criar estudo<br/>
![image](https://user-images.githubusercontent.com/93548287/162081533-4373d039-3dca-469d-a5c3-6cf30a3a91cb.png)
<br/><br/> 
Após selecionar o exemplo de aplicação, deve-se escolher o tipo de solucionador utilizado. O Generative Design oferece as opções apresentadas na Figura 40. Neste exemplo é utilizado método de otimizar.
<br/><br/>Figura 40 – Opções de solucionador<br/>
![image](https://user-images.githubusercontent.com/93548287/162081747-058669e6-fd7e-470e-a4f9-921252f829b4.png)
<br/><br/>
Como dito no item 3.2.1 os nós de seleção marcados como ‘de entrada’ são variáveis de estudo, desse modo, na caixa do estudo aparece os botões de seleção referente a cada um destes nós. Após clicar no botão ‘selecionar’, Figura 41, o projetista seleciona na interface do Revit a viga que será explorada e as faces que a limitam.  <br/><br/> Figura 41 - Seleção no modelo<br/>
![image](https://user-images.githubusercontent.com/93548287/162081764-4c325d62-5c7f-4cd3-ab2f-92f411fbf95d.png)
<br/><br/>
Em seguida o projetista deve definir as metas do estudo, Figura 42. Todos os nós marcados como ‘de saída’ descritos no item 3.2.3 vão aparecer como opções de otimização e restrição. Neste trabalho foram feitos três diferentes estudos: o primeiro com apenas um objetivo de minimizar o custo da viga, o segundo de dois objetivos que minimiza a flecha total também e o terceiro com três objetivos que adicionalmente minimiza o comprimento total de armadura longitudinal utilizada.
 <br/><br/>Figura 42 - Metas do estudo com dois objetivos<br/>
 ![image](https://user-images.githubusercontent.com/93548287/162081837-e0a685e0-04d3-42ad-81b4-883379920e44.png)
 <br/><br/>
A definição das restrições segue os limites apresentados no item 3.2.3(do relatório). Observe que, as restrições podem ser aplicadas antes do processamento como na Figura 43 ou após o processamento com a filtragem dos resultados. <br/>
Se aplicados antes do processamento o NSGA-II vai desencorajar a exploração de regiões promissoras do espaço de projeto que não atenderem as restrições, já filtrar as opções após o processamento permite a exploração do espaço de projeto sem restrições. Observou-se que o modelo apresentou poucas opções de projeto que não atendem restrições, por isso, optou-se por aplicar as condições de restrições com os filtros após o processamento.
 <br/><br/> Figura 43 - Definição das restrições<br/>
![image](https://user-images.githubusercontent.com/93548287/162081869-2ab760c2-6700-4689-a04d-ffc4bf7934aa.png)
  <br/><br/>
Por fim, na configuração de geração, o projetista define o tamanho da população de cada geração e o número de gerações do estudo, neste projeto, inicialmente foram usadas as configurações padrão do Generative Design, Figura 44.
 <br/><br/>Figura 44 - Configurações da geração<br/>
![image](https://user-images.githubusercontent.com/93548287/162081906-e4457e82-1ab1-4d5e-b202-b2ec7ffb949d.png)
  <br/><br/>
Nos resultados do Generative Design são apresentadas as opções de projetos e os gráficos. As opções de projeto, ficam na parte superior a esquerda e podem ser apresentadas em grade como na Figura 45 ou em lista como na Figura 46. Já os gráficos, podem ser apresentados em gráficos de coordenadas paralelas ou gráfico de dispersão, Figura 45 e 46 respectivamente. Qualquer opção de projeto selecionada é imediatamente detalhada no lado direito. 
<br/><br/>Figura 45 - Resultados modelo 1<br/>
![image](https://user-images.githubusercontent.com/93548287/162081938-7c503993-9d51-4552-9c11-490ff3cbac44.png)
<br/><br/>Figura 46 - Resultados modelo 2<br/>
![image](https://user-images.githubusercontent.com/93548287/162081953-705abf19-477a-4603-b081-78a8dda51bdf.png)
<br/><br/>
O resultado da otimização com apenas um objetivo (o custo da viga) é apresentado na Figura 47. Note que, para um objetivo o algoritmo naturalmente apresenta apenas uma opção de projeto. Observe que, estão destacados os valores de flecha total e comprimento de armadura dessa opção, esses valores são importantes para serem comparados com os estudos com mais objetivos.
 <br/><br/>Figura 47 - Resultado para um objetivo<br/>
 ![image](https://user-images.githubusercontent.com/93548287/162081991-070ff81c-38cb-4430-824d-629e9be2adad.png)
  <br/><br/>
A otimização com duplo objetivo, por sua vez, apresenta um conjunto de soluções ideais com a formação da Frente Ideal de Pareto. A Figura 48 mostra a essa frente ideal, o gráfico tem a flecha total representada no eixo vertical e o custo da viga no eixo horizontal. Como esperado, não existe nenhuma solução na frente ideal que seja superada em ambos os objetivos por uma outra solução.
 <br/><br/>Figura 48 - Frente de Pareto objetivo duplo com 10 gerações<br/>
![image](https://user-images.githubusercontent.com/93548287/162082003-4f9ef10e-da38-4585-8323-b76f820b9626.png)
  <br/><br/>
Observe que, o estudo com objetivo duplo apresentou a maioria das soluções mais custosas que o estudo com um único objetivo, porém estas soluções apresentam uma flecha total menor. Esse comportamento é esperado uma vez que, a otimização de objetivo único está comprometida apenas com o custo, portanto entrega resultados melhores deste avaliador. 
O estudo foi repetido com 20 (Figura 49) e 40 gerações (Figura 50), desse modo, o estudo permite a exploração de opções de projeto melhores e com menores valores de custo e flecha total. Além disso, um maior número de gerações vai formar uma Frente de Pareto mais clara. 
 <br/><br/>Figura 49 - Frente de Pareto objetivo duplo com 20 gerações<br/>
 ![image](https://user-images.githubusercontent.com/93548287/162082010-3d975d24-795e-4d9e-b95a-5bf2c2171f44.png)
 <br/><br/>Figura 50 - Frente de Pareto objetivo duplo com 40 gerações<br/>
 ![image](https://user-images.githubusercontent.com/93548287/162082014-97f9bd7f-25dc-4589-99ed-fcfbb41a9e04.png)
  <br/><br/>
O estudo de objetivo triplo deve apresentar uma Frente de Pareto no espaço tridimensional, neste, além dos eixos verticais e horizontais representarem flecha e o custo, a cor dos pontos indica o comprimento total de armadura longitudinal utilizado, como na Figura 51. Onde, as cores vermelhas representam comprimento total mais curto, enquanto as cores laranja, roxo, verde e azul, nessa ordem, são opções com maior comprimento.<br/>
O gráfico da Figura 51, tem alguns formatos de Fronteiras de Pareto, estas são fronteiras ideais de diferentes regiões do espaço de projeto.  Esse efeito é causado devido a tridimensionalidade dos objetivos e a presença de alguma descontinuidade.<br/>
O gráfico da Figura 52 é semelhante ao anterior, no entanto, a cor dos pontos representa o diâmetro da armadura. Nota-se que cada uma das frentes ideais tem soluções com diâmetros diferentes de barras. Isto aponta que a descontinuidade ocorre na mudança de diâmetro de uma barra para outra.
 <br/><br/>Figura 51 - Frente ideal de objetivo triplo.<br/>
 ![image](https://user-images.githubusercontent.com/93548287/162082040-450a1d25-f631-4c1b-a27d-acf315b173d7.png)
  <br/><br/>Figura 52 - Frente ideal de objetivo triplo relação com diâmetros<br/>
![image](https://user-images.githubusercontent.com/93548287/162082970-cdb411a7-ff9d-4163-8a3c-20fc04380541.png)
  <br/><br/>
Depois da exploração das opções de projeto pelo projetista, ele deve integrar a opção escolhida ao restante do modelo. Para isso, basta selecionar a opção desejada e clicar no botão ‘Criar elementos do Revit’. Esse botão pode ser visto nas Figuras 46 e 47, na parte inferior a direita. Então o Generative Design importa para o modelo a viga selecionada como na Figura 53.
 <br/><br/>Figura 53 - Integração da opção de projeto no modelo<br/>
 ![image](https://user-images.githubusercontent.com/93548287/162082990-bd064d79-ac0c-4823-b990-66a1255fe670.png)
  <br/><br/>
  
### Exploração do espaço de projeto por diferentes solucionadores
Neste subcapitulo será discutido como os diferentes solucionadores genéticos do Generative Design exploram o espaço de projeto aplicados a viga V2. Os gráficos deste capítulo são construídos com eixo vertical referente a porcentagem da altura da viga e horizontal e eixo horizontal ao f_ck do concreto. <br/>
Cada solucionador ou método irá explorar o espaço de projeto de formas diferentes. <br/>
O método de ‘Randomizar’ vai explorar todo espaço de projeto de forma aleatória. Note que, os eixos de altura e de f_ck compreendem todo o espaço de projeto e a distribuição de pontos é aleatória, Figura 54. <br/>
<br/><br/>Figura 54 - Espaço de projeto do Método Randomizar<br/>
 ![image](https://user-images.githubusercontent.com/93548287/162083240-fe869e7c-5bd6-4fb3-b4e3-c70f4b9c0487.png)
<br/><br/>
Já o método ‘Curtir isso’, cria opções de projetos semelhantes a uma opção inicial que o projetista já gosta. Para esse exemplo foi atribuído um valor aleatório inicial para os parâmetros de altura e f_ck: 0,8 e 25 Mpa respectivamente. Neste caso, as opções estão concentradas numa região do espaço de projeto, o f_ck só varia em 3 valores e a porcentagem de altura varia num intervalo limitado no espaço de projeto, como na Figura 55.
<br/><br/>Figura 55 - Espaço de projeto do Método Curtir isso<br/><br/>
 ![image](https://user-images.githubusercontent.com/93548287/162083247-98cd9572-2d83-4c64-8b5f-654f4b2ce2c4.png)
<br/><br/>
O método de Otimização também retorna opções pouco dispersas no espaço de projeto, no entanto este método vai escolher de forma inteligente as regiões ótimas. Neste gráfico os eixos também estão limitados, Figura 56, no entanto, diferente do método anterior, o algoritmo genético escolheu a região que irá se concentrar, por exemplo, procura valores de f_ck mais altos. Vale destacar que a otimização embora teste 200 opções de projetos, somente 13 opções foram consideradas ideais e pertencem a solução deste método.
<br/><br/>Figura 56 - Espaço de projeto da otimização<br/>
 ![image](https://user-images.githubusercontent.com/93548287/162083263-ff58714d-98d0-4f79-aa7f-5086b0c43a8c.png)
<br/><br/>
Por fim, o produto transversal explora todo espaço de projeto e dispersa as opções de projeto de forma padronizada e equidistantes como na Figura 57. Uma vez que o espaço de projeto definido no item 3.2.1 é muito grande, para tornar esse método exequível, o estudo aumentou o passo das variáveis e algumas delas foram transformadas em constantes.
<br/><br/>Figura 57 - Espaço de projeto do produto transversal<br/>
 ![image](https://user-images.githubusercontent.com/93548287/162083276-aa2153b6-9e8f-41c5-b01d-1f931e0020ac.png)
<br/><br/>


## Ferramentas

## O Algoritmo
