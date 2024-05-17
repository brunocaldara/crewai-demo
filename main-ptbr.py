import os

from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

ferramenta_pesquisa = SerperDevTool()

pesquisador = Agent(
    role='Pesquisador Sênior',
    goal='Descobrir tecnologias inovadoras em IA',
    verbose=True,
    memory=True,
    backstory='Motivado pela curiosidade, na vanguarda da inovação, ansioso para explorar e compartilhar conhecimento.',
    tools=[ferramenta_pesquisa],
    allow_delegation=True
)

escritor = Agent(
    role='Escritor',
    goal='Narrar histórias tecnológicas envolventes sobre IA',
    verbose=True,
    memory=True,
    backstory='Com um talento para simplificar tópicos complexos, criando narrativas envolventes.',
    tools=[ferramenta_pesquisa],
    allow_delegation=False
)

tarefa_de_pesquisa = Task(
    description='Identificar a próxima grande tendência em IA. Focar nos prós e contras e na narrativa geral.',
    expected_output='Um relatório compreensivo de 3 parágrafos sobre as últimas tendências em IA.',
    tools=[ferramenta_pesquisa],
    agent=pesquisador
)

tarefa_de_escrita = Task(
    description='Compor um artigo perspicaz sobre tendências de IA e seu impacto na marketing digital.',
    expected_output='Um artigo de 4 parágrafos formatado em markdown.',
    tools=[ferramenta_pesquisa],
    agent=escritor,
    async_execution=False,
    output_file='novo-post-no-blog.md'
)

equipe = Crew(
    agents=[pesquisador, escritor],
    tasks=[tarefa_de_pesquisa, tarefa_de_escrita],
    process=Process.sequential,
    max_rpm=1,
    cache=True,
    memory=True,
    language='pt-BR'
)

resultado = equipe.kickoff(inputs={'topic': 'IA no Markenting Digital'})
print(resultado)
