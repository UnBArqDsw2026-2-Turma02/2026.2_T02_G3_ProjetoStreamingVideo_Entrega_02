import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'    /\* =========================\n       CUSTOMIZAÇÃO DAS SETAS \(MENU SANFONA\).*?margin-left: 0px !important;\n    }', re.DOTALL)

new_css = """    /* =========================
       CUSTOMIZAÇÃO DAS SETAS (MENU SANFONA)
    ========================= */
    /* Mata a seta nativa (feia) do plugin em absolutamente todos os itens */
    .sidebar-nav ul:not(.app-sub-sidebar)>li::before {
      display: none !important;
      content: none !important;
    }

    /* Recria a seta APENAS nos itens que são pastas (collapse/open) */
    .sidebar-nav ul:not(.app-sub-sidebar)>li.collapse::before, 
    .sidebar-nav ul:not(.app-sub-sidebar)>li.open::before {
      content: "▸" !important;
      display: inline-block !important;
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
    }

    .sidebar-nav ul:not(.app-sub-sidebar)>li.open::before {
      content: "▾" !important;
    }

    /* Alinhamento geral das margens */
    .sidebar-nav ul:not(.app-sub-sidebar) > li {
      position: relative;
    }
    
    /* Arquivos sem seta precisam estar na mesma linha que os com seta */
    .sidebar-nav ul:not(.app-sub-sidebar)>li:not(.collapse):not(.open) {
      margin-left: 0px !important;
    }"""

new_text = pattern.sub(new_css, text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Fix 3 aplicado!")
