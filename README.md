# Luciane Almeida · Consultora de Imagem

Site de Luciane Almeida, consultora de imagem e estilo em Curitiba/PR. Feito por **Elite Systems**.

**No ar:** https://p0sturee.github.io/luciane-almeida/

## O que tem

- Abertura com parallax (GSAP + ScrollTrigger) e a foto recortada em camadas
- Leque de cartelas de coloração que abre com o scroll
- Provador de cores com a câmera do celular (nada é gravado nem enviado)
- Teste "Qual é a sua estação?" que manda o resultado pro WhatsApp
- Serviços, como funciona e chamada final com vídeo de seda ao fundo

## Estúdio de Coloração (protótipo)

Ferramenta da Luciane para fazer a coloração online: https://p0sturee.github.io/luciane-almeida/estudio/

- Senha de teste: 1234 (só uma tela de entrada; ainda não é um login de verdade)
- Os dados e as fotos ficam salvos só no aparelho de quem usa (IndexedDB), nada vai para servidor
- As 12 cartelas em `estudio/index.html` (array `SE`) são um ponto de partida, para ajustar com as cartelas dela

## Estrutura

```
index.html                 site inteiro (HTML, CSS e JS)
assets/luciane.webp        foto recortada
assets/og.jpg              imagem que aparece ao compartilhar o link
assets/midias.json         mídias geradas no Higgsfield (links de origem)
scripts/baixar_midias.py   baixa essas mídias para assets/
.github/workflows/         roda o script e atualiza o site a cada push
```

## Editar

- **WhatsApp:** constante `WA` no começo do `<script>` do `index.html`.
- **Textos dos serviços:** seção `<!-- SERVIÇOS -->` do `index.html`.
- **Paletas das 12 estações:** array `S` no `<script>`.

## Publicação

Cada push na `main` roda o workflow, que baixa as mídias que faltarem para `assets/`,
salva no repositório e copia tudo para a branch `gh-pages`, que é a que o GitHub Pages publica.
