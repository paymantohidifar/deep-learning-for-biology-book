# Environment Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/paymantohidifar/deep-learning-for-biology-book.git --branch main dlfb
cd dlfb
```

### 2. Local Installation via `pixi` (Recommended)

[Pixi](https://pixi.sh/) is the recommended way to run this project. It manages a
per-chapter environment for you inside a local, hidden `.pixi/` directory, so each
chapter only pulls in the dependencies it actually needs.

Every environment builds on a shared `base` feature (numpy, pandas, scikit-learn,
jax/flax, jupyter, etc.). Chapter environments additionally layer on the chapter's
own dependencies plus `gpu` (CUDA-enabled JAX):

| Environment    | Features                      | Use for                                                |
|-----------------|--------------------------------|---------------------------------------------------------|
| `default`       | `base`                        | Chapter 1 (Introduction)                                 |
| `proteins`      | `base`, `proteins`, `gpu`     | Chapter 2 (Learning the Language of Proteins)             |
| `dna`           | `base`, `gpu`                 | Chapter 3 (Learning the Logic of DNA)                     |
| `graphs`        | `base`, `graphs`, `gpu`       | Chapter 4 (Drug–Drug Interactions Using Graphs)            |
| `cancer`        | `base`, `cancer`, `gpu`       | Chapter 5 (Detecting Skin Cancer in Medical Images)        |
| `localization`  | `base`, `localization`, `gpu` | Chapter 6 (Spatial Organization Patterns Within Cells)     |

```bash
# Optional: preview the dependency resolution without installing packages
pixi update --dry-run

# Install the default environment (base packages only, CPU)
pixi install

# Install a chapter-specific environment, e.g. proteins
pixi install -e proteins

# Launch Jupyter inside a given environment
pixi run -e proteins jupyter lab
```

> [!NOTE]
> `pixi.toml` currently targets **Linux (64-bit)** only.
