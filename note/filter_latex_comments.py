import os
os.chdir(os.path.dirname(__file__))

alll = []
files = ['clp_basic_notes.tex', 'clp_limits_notes.tex', 'clp_differentiation_notes.tex', 'clp_applications_notes.tex']
for f in files:
    for l in open(f, 'r'):
        ll = l.strip()
        if ll:
            if ll[0] == '%':
                pass
            else:
                alll.append(ll)

open('clp1.tex', 'w').write('\n'.join(alll))
