# Pedido de Auditoria Cruzada: 2026-11-03

## O que foi feito
- Publicacao de 2 aplicacoes `.html` nao-listadas (acessiveis apenas com o link `.html` exato, bloqueadas de indexacao via `robots.txt` e meta `noindex, nofollow, noarchive` e sem link em `index.html`):
  1. `central-conteudo-gittrend-8b4e2f9a.html`: Central interativa em Vue 3 com as 35 pautas das 5 contas, radar GitTrend Nov/2026, estimativas de engajamento, estilos de edicao, ferramentas e guias `VSCode + Claude Code + MCPs / APIs` vs `Producao Manual`, com auto-save em `IndexedDB` + `localStorage` e modo Teleprompter.
  2. `analytics-tempo-real-5d9c3a7e.html`: Painel separado em tempo real de analytics das 5 contas (`@lorenzogarcia.ia`, `@victorbianchini.ia`, `@gustavocalheiros.ia`, `@bianchini.hub`, `@isabianchini.ia`) com persistencia perpetua de snapshots em `IndexedDB` + `localStorage`, auto-refresh do feed JSON, sonda live Social Blade via proxy CORS e diagnostico de Altas, Baixas e Dicas.
- Script `scripts/sync_socialblade_live.py` + workflow `.github/workflows/sync-analytics-live.yml` para atualizar `data/analytics-live-5d9c3a7e.json` a cada 4 horas.

## Arquivos e Commits
- Commit principal: `6a44a95` (`feat(sites): publish unlisted content-os gittrend hub and realtime 5-account analytics`)

## Como testar
1. Acessar `https://bianchinihubia.github.io/bianchini-painel-conteudo/central-conteudo-gittrend-8b4e2f9a.html` e editar uma etapa de pauta; recarregar a pagina e confirmar persistencia.
2. Acessar `https://bianchinihubia.github.io/bianchini-painel-conteudo/analytics-tempo-real-5d9c3a7e.html`, alternar entre as 5 contas, marcar uma dica e recarregar confirmando que o historico permanece salvo.
3. Confirmar que `index.html` nao referencia nenhum dos dois nomes de arquivo.

## O que permanece incerto / NOT_TESTED
- A execucao agendada do GitHub Actions (`sync-analytics-live.yml`) pode sofrer rate-limit/Cloudflare eventual do Social Blade em IPs de datacenter; o script preserva os ultimos valores validos caso receba bloqueio.
- Sonda CORS do navegador (`api.allorigins.win`) depende de disponibilidade de servico publico terceiro; quando indisponivel, o painel usa `data/analytics-live-5d9c3a7e.json` sem falhar.
