"""
Script para popular o banco de dados com registros de exemplo
Execute com: python manage.py shell < popular_banco.py
"""

import os
import django
from datetime import datetime, timedelta
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pw2025.settings')
django.setup()

from django.contrib.auth.models import User
from paginasweb.models import Doador, Instituicao, Status, Doacao, Historia_Inspiradoras

# Limpar dados existentes (opcional - comente se não quiser limpar)
print("Limpando dados existentes...")
Historia_Inspiradoras.objects.all().delete()
Doacao.objects.all().delete()
Doador.objects.all().delete()
Instituicao.objects.all().delete()
Status.objects.all().delete()

# Criar ou obter superusuário
print("\nCriando usuário admin...")
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@solly.com',
        'is_staff': True,
        'is_superuser': True,
    }
)
if created:
    admin_user.set_password('admin123')
    admin_user.save()
    print(f"✓ Superusuário criado: {admin_user.username}")
else:
    print(f"✓ Superusuário já existe: {admin_user.username}")

# Criar usuários normais
print("\nCriando usuários normais...")
usuarios = []
nomes_usuarios = ['joao', 'maria', 'pedro', 'ana', 'carlos', 'juliana', 'rafael', 'patricia', 'lucas', 'fernanda']

for nome in nomes_usuarios:
    user, created = User.objects.get_or_create(
        username=nome,
        defaults={
            'email': f'{nome}@email.com',
            'first_name': nome.capitalize(),
        }
    )
    if created:
        user.set_password('senha123')
        user.save()
    usuarios.append(user)

print(f"✓ {len(usuarios)} usuários criados/verificados")

# Criar Status
print("\nCriando status...")
status_list = [
    Status(nome="Pendente", pode_editar=True),
    Status(nome="Em Processamento", pode_editar=True),
    Status(nome="Confirmado", pode_editar=True),
    Status(nome="Entregue", pode_editar=False),
    Status(nome="Cancelado", pode_editar=False),
    Status(nome="Aguardando Retirada", pode_editar=True),
    Status(nome="Em Transporte", pode_editar=True),
    Status(nome="Recebido", pode_editar=False),
    Status(nome="Agradecido", pode_editar=False),
    Status(nome="Arquivado", pode_editar=False),
]

for status in status_list:
    status.save()

print(f"✓ {len(status_list)} status criados")

# Criar Doadores
print("\nCriando doadores...")
doadores_data = [
    {"nome": "João Silva", "telefone": "(11)98765-4321", "cidade": "São Paulo", "usuario": usuarios[0]},
    {"nome": "Maria Santos", "telefone": "(21)97654-3210", "cidade": "Rio de Janeiro", "usuario": usuarios[1]},
    {"nome": "Pedro Costa", "telefone": "(31)96543-2109", "cidade": "Belo Horizonte", "usuario": usuarios[2]},
    {"nome": "Ana Oliveira", "telefone": "(41)95432-1098", "cidade": "Curitiba", "usuario": usuarios[3]},
    {"nome": "Carlos Mendes", "telefone": "(51)94321-0987", "cidade": "Porto Alegre", "usuario": usuarios[4]},
    {"nome": "Juliana Lima", "telefone": "(61)93210-9876", "cidade": "Brasília", "usuario": usuarios[5]},
    {"nome": "Rafael Souza", "telefone": "(71)92109-8765", "cidade": "Salvador", "usuario": usuarios[6]},
    {"nome": "Patricia Alves", "telefone": "(81)91098-7654", "cidade": "Recife", "usuario": usuarios[7]},
    {"nome": "Lucas Ferreira", "telefone": "(85)90987-6543", "cidade": "Fortaleza", "usuario": usuarios[8]},
    {"nome": "Fernanda Rocha", "telefone": "(91)89876-5432", "cidade": "Belém", "usuario": usuarios[9]},
]

doadores = []
for data in doadores_data:
    doador = Doador(**data)
    doador.save()
    doadores.append(doador)

print(f"✓ {len(doadores)} doadores criados")

# Criar Instituições
print("\nCriando instituições...")
instituicoes_data = [
    {
        "nome": "Casa de Apoio Esperança",
        "telefone": "(11)3456-7890",
        "cidade": "São Paulo",
        "tipo": "Abrigo",
        "descricao": "Abrigo para crianças e adolescentes em situação de vulnerabilidade social",
        "usuario": admin_user
    },
    {
        "nome": "ONG Amigos da Natureza",
        "telefone": "(21)3567-8901",
        "cidade": "Rio de Janeiro",
        "tipo": "ONG Ambiental",
        "descricao": "Organização dedicada à preservação ambiental e educação ecológica",
        "usuario": admin_user
    },
    {
        "nome": "Instituto Sorriso de Criança",
        "telefone": "(31)3678-9012",
        "cidade": "Belo Horizonte",
        "tipo": "ONG Social",
        "descricao": "Apoio educacional e psicológico para crianças carentes",
        "usuario": admin_user
    },
    {
        "nome": "Lar dos Idosos São Vicente",
        "telefone": "(41)3789-0123",
        "cidade": "Curitiba",
        "tipo": "Casa de Repouso",
        "descricao": "Casa de repouso com atendimento humanizado para idosos",
        "usuario": admin_user
    },
    {
        "nome": "Centro de Recuperação Nova Vida",
        "telefone": "(51)3890-1234",
        "cidade": "Porto Alegre",
        "tipo": "Centro de Reabilitação",
        "descricao": "Centro de recuperação para dependentes químicos",
        "usuario": admin_user
    },
    {
        "nome": "Abrigo Patinhas Carentes",
        "telefone": "(61)3901-2345",
        "cidade": "Brasília",
        "tipo": "ONG de Proteção Animal",
        "descricao": "Resgate e cuidado de animais abandonados",
        "usuario": admin_user
    },
    {
        "nome": "Fundação Alimentar Solidário",
        "telefone": "(71)4012-3456",
        "cidade": "Salvador",
        "tipo": "ONG Assistencial",
        "descricao": "Distribuição de alimentos para famílias em situação de pobreza",
        "usuario": admin_user
    },
    {
        "nome": "Hospital Beneficente Santa Maria",
        "telefone": "(81)4123-4567",
        "cidade": "Recife",
        "tipo": "Hospital Filantrópico",
        "descricao": "Atendimento hospitalar gratuito para a comunidade carente",
        "usuario": admin_user
    },
    {
        "nome": "Projeto Educação para Todos",
        "telefone": "(85)4234-5678",
        "cidade": "Fortaleza",
        "tipo": "ONG Educacional",
        "descricao": "Reforço escolar e cursos profissionalizantes gratuitos",
        "usuario": admin_user
    },
    {
        "nome": "Casa de Apoio às Mulheres",
        "telefone": "(91)4345-6789",
        "cidade": "Belém",
        "tipo": "Abrigo",
        "descricao": "Acolhimento e apoio jurídico para mulheres vítimas de violência",
        "usuario": admin_user
    },
]

instituicoes = []
for data in instituicoes_data:
    instituicao = Instituicao(**data)
    instituicao.save()
    instituicoes.append(instituicao)

print(f"✓ {len(instituicoes)} instituições criadas")

# Criar Doações
print("\nCriando doações...")
tipos_disponiveis = ["1", "2", "3"]  # Dinheiro, Roupa, Alimento
doacoes = []

for i in range(15):
    data_doacao = datetime.now() - timedelta(days=i*5)
    doacao = Doacao(
        tipo=tipos_disponiveis[i % 3],
        quantidade=Decimal(str(50 + (i * 10))),
        data=data_doacao,
        doador=doadores[i % len(doadores)],
        instituicao=instituicoes[i % len(instituicoes)],
        status=status_list[i % len(status_list)],
        usuario=doadores[i % len(doadores)].usuario
    )
    doacao.save()
    doacoes.append(doacao)

print(f"✓ {len(doacoes)} doações criadas")

# Criar Histórias Inspiradoras
print("\nCriando histórias inspiradoras...")
historias_data = [
    {
        "titulo": "Uma Nova Chance de Vida",
        "conteudo": "Após receber doações de alimentos e roupas, nossa família conseguiu superar um momento muito difícil. A solidariedade das pessoas nos deu forças para continuar lutando. Hoje, minha filha está bem alimentada e frequentando a escola com uniforme novo. Gratidão eterna!",
        "autor": "Maria Santos",
        "doador": doadores[1],
        "usuario": usuarios[1]
    },
    {
        "titulo": "O Poder da Educação",
        "conteudo": "Graças ao Projeto Educação para Todos, consegui concluir meus estudos e hoje sou formado em Administração. As doações que recebemos possibilitaram que eu tivesse material escolar e pudesse me dedicar aos estudos. Hoje ajudo outras crianças a terem a mesma oportunidade.",
        "autor": "Lucas Ferreira",
        "instituicao": instituicoes[8],
        "usuario": usuarios[8]
    },
    {
        "titulo": "Salvando Vidas de Animais",
        "conteudo": "Como voluntária do Abrigo Patinhas Carentes, vi de perto o impacto das doações. Com a ajuda de nossos doadores, conseguimos resgatar mais de 50 animais este ano, todos tratados, vacinados e adotados por famílias amorosas. Cada contribuição salva uma vida!",
        "autor": "Juliana Lima",
        "instituicao": instituicoes[5],
        "usuario": usuarios[5]
    },
    {
        "titulo": "Transformando a Terceira Idade",
        "conteudo": "O Lar dos Idosos São Vicente transformou completamente a vida do meu pai. As doações permitiram que a instituição oferecesse atividades recreativas, alimentação de qualidade e cuidados médicos. Ver meu pai feliz e bem cuidado não tem preço!",
        "autor": "Patricia Alves",
        "instituicao": instituicoes[3],
        "usuario": usuarios[7]
    },
    {
        "titulo": "Reconstruindo Sonhos",
        "conteudo": "Depois de perder tudo em um incêndio, não sabia como recomeçar. A Casa de Apoio Esperança nos acolheu e, graças às doações, conseguimos reconstruir nossa vida. Hoje tenho um novo emprego e meus filhos voltaram a sorrir. A solidariedade move montanhas!",
        "autor": "Carlos Mendes",
        "instituicao": instituicoes[0],
        "usuario": usuarios[4]
    },
    {
        "titulo": "Vencendo o Vício",
        "conteudo": "O Centro de Recuperação Nova Vida me deu a oportunidade de recomeçar. As doações garantem que pessoas como eu tenham acesso a tratamento de qualidade. Hoje estou há 2 anos limpo, trabalhando e cuidando da minha família. Obrigado a todos que acreditaram em mim!",
        "autor": "Rafael Souza",
        "instituicao": instituicoes[4],
        "usuario": usuarios[6]
    },
    {
        "titulo": "Segurança e Dignidade",
        "conteudo": "A Casa de Apoio às Mulheres me salvou. Consegui sair de um relacionamento abusivo e reconstruir minha vida com dignidade. As doações possibilitam que mulheres como eu tenham um lugar seguro para recomeçar. Hoje sou independente e meus filhos crescem em um ambiente saudável.",
        "autor": "Fernanda Rocha",
        "instituicao": instituicoes[9],
        "usuario": usuarios[9]
    },
    {
        "titulo": "Alimentando Esperança",
        "conteudo": "A Fundação Alimentar Solidário chegou em nossa comunidade no momento certo. Centenas de famílias foram beneficiadas com cestas básicas. Vi crianças que estavam passando fome voltarem a sorrir. Doar é plantar sementes de esperança!",
        "autor": "João Silva",
        "instituicao": instituicoes[6],
        "usuario": usuarios[0]
    },
    {
        "titulo": "Saúde Acessível para Todos",
        "conteudo": "Quando minha mãe ficou doente, não tínhamos condições de pagar um hospital particular. O Hospital Beneficente Santa Maria a tratou com excelência, sem cobrar nada. As doações mantêm essa instituição funcionando e salvando vidas. Minha mãe está curada graças a vocês!",
        "autor": "Ana Oliveira",
        "instituicao": instituicoes[7],
        "usuario": usuarios[3]
    },
    {
        "titulo": "Preservando Nosso Planeta",
        "conteudo": "A ONG Amigos da Natureza realiza um trabalho incrível de educação ambiental. Com as doações, conseguimos plantar mais de 1000 árvores e limpar praias. Ver crianças aprendendo a cuidar do meio ambiente me enche de esperança no futuro. Juntos somos mais fortes!",
        "autor": "Pedro Costa",
        "instituicao": instituicoes[1],
        "usuario": usuarios[2]
    },
]

historias = []
for i, data in enumerate(historias_data):
    historia = Historia_Inspiradoras(**data)
    historia.save()
    historias.append(historia)

print(f"✓ {len(historias)} histórias inspiradoras criadas")

# Resumo
print("\n" + "="*60)
print("RESUMO DA POPULAÇÃO DO BANCO DE DADOS")
print("="*60)
print(f"Usuários: {User.objects.count()}")
print(f"Doadores: {Doador.objects.count()}")
print(f"Instituições: {Instituicao.objects.count()}")
print(f"Status: {Status.objects.count()}")
print(f"Doações: {Doacao.objects.count()}")
print(f"Histórias: {Historia_Inspiradoras.objects.count()}")
print("="*60)
print("\n✅ Banco de dados populado com sucesso!")
print("\nCredenciais de acesso:")
print("  Admin: admin / admin123")
print("  Usuários: joao, maria, pedro, etc / senha123")
