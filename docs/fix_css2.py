import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'\.sidebar-nav ul:not\(\.app-sub-sidebar\)>li:not\(\.file\)::before', re.DOTALL)

# Trocamos para focar APENAS em li.collapse (pastas fechadas) e li.open (pastas abertas)
new_css = ".sidebar-nav ul:not(.app-sub-sidebar)>li.collapse::before, .sidebar-nav ul:not(.app-sub-sidebar)>li.open::before"

new_text = pattern.sub(new_css, text)

# Precisamos garantir que o li.open não fique com o "▸" por baixo.
# Na verdade a regra original coloca "▸" para todos, e depois "▾" para o open.
# Com a nova regra, "▸" aplica para collapse e open, e depois "▾" sobrescreve pro open. Isso funciona perfeitamente!

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Fix aplicado!")
