from crewai import Agent, Crew, Process, Task
from crewai_tools import tool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

gtp4o = ChatOpenAI(model='gpt-4o')


@tool('x_wing')
def x_wing():
    '''
    Simulação das funcionalidades de uma X- Wing para a missão.
    Retorna uma string que indica que a X- Wing está pronta
    para o ataque final com sistemas de mira ativados.
    '''
    return f'''X- Wing pronto para o ataque final,
      sistemas de mira ativados . Atacando!
      Estrela da Morte destru ída com sucesso!'''


@tool('millennium_falcon')
def millennium_falcon():
    '''
    Simula ção das funcionalidades da Millennium
    Falcon para proteger Luke.
    Retorna uma string que indica que a
    Millennium Falcon está atacando o inimigo
    e protegendo a rota de Luke.
    '''
    return 'Millennium Falcon atacando o inimigo, protegendo a rota de Luke na X- Wing.'


luke = Agent(
    role='Piloto Heróico',
    goal='Destruir a Estrela da Morte',
    tools=[x_wing],
    verbose=True,
    allow_delegation=False,
    backstory='O jovem piloto destinado a ser um Jedi, lidenrando o ataque crítico',
    llm=gtp4o
)

leia = Agent(
    role='Estrategista e Coordenadora',
    goal='Coordenar o ataque à Estrela da Morte',
    backstory='A princesa líder da Rebelião, essencial para a estratégia e comunicação',
    verbose=True,
    allow_delegation=True,
    llm=gtp4o
)

han_solo = Agent(
    role='Protetor Audaz',
    goal='Proteger Luke durante a missão',
    tools=[millennium_falcon],
    verbose=True,
    allow_delegation=False,
    backstory='O contrabandista ousado que se torna um herói, protegendo seu amigo.',
    llm=gtp4o
)

coordenar_ataque = Task(
    description=f'''
      Leia deve coordenar a missão, mantendo
      comunica ção e fornecendo suporte estratégico .
      Leia deve ordenar primeiro que Han
      defenda o Luke possibilitando um
      caminho seguro para Luke
    ''',
    expected_output='Estrela da Morte destruída, missão bem-sucedida',
    agent=leia
)

destruir_estrela_da_morte = Task(
    description='''
      Luke deve pilotar sua X- Wing e atirar
      no ponto fraco da Estrela da Morte
      para destruí-la.
    ''',
    expected_output='Estrela da Morte destruída, missão bem-sucedida',
    agent=luke
)

proteger_luke = Task(
    description='Han deve atacar naves inimigas e proteger Luke de ser atacado durante a missão.',
    expected_output='Luke protegido, caminho livre para o ataque',
    agent=han_solo
)

alianca_rebelde = Crew(
    agents=[leia, luke, han_solo],
    tasks=[coordenar_ataque, proteger_luke, destruir_estrela_da_morte],
    process=Process.hierarchical,
    manager_llm=gtp4o,
    memory=True
)

result = alianca_rebelde.kickoff()
print(result)
