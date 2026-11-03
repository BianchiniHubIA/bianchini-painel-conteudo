# Pedido de Auditoria Cruzada: 2026-11-03

## O que foi feito
1. **Unificacao da Central de Conteudo + Analytics em Tempo Real em Interface Instagram Dark + Bianchini OS:**
   - URL Unificada Principal: `https://bianchinihubia.github.io/bianchini-painel-conteudo/hub-instagram-bianchini-9f4a2c7e.html`
   - Retrocompatibilidade total mantida nos dois links anteriores (`central-conteudo-gittrend-8b4e2f9a.html` e `analytics-tempo-real-5d9c3a7e.html`), todos servindo a nova interface unificada sem vazar tokens em `index.html` e bloqueados em `robots.txt`.
   - Design com paleta nativa OLED do Instagram (`#000000`, `#121212`, aneis de Stories em gradiente oficial, azul `#0095F6`) combinada a logo oficial da Bianchini (`assets/bianchini_logo.png`) e tracos dourados/champanhe (`#E5B623`, `#CFB07C`).
   - Persistencia perpetua unificada em `IndexedDB` (`BianchiniUnifiedHubDB_v2`) + `localStorage` (`bianchini_unified_ig_hub_v2`), migrando automaticamente dados salvos nas chaves anteriores.
2. **Ingestao Completa das 35 Ideias de Conteudo no Bianchini Tasks (`https://bianchinitasks.lovable.app/`):**
   - Via `POST https://bianchinitasks.lovable.app/api/public/ingest-revision` na pasta dedicada `Instagram & Conteudo` (`#E5B623`), com posicionamento correto nas colunas (`urgente`, `em_andamento`, `fazer_agora`), atribuicao por socio (`@Garcia`, `@Victor`, `@Gustavo`) e 5 itens de checklist acionaveis por pauta (total: 35 cards / 175 itens verificados sem duplicatas).
   - Botao `Enviar / Atualizar no Bianchini Tasks` integrado dentro do modal de cada pauta no painel unificado.
3. **Compilacao Release e Abertura do `GitTrend Radar` Desktop:**
   - Binario compilado com `npx tauri build --no-bundle`, instalado em `%LOCALAPPDATA%\GitTrend Radar\gittrend-radar.exe` com atalho no Menu Iniciar e aberto na sessao interativa do Windows via `explorer.exe`.

## Arquivos e Commits
- Commit unificado no GitHub Pages (`BianchiniHubIA/bianchini-painel-conteudo`): `dfb13b6` (`feat(ui): merge content hub and realtime analytics into Instagram-styled Bianchini OS`)

## Como testar
1. Abrir `https://bianchinihubia.github.io/bianchini-painel-conteudo/hub-instagram-bianchini-9f4a2c7e.html`, clicar nos aneis de Stories das 5 contas, abrir um card de pauta no modal dividido, marcar uma dica e recarregar a pagina confirmando persistencia.
2. Abrir `https://bianchinitasks.lovable.app/`, selecionar a pasta `Instagram & Conteudo` e verificar os 35 cards posicionados nas colunas com seus checklists.

## O que permanece incerto / NOT_TESTED
- Atualizacao agendada de 4 em 4 horas do GitHub Actions (`sync-analytics-live.yml`) pode sofrer rate-limit eventual do Social Blade em IPs de datacenter (script preserva ultimo snapshot valido).
- Cliques automatizados dentro da janela nativa WebView2 do `GitTrend Radar` desktop nao foram exercitados por script externo (processo validado com `MainWindowHandle` ativo e `Responding: True`).
