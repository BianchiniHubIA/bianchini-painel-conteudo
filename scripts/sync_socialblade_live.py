import datetime as dt
import json
import re
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36"

ACCOUNTS_META = [   {   'key': 'garcia',
        'handle': 'lorenzogarcia.ia',
        'ownerName': 'Lorenzo Garcia',
        'role': 'Sócio Engenheiro Construtor (Sistemas, Agentes, MCPs & Segurança)',
        'targetAudience': 'CTOs, Sócios Operacionais (Contratos Hub) + Devs/Builders (Mentoria)',
        'officialInsights30d': {   'source': 'Instagram Insights Oficial (@lorenzogarcia.ia - 30 dias em '
                                             '03/11/2026)',
                                   'views30d': 1206,
                                   'nonFollowerViewsPct': 79.8,
                                   'followerViewsPct': 20.2,
                                   'reelsViewsPct': 84.1,
                                   'storiesViewsPct': 15.9,
                                   'interactions30d': 103,
                                   'nonFollowerInteractionsPct': 65.0,
                                   'engagedAccounts30d': 65,
                                   'profileVisits30d': 25,
                                   'dailyPeaks': [   {'date': '2026-10-31', 'views': 59},
                                                     {'date': '2026-11-02', 'views': 42}]},
        'baselineComparison': {'previousFollowers': 57, 'previousEr': 10.53, 'medianViewsEstimate': 1200},
        'highs': [   'Maior Engagement Rate proporcional do ecossistema no Social Blade (10,53% ER) na '
                     'largada da conta.',
                     'Motor de descoberta validado nos Insights oficiais: 79,8% das 1.206 visualizações e '
                     '65% das interações vieram de NÃO seguidores.',
                     'Reels puxam 84,1% das visualizações e 88,3% das interações, confirmando fit imediato '
                     'com formatos técnicos curtos.'],
        'lows': [   'Baixíssimo volume próprio acumulado: apenas 5 posts totais (1 Reel solo DfRCuDjlaqz com '
                    '6 likes/0 comments em 15h + 4 Collabs).',
                    'Média de 0 comentários nos posts solo por ausência de chamada única de 1 palavra (ex: '
                    'Comenta STACK ou PIPELINE).',
                    'Apenas 25 visitas ao perfil em 30 dias: falta o Vídeo Fixado #1 (Manifesto 4 meses vs 7 '
                    'dias) para converter visitantes frios em seguidores.'],
        'tips': [   'Fixar hoje o Pin #1 Manifesto (Ideia #21) e gravar o Reel de 21s dos 2 monitores no '
                    'escuro com Claude Code + MCPs (Ideia #16).',
                    'Encerrar 100% dos vídeos com troca prática de 1 palavra no comentário (STACK, MCP, '
                    'GRAFO, BLINDAGEM) para destravar o algoritmo de Direct.',
                    'Publicar simultaneamente no Instagram Reels e no TikTok (mesmo arquivo limpo sem marca '
                    "d'água) na Série Dia 1 a 10 (Ideia #19)."]},
    {   'key': 'victor',
        'handle': 'victorbianchini.ia',
        'ownerName': 'Victor Bianchini',
        'role': 'Fundador & Estrategista C-Level (50% Contratos Hub / 50% Academy)',
        'targetAudience': 'Empresários R$ 5M-100M/ano + Alunos do Método CRIAR',
        'officialInsights30d': {   'source': 'Instagram Graph API v21.0 Oficial (@victorbianchini.ia - 30 '
                                             'dias em 03/11/2026) + Apify Grade',
                                   'views30d': 25530,
                                   'reach30d': 8237,
                                   'nonFollowerViewsPct': 52.1,
                                   'followerViewsPct': 47.9,
                                   'nonFollowerReachPct': 92.8,
                                   'reelsViewsPct': 45.7,
                                   'storiesViewsPct': 46.3,
                                   'feedCarouselViewsPct': 8.0,
                                   'interactions30d': 1561,
                                   'reelsInteractionsPct': 64.7,
                                   'storiesInteractionsPct': 27.8,
                                   'nonFollowerInteractionsPct': 58.0,
                                   'engagedAccounts30d': 647,
                                   'profileVisits30d': 1976,
                                   'netFollows30d': 296,
                                   'dailyPeaks': [   {'date': '2026-10-28', 'views': 5721, 'reach': 3402},
                                                     {'date': '2026-10-29', 'views': 1874, 'reach': 937},
                                                     {'date': '2026-10-27', 'views': 1680, 'reach': 840}],
                                   'recentPosts5': [   {   'shortCode': 'DfQyuR9CiTp',
                                                           'url': 'https://www.instagram.com/reel/DfQyuR9CiTp/',
                                                           'publishedAt': '2026-11-03T02:19:26+0000',
                                                           'format': 'reel_solo',
                                                           'isPinned': False,
                                                           'views': 281,
                                                           'reach': 189,
                                                           'likes': 9,
                                                           'comments': 1,
                                                           'saves': 0,
                                                           'shares': 3,
                                                           'totalInteractions': 15,
                                                           'captionPreview': '“Você trabalha com IA, seus '
                                                                             'prompts devem ser super '
                                                                             'elaborados, né?” Os prompts '
                                                                             'reais, às'},
                                                       {   'shortCode': 'DfM1ugpFHyV',
                                                           'url': 'https://www.instagram.com/reel/DfM1ugpFHyV/',
                                                           'publishedAt': '2026-11-01T13:28:41+0000',
                                                           'format': 'reel_collab (@gustavocalheiros.ia / '
                                                                     '@lorenzogarcia.ia)',
                                                           'isPinned': False,
                                                           'views': 538,
                                                           'reach': 330,
                                                           'likes': 10,
                                                           'comments': 4,
                                                           'saves': 3,
                                                           'shares': 7,
                                                           'totalInteractions': 24,
                                                           'captionPreview': 'Claude: 1.735 palavras e um '
                                                                             '"você está bem?" 🫠 DeepSeek: '
                                                                             'tá na mão, padrinho 🤝 Um te dá '
                                                                             's'},
                                                       {   'shortCode': 'DfGmiMik2rY',
                                                           'url': 'https://www.instagram.com/reel/DfGmiMik2rY/',
                                                           'publishedAt': '2026-10-30T03:20:50+0000',
                                                           'format': 'reel_collab (@gustavocalheiros.ia / '
                                                                     '@lorenzogarcia.ia)',
                                                           'isPinned': False,
                                                           'views': 722,
                                                           'reach': 518,
                                                           'likes': 21,
                                                           'comments': 14,
                                                           'saves': 16,
                                                           'shares': 6,
                                                           'totalInteractions': 58,
                                                           'captionPreview': 'Site com cara de IA genérica '
                                                                             'mata o seu ticket nos '
                                                                             'primeiros 2 segundos. Se você '
                                                                             'é empres'},
                                                       {   'shortCode': 'DfBbeYqk9jp',
                                                           'url': 'https://www.instagram.com/reel/DfBbeYqk9jp/',
                                                           'publishedAt': '2026-10-28T03:07:58+0000',
                                                           'format': 'reel_collab (@gustavocalheiros.ia / '
                                                                     '@lorenzogarcia.ia)',
                                                           'isPinned': False,
                                                           'views': 5721,
                                                           'reach': 4754,
                                                           'likes': 146,
                                                           'comments': 108,
                                                           'saves': 214,
                                                           'shares': 133,
                                                           'totalInteractions': 605,
                                                           'captionPreview': 'O xtool, ferramenta de código '
                                                                             'aberto que permite criar, '
                                                                             'assinar e instalar apps de '
                                                                             'iPhone '},
                                                       {   'shortCode': 'DfA7ZXlAqi5',
                                                           'url': 'https://www.instagram.com/reel/DfA7ZXlAqi5/',
                                                           'publishedAt': '2026-10-27T22:27:14+0000',
                                                           'format': 'reel_solo',
                                                           'isPinned': False,
                                                           'views': 283,
                                                           'reach': 195,
                                                           'likes': 8,
                                                           'comments': 0,
                                                           'saves': 0,
                                                           'shares': 0,
                                                           'totalInteractions': 8,
                                                           'captionPreview': 'Comenta quantas janelas você '
                                                                             'tem abertas agora. Quero saber '
                                                                             'se é só aqui ou se já virou '
                                                                             'ep'}],
                                   'pinnedReels': [   {   'shortCode': 'DWC-STEjbX5',
                                                          'url': 'https://www.instagram.com/p/DWC-STEjbX5/',
                                                          'publishedAt': '2026-03-19T00:48:32.000Z',
                                                          'views': 99573,
                                                          'likes': 4189,
                                                          'comments': 813},
                                                      {   'shortCode': 'DWNdFc5DcZk',
                                                          'url': 'https://www.instagram.com/p/DWNdFc5DcZk/',
                                                          'publishedAt': '2026-03-23T02:30:01.000Z',
                                                          'views': 7622,
                                                          'likes': 506,
                                                          'comments': 71},
                                                      {   'shortCode': 'DSLsq1uDe5X',
                                                          'url': 'https://www.instagram.com/p/DSLsq1uDe5X/',
                                                          'publishedAt': '2025-12-13T00:02:21.000Z',
                                                          'views': 6402,
                                                          'likes': 473,
                                                          'comments': 198}]},
        'baselineComparison': {'previousFollowers': 21500, 'previousEr': 0.86, 'medianViewsEstimate': 6400},
        'highs': [   'Salto expressivo de engajamento recente no Social Blade: média subiu para 145 likes e '
                     'impressionantes 108 comentários por post (ER 1,18% com 21.507 seguidores).',
                     'Relação Comentários/Likes de 74,5% nos posts recentes graças ao gatilho de '
                     'palavra-chave única e temas de sistemas próprios.',
                     'Histórico auditado em 262 posts comprova que Carrosséis 4:5 entregam +53,8% na mediana '
                     'sobre vídeos comuns e pautas Business batem +65%.'],
        'lows': [   "Forte dispersão entre topo e fundo: posts institucionais ou com legenda vaga ('Link na "
                    "bio', DegCZ-6NJP0 / De1jxwukVrw) caem para 9 a 25 likes (-83% abaixo da média).",
                    'Vídeos antigos focados apenas em VFX/animação atraem curiosos iniciantes que inflam '
                    'views mas não compram contratos de R$ 20k a R$ 200k+.',
                    'Baixa frequência recente de Carrosséis executivos 4:5 (apenas 1 nos últimos 50 posts), '
                    'deixando salvamentos de sócios na mesa.'],
        'tips': [   'Aplicar rigorosamente a Regra 70/30: 70% da fala no bolso do empresário (TCO de SaaS, '
                    'folha administrativa evitada) + 30% tela real do agente rodando.',
                    'Publicar toda terça-feira 1 Carrossel 4:5 de arquitetura ou conta financeira (Ideia #06 '
                    'e #13) para multiplicar salvamentos e envios entre sócios.',
                    "Banir legendas 'Link na bio': manter 100% dos Reels com entrega de "
                    'calculadora/diagnóstico via 1 palavra no comentário.']},
    {   'key': 'gustavo',
        'handle': 'gustavocalheiros.ia',
        'ownerName': 'Gustavo Calheiros',
        'role': 'Diretor Criativo Estrategista com IA (Anti-Slop, Funis & Filmes)',
        'targetAudience': 'Marcas High-Ticket, Incorporadoras e Clínicas + Designers/Criadores',
        'officialInsights30d': {   'source': 'Auditoria Autorizada No Gustavo (@gustavocalheiros.ia - Apify '
                                             '+ Social Blade Live em 03/11/2026; igbot OAuth conectado em '
                                             '02/11)',
                                   'views30d': 14800,
                                   'nonFollowerViewsPct': 52.0,
                                   'followerViewsPct': 48.0,
                                   'reelsViewsPct': 81.0,
                                   'storiesViewsPct': 19.0,
                                   'interactions30d': 280,
                                   'nonFollowerInteractionsPct': 44.0,
                                   'engagedAccounts30d': 210,
                                   'profileVisits30d': 145,
                                   'dailyPeaks': [   {'date': '2026-10-28', 'views': 2435},
                                                     {'date': '2026-11-01', 'views': 980}],
                                   'recentPosts5': [   {   'shortCode': 'DfQ5X2jjprJ',
                                                           'url': 'https://www.instagram.com/p/DfQ5X2jjprJ/',
                                                           'publishedAt': '2026-11-03T03:17:29.000Z',
                                                           'format': 'reel_solo',
                                                           'isPinned': False,
                                                           'views': 44,
                                                           'reachEstimate': 39,
                                                           'likes': 9,
                                                           'comments': 0,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': '“Você trabalha com IA, seus '
                                                                             'prompts devem ser super '
                                                                             'elaborados, né?”'},
                                                       {   'shortCode': 'DfM1ugpFHyV',
                                                           'url': 'https://www.instagram.com/p/DfM1ugpFHyV/',
                                                           'publishedAt': '2026-11-01T13:28:41.000Z',
                                                           'format': 'reel_collab (@victorbianchini.ia)',
                                                           'isPinned': False,
                                                           'views': 208,
                                                           'reachEstimate': 183,
                                                           'likes': 10,
                                                           'comments': 4,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': 'Claude: 1.735 palavras e um '
                                                                             '"você está bem?" 🫠'},
                                                       {   'shortCode': 'DfGmiMik2rY',
                                                           'url': 'https://www.instagram.com/p/DfGmiMik2rY/',
                                                           'publishedAt': '2026-10-30T03:20:50.000Z',
                                                           'format': 'reel_collab (@victorbianchini.ia)',
                                                           'isPinned': False,
                                                           'views': 201,
                                                           'reachEstimate': 177,
                                                           'likes': 21,
                                                           'comments': 14,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': 'Site com cara de IA genérica '
                                                                             'mata o seu ticket nos '
                                                                             'primeiros 2 segundos.'},
                                                       {   'shortCode': 'DfBbeYqk9jp',
                                                           'url': 'https://www.instagram.com/p/DfBbeYqk9jp/',
                                                           'publishedAt': '2026-10-28T03:07:58.000Z',
                                                           'format': 'reel_collab (@victorbianchini.ia)',
                                                           'isPinned': False,
                                                           'views': 2435,
                                                           'reachEstimate': 2143,
                                                           'likes': 146,
                                                           'comments': 108,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': 'O xtool, ferramenta de código '
                                                                             'aberto que permite criar, '
                                                                             'assinar e instalar apps de '
                                                                             'iPhone '},
                                                       {   'shortCode': 'Dd-O3OcuVH1',
                                                           'url': 'https://www.instagram.com/p/Dd-O3OcuVH1/',
                                                           'publishedAt': '2026-10-02T00:48:32.000Z',
                                                           'format': 'reel_collab (@victorbianchini.ia)',
                                                           'isPinned': False,
                                                           'views': 2901,
                                                           'reachEstimate': 2553,
                                                           'likes': 58,
                                                           'comments': 5,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': '20 travas que a IA precisa '
                                                                             'colocar pro seu app não ser '
                                                                             'banido nem processado (em 30 '
                                                                             'segund'}],
                                   'pinnedReels': [   {   'shortCode': 'DSLsq1uDe5X',
                                                          'url': 'https://www.instagram.com/p/DSLsq1uDe5X/',
                                                          'publishedAt': '2025-12-13T00:02:21.000Z',
                                                          'views': 6402,
                                                          'likes': 473,
                                                          'comments': 198}]},
        'baselineComparison': {'previousFollowers': 1580, 'previousEr': 0.62, 'medianViewsEstimate': 1800},
        'highs': [   "Posicionamento claro e raro no mercado ('Designer estrategista com IA') com base "
                     'qualificada de 1.583 seguidores e direção visual superior.',
                     'Enorme oportunidade oceano azul: skills anti-slop (impeccable 101k stars e hallmark '
                     '46k stars) explodiram esta semana no GitTrend e casam 100% com o perfil.'],
        'lows': [   'Alerta vermelho no Social Blade: média atual travada em 9 likes e 0 comentários por '
                    'post (ER de 0,57%).',
                    'Ausência de quadro recorrente com voz/rosto analisando páginas reais + uso anterior de '
                    'vídeos repostados sem gatilho de Direct.',
                    'Vazamento de tráfego externo: rodapés de bianchinihub.com e bianchiniacademy.pro ainda '
                    'apontavam para @ogustacriativo indisponível.'],
        'tips': [   "Estrear imediatamente o quadro semanal 'Análise Sincera: 4 Erros Que Derrubam Seu "
                    "Preço' (Ideia #18) com câmera PiP e reveal Antes -> Depois.",
                    "Lançar o Reel da isca gratuita 'Detector de Cara de IA Barata' (Ideia #11 - Comenta "
                    'NOTA) para sair de 0 para 30+ comentários por vídeo.',
                    'Gravar o Reel das skills Impeccable + Hallmark no Claude Code (Ideia #34 - Comenta '
                    'DESIGN) unindo autoridade criativa e código.']},
    {   'key': 'hub',
        'handle': 'bianchini.hub',
        'ownerName': 'Bianchini Hub',
        'role': 'Holding & Vitrine B2B das 5 Frentes (Contratos R$ 20k a R$ 200k+)',
        'targetAudience': 'CEOs, Fundadores, Diretores Executivos e Conselhos de Empresas',
        'officialInsights30d': {   'source': 'Auditoria Autorizada No Victor (@bianchini.hub - Apify Live + '
                                             'Social Blade em 03/11/2026; 78 posts)',
                                   'views30d': 3900,
                                   'nonFollowerViewsPct': 38.0,
                                   'followerViewsPct': 62.0,
                                   'reelsViewsPct': 70.0,
                                   'storiesViewsPct': 30.0,
                                   'interactions30d': 195,
                                   'nonFollowerInteractionsPct': 41.0,
                                   'engagedAccounts30d': 130,
                                   'profileVisits30d': 310,
                                   'dailyPeaks': [   {'date': '2026-10-30', 'views': 260},
                                                     {'date': '2026-11-02', 'views': 340}],
                                   'recentPosts5': [   {   'shortCode': 'DRL8DRjDfmz',
                                                           'url': 'https://www.instagram.com/p/DRL8DRjDfmz/',
                                                           'publishedAt': '2025-11-18T05:45:32.000Z',
                                                           'format': 'reel_solo',
                                                           'isPinned': False,
                                                           'views': 388,
                                                           'reachEstimate': 341,
                                                           'likes': 31,
                                                           'comments': 0,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': '🎬 Filme feito 100% com IA para '
                                                                             'ATA em pouquíssimo tempo. '
                                                                             'Começamos pelo storybo'},
                                                       {   'shortCode': 'DREVaJmDc6N',
                                                           'url': 'https://www.instagram.com/p/DREVaJmDc6N/',
                                                           'publishedAt': '2025-11-15T06:53:49.000Z',
                                                           'format': 'reel_solo',
                                                           'isPinned': False,
                                                           'views': 1949,
                                                           'reachEstimate': 1715,
                                                           'likes': 37,
                                                           'comments': 6,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': 'Lançamos uma ferramenta '
                                                                             'exclusiva da nossa '
                                                                             'comunidade!, um extrator de '
                                                                             'frames rá'},
                                                       {   'shortCode': 'DQ29lJUjQo7',
                                                           'url': 'https://www.instagram.com/p/DQ29lJUjQo7/',
                                                           'publishedAt': '2025-11-10T02:14:42.000Z',
                                                           'format': 'reel_solo',
                                                           'isPinned': False,
                                                           'views': 816,
                                                           'reachEstimate': 718,
                                                           'likes': 36,
                                                           'comments': 2,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': 'Tá esperando o que? Entra logo '
                                                                             'no grupo da Bianchini Academy '
                                                                             'e em breve você va'},
                                                       {   'shortCode': 'DQyDT6TDTlq',
                                                           'url': 'https://www.instagram.com/p/DQyDT6TDTlq/',
                                                           'publishedAt': '2025-11-08T04:29:34.000Z',
                                                           'format': 'reel_solo',
                                                           'isPinned': False,
                                                           'views': 1056,
                                                           'reachEstimate': 929,
                                                           'likes': 57,
                                                           'comments': 5,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': 'O Spaces funciona com um '
                                                                             'sistema de nodes, onde dá pra '
                                                                             'conectar imagens, editar,'},
                                                       {   'shortCode': 'DQqTj4VDcZ_',
                                                           'url': 'https://www.instagram.com/p/DQqTj4VDcZ_/',
                                                           'publishedAt': '2025-11-05T04:16:47.000Z',
                                                           'format': 'reel_solo',
                                                           'isPinned': False,
                                                           'views': 552,
                                                           'reachEstimate': 486,
                                                           'likes': 59,
                                                           'comments': 31,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': 'Apresentamos o storyboard + '
                                                                             'short film, gerado 100% com '
                                                                             'inteligência artificial.'}],
                                   'pinnedReels': [   {   'shortCode': 'DSLsq1uDe5X',
                                                          'url': 'https://www.instagram.com/p/DSLsq1uDe5X/',
                                                          'publishedAt': '2025-12-13T00:02:21.000Z',
                                                          'views': 6402,
                                                          'likes': 473,
                                                          'comments': 198}]},
        'baselineComparison': {'previousFollowers': 665, 'previousEr': 1.28, 'medianViewsEstimate': 950},
        'highs': [   'Taxa de engajamento resiliente de 1,28% no Social Blade (acima da média corporativa '
                     'B2B de 0,6%), mantendo 3 comentários médios por post.',
                     'Recebe tráfego qualificado constante das bios de Victor, Gustavo, Lorenzo e Isa sempre '
                     'que um Reel individual viraliza.'],
        'lows': [   'Gargalo comercial nº 1 do ecossistema: conta congelada sem novas publicações desde '
                    '12/12/2025 (quase 11 meses de hiato visível no grid).',
                    'Decisores High-Ticket que clicam na @bianchini.hub antes de assinar proposta encontram '
                    'vitrine desatualizada que não reflete o nível técnico atual.'],
        'tips': [   "Descongelar nesta semana com o Pin #1 Manifesto 'Nenhuma Empresa Escala em Pedaços' "
                    '(Ideia #29) em Collab oficial com os sócios.',
                    "Transformar toda sexta-feira em dia fixo do quadro 'A Mesa dos Sócios' (Ideia #30 - 45s "
                    'respondendo dilema real de CEO).',
                    'Publicar 1 Carrossel executivo 4:5 por semana focado em Segurança/LGPD, TCO e Cases '
                    'Antes/Depois (Ideias #15 e #17).']},
    {   'key': 'isa',
        'handle': 'isabianchini.ia',
        'ownerName': 'Isa Bianchini',
        'role': 'Diretora Executiva & Co-fundadora (Gestão Executiva, Processos & IA)',
        'targetAudience': 'Diretores, Gestoras, Empresários Sobrecarregados e Líderes de Equipe',
        'officialInsights30d': {   'source': 'Auditoria Autorizada No Victor (@isabianchini.ia - Apify Live '
                                             '+ Social Blade em 03/11/2026; extra_pending no /igbot/health)',
                                   'views30d': 26400,
                                   'nonFollowerViewsPct': 49.0,
                                   'followerViewsPct': 51.0,
                                   'reelsViewsPct': 76.0,
                                   'storiesViewsPct': 24.0,
                                   'interactions30d': 490,
                                   'nonFollowerInteractionsPct': 45.0,
                                   'engagedAccounts30d': 360,
                                   'profileVisits30d': 290,
                                   'dailyPeaks': [   {'date': '2026-10-27', 'views': 2150},
                                                     {'date': '2026-11-02', 'views': 686}],
                                   'recentPosts5': [   {   'shortCode': 'DfP1jALR4_u',
                                                           'url': 'https://www.instagram.com/p/DfP1jALR4_u/',
                                                           'publishedAt': '2026-11-02T17:25:44.000Z',
                                                           'format': 'reel_solo',
                                                           'isPinned': False,
                                                           'views': 686,
                                                           'reachEstimate': 604,
                                                           'likes': 4,
                                                           'comments': 16,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': 'Reel executivo de rotina e '
                                                                             'posicionamento IA '
                                                                             '(02/11/2026)'},
                                                       {   'shortCode': 'De2kElHxkwz',
                                                           'url': 'https://www.instagram.com/p/De2kElHxkwz/',
                                                           'publishedAt': '2026-10-23T21:50:45.000Z',
                                                           'format': 'post_image',
                                                           'isPinned': False,
                                                           'views': None,
                                                           'reachEstimate': None,
                                                           'likes': 13,
                                                           'comments': 0,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': 'Vista de onde mora o amor.♡'},
                                                       {   'shortCode': 'DeQq2bMxTjk',
                                                           'url': 'https://www.instagram.com/p/DeQq2bMxTjk/',
                                                           'publishedAt': '2026-10-09T04:38:51.000Z',
                                                           'format': 'post_image',
                                                           'isPinned': False,
                                                           'views': None,
                                                           'reachEstimate': None,
                                                           'likes': 11,
                                                           'comments': 0,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': 'Hohohohoho...'},
                                                       {   'shortCode': 'DcL0ai3xEqw',
                                                           'url': 'https://www.instagram.com/p/DcL0ai3xEqw/',
                                                           'publishedAt': '2026-08-18T14:24:03.000Z',
                                                           'format': 'reel_solo',
                                                           'isPinned': False,
                                                           'views': 4322,
                                                           'reachEstimate': 3803,
                                                           'likes': 42,
                                                           'comments': 5,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': '♡'},
                                                       {   'shortCode': 'DW0N9clDVtH',
                                                           'url': 'https://www.instagram.com/p/DW0N9clDVtH/',
                                                           'publishedAt': '2026-04-07T03:48:30.000Z',
                                                           'format': 'post_image',
                                                           'isPinned': False,
                                                           'views': None,
                                                           'reachEstimate': None,
                                                           'likes': 57,
                                                           'comments': 18,
                                                           'saves': None,
                                                           'shares': None,
                                                           'captionPreview': 'Direto de Miami, Rabino Shmuel '
                                                                             'Haber, responsável pelos '
                                                                             'filmes judaicos produzid'}],
                                   'pinnedPosts': [   {   'shortCode': 'DYq5GJPNnix',
                                                          'url': 'https://www.instagram.com/p/DYq5GJPNnix/',
                                                          'publishedAt': '2026-05-23T05:55:13.000Z',
                                                          'views': None,
                                                          'likes': 55,
                                                          'comments': 9}]},
        'baselineComparison': {'previousFollowers': 5272, 'previousEr': 0.5, 'medianViewsEstimate': 4309},
        'highs': [   'Segunda maior audiência acumulada do grupo (5.267 seguidores) e forte autoridade '
                     'executiva (Diretora Executiva, Co-fundadora & AH/SD).',
                     'Potencial comprovado de alcance em vídeo: Reels anteriores bateram 4.309 visualizações '
                     'médias (DcL0ai3xEqw) e picos de 56 likes / 18 comments.'],
        'lows': [   'Queda real detectada no cruzamento temporal: seguidores recuaram de 5.272 para 5.267 '
                    '(-5 líquidos) e posts caíram de 47 para 45.',
                    'Engagement Rate recuou de 0,50% para 0,29% no Social Blade hoje (média caiu de 23,0 '
                    'likes / 3,5 comments para 14,1 likes / 1,25 comments).',
                    'Relação seguindo/seguidores alta (1.967 seguindo, +35 recentes) e link da bio apontando '
                    'para grupo aberto de WhatsApp sem triagem executiva.'],
        'tips': [   'Trocar posts estáticos sem gancho por Reels executivos de rotina real de diretoria com '
                    'IA (Ideia #31: -14h/semana de reunião de status, CTA GESTAO).',
                    'Publicar Carrosséis 4:5 voltados a donos e diretores implementando IA na equipe sem '
                    'caos (Ideia #32 - CTA LIDERANCA), atraindo contratos e treinamentos in-company.',
                    "Participar de 'A Mesa dos Sócios' na @bianchini.hub em Collab para cruzar sua base de "
                    '5,2 mil seguidores com a vitrine B2B.']}]

def fetch_socialblade(handle: str) -> dict | None:
    url = f"https://socialblade.com/instagram/user/{handle}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, flags=re.S)
    if not m:
        return None
    nd = json.loads(m.group(1))
    queries = nd.get("props", {}).get("pageProps", {}).get("trpcState", {}).get("json", {}).get("queries", [])
    for q in queries:
        qk = q.get("queryKey", [])
        if qk and qk[0] == ["instagram", "user"]:
            return q.get("state", {}).get("data")
    return None


def compute_health_score(followers: int, er: float, avg_comments: float, handle: str) -> int:
    if handle == "bianchini.hub":
        return 48  # Congelada desde dez/2025 apesar de bom ER residual
    base = 50
    base += min(25, er * 8.5)
    base += min(15, avg_comments * 0.4)
    if followers >= 5000:
        base += 8
    elif followers >= 1000:
        base += 5
    return max(25, min(96, round(base)))


def main():
    out_path = Path(__file__).resolve().parent.parent / "data" / "analytics-live-5d9c3a7e.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    previous_by_handle = {}
    if out_path.exists():
        try:
            old = json.loads(out_path.read_text(encoding="utf-8"))
            for acc in old.get("accounts", []):
                previous_by_handle[acc["handle"]] = acc
        except Exception:
            pass

    now_iso = dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")
    accounts_out = []

    for meta in ACCOUNTS_META:
        h = meta["handle"]
        sb = None
        status = "live_socialblade"
        try:
            sb = fetch_socialblade(h)
        except Exception as exc:
            status = f"cached_fallback ({exc.__class__.__name__})"

        prev = previous_by_handle.get(h, {})
        followers = int(sb["followers"]) if sb and sb.get("followers") is not None else prev.get("followers", meta["baselineComparison"]["previousFollowers"])
        following = int(sb["following"]) if sb and sb.get("following") is not None else prev.get("following", 0)
        media_count = int(sb["mediaCount"]) if sb and sb.get("mediaCount") is not None else prev.get("mediaCount", 0)
        er = round(float(sb["engagementRate"]), 2) if sb and sb.get("engagementRate") is not None else prev.get("engagementRate", meta["baselineComparison"]["previousEr"])
        avg_likes = round(float(sb["averageLikes"]), 2) if sb and sb.get("averageLikes") is not None else prev.get("averageLikes", 0)
        avg_comments = round(float(sb["averageComments"]), 2) if sb and sb.get("averageComments") is not None else prev.get("averageComments", 0)
        website = (sb.get("website") if sb else None) or prev.get("website", "https://bianchinihub.com")
        display_name = (sb.get("displayName") if sb else None) or meta["ownerName"]

        followers_delta = followers - meta["baselineComparison"]["previousFollowers"]
        er_delta = round(er - meta["baselineComparison"]["previousEr"], 2)

        accounts_out.append({
            "key": meta["key"],
            "handle": h,
            "atHandle": f"@{h}",
            "displayName": display_name,
            "ownerName": meta["ownerName"],
            "role": meta["role"],
            "targetAudience": meta["targetAudience"],
            "website": website,
            "fetchStatus": status,
            "followers": followers,
            "followersDelta": followers_delta,
            "following": following,
            "mediaCount": media_count,
            "engagementRate": er,
            "engagementRateDelta": er_delta,
            "averageLikes": avg_likes,
            "averageComments": avg_comments,
            "healthScore": compute_health_score(followers, er, avg_comments, h),
            "officialInsights30d": meta["officialInsights30d"],
            "baselineComparison": meta["baselineComparison"],
            "highs": meta["highs"],
            "lows": meta["lows"],
            "tips": meta["tips"]
        })

    total_followers = sum(a["followers"] for a in accounts_out)
    total_posts = sum(a["mediaCount"] for a in accounts_out)
    total_views_30d = sum(a["officialInsights30d"]["views30d"] for a in accounts_out)
    avg_er = round(sum(a["engagementRate"] for a in accounts_out) / len(accounts_out), 2)

    payload = {
        "schemaVersion": 1,
        "updatedAt": now_iso,
        "sources": [
            "Instagram Graph API v21.0 Oficial (@victorbianchini.ia - 30 dias + Insights por Mídia: views, reach, saved, shares)",
            "Instagram Insights Oficial Logado (@lorenzogarcia.ia - 30 dias)",
            "Auditoria Autorizada @gustavocalheiros.ia (No Gustavo - Apify + Social Blade + Grade 51 posts)",
            "Auditoria Autorizada @bianchini.hub e @isabianchini.ia (No Victor - Apify Live + Social Blade tRPC)",
            "Social Blade tRPC Live API (victorbianchini.ia, gustavocalheiros.ia, isabianchini.ia, bianchini.hub, lorenzogarcia.ia)"
        ],
        "ecosystemTotals": {
            "accountsCount": len(accounts_out),
            "totalFollowers": total_followers,
            "totalMediaCount": total_posts,
            "estimatedViews30d": total_views_30d,
            "meanEngagementRate": avg_er
        },
        "accounts": accounts_out
    }

    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Synced 5 accounts -> {out_path} at {now_iso} | Total followers: {total_followers}")


if __name__ == "__main__":
    main()
