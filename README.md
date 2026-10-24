# recipe-window-clipper

## Français

Trouver la région exacte de réglages satisfaisant une recette.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m recipe_window_clipper examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Intersection exacte de demi-plans rationnels dans une boîte de paramètres 2D déclarée ; fournit sommets, aire et sous-ensemble contradictoire irréductible. Contrairement à tolerance-stack-witness, cherche des réglages admissibles plutôt que le pire empilement dimensionnel.

### Limites

Deux paramètres linéaires seulement ; boîte fixée hors du noyau contradictoire. Les inégalités et unités sont fournies, pas apprises ni validées sur une machine.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Find the exact settings region satisfying a process recipe.

Synthetic data; no network access or secret required.

```sh
python -m recipe_window_clipper examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Exact rational half-plane intersection inside a declared2D parameter box; returns vertices, area and an irreducible conflicting subset. Unlike tolerance-stack-witness, finds feasible settings rather than a worst dimensional stack.

### Limits

Two linear parameters only; fixed box is outside the conflicting subset. Inequalities and units are supplied, not learned or machine-validated.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Encontrar la región exacta de ajustes que satisface una receta.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m recipe_window_clipper examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Intersección exacta de semiplanos racionales en una caja2D declarada; devuelve vértices, área y subconjunto contradictorio irreducible. A diferencia de tolerance-stack-witness, busca ajustes viables y no el peor apilamiento dimensional.

### Límites

Solo dos parámetros lineales; caja fija fuera del subconjunto contradictorio. Desigualdades y unidades suministradas, no aprendidas ni validadas en máquina.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.nist.gov/programs-projects/metrology-real-time-monitoring-additive-manufacturing
