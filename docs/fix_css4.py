import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remover tudo que eu adicionei (do comentário inicial até a tag de fechamento)
pattern = re.compile(r'    /\* =========================\n       CUSTOMIZAÇÃO DAS SETAS \(MENU SANFONA\).*?margin-left: 0px !important;\n    }', re.DOTALL)

clean_css = """    /* =========================
       CUSTOMIZAÇÃO DAS SETAS (MENU SANFONA)
    ========================= */
    /* Remove a "borda" feia original do plugin sem quebrar a lógica dele */
    .sidebar-nav ul:not(.app-sub-sidebar)>li:not(.file)::before {
        border: none !important;
        transform: none !important;
        width: auto !important;
        height: auto !important;
    }

    /* Seta para pasta fechada */
    .sidebar-nav ul:not(.app-sub-sidebar)>li.collapse:not(.file)::before {
        content: "▸" !important;
        font-size: 18px !important;
        color: var(--purple-700) !important;
        position: absolute;
        left: -14px;
        top: 2px;
    }

    /* Seta para pasta aberta */
    .sidebar-nav ul:not(.app-sub-sidebar)>li.open:not(.file)::before {
        content: "▾" !important;
        font-size: 18px !important;
        color: var(--purple-700) !important;
        position: absolute;
        left: -14px;
        top: 2px;
    }"""

new_text = pattern.sub(clean_css, text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Fix 4 aplicado!")
