import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'    /\* =========================\n       CUSTOMIZAÇÃO DAS SETAS \(MENU SANFONA\).*?margin-left: 0px; \n    }', re.DOTALL)

new_css = """    /* =========================
       CUSTOMIZAÇÃO DAS SETAS (MENU SANFONA)
    ========================= */
    /* Sobrescreve a seta nativa do docsify-sidebar-collapse */
    .sidebar-nav ul:not(.app-sub-sidebar)>li:not(.file)::before {
      content: "▸" !important;
      font-size: 18px !important;
      color: var(--purple-700) !important;
      border: none !important;
      background: transparent !important;
      transform: none !important;
      position: absolute !important;
      top: 0px !important;
      left: -16px !important;
      width: auto !important;
      height: auto !important;
      display: inline-block !important;
    }

    .sidebar-nav ul:not(.app-sub-sidebar)>li.open::before {
      content: "▾" !important;
    }

    /* Alinhamento geral das margens */
    .sidebar-nav ul:not(.app-sub-sidebar) > li {
      position: relative;
    }
    
    /* Arquivos sem seta (ex: IA Generativa) precisam estar na mesma linha */
    .sidebar-nav ul:not(.app-sub-sidebar)>li.file {
      margin-left: 0px !important;
    }"""

new_text = pattern.sub(new_css, text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Substituido com sucesso!")
