# Environment Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/paymantohidifar/deep-learning-for-biology-book.git --branch main dlfb
cd dlfb
```

### 2. Local Installation via `uv` / `pip` (Fastest)

[uv](https://docs.astral.sh/uv/) is the fastest way to get running. The dependency
set is exposed as standard `[project.optional-dependencies]` extras in
`pyproject.toml`, so `uv` or `pip` users can install directly, e.g.:

```bash
# CPU-only proteins environment
uv sync --extra proteins-cpu

# GPU-enabled proteins environment
uv sync --extra proteins --extra gpu
```

`torch` is automatically routed to the CPU-only wheel index for the `-cpu` extras
via `[tool.uv.sources]`, so no CUDA binaries are downloaded in that case either.

### 3. Local Installation via `pixi` (Recommended for reproducibility)

[Pixi](https://pixi.sh/) manages a per-chapter environment for you inside a local,
hidden `.pixi/` directory, so each chapter only pulls in the dependencies it
actually needs. It reads its configuration from the `[tool.pixi.*]` tables in
`pyproject.toml`.

Every environment builds on a shared `base` feature (numpy, pandas, scikit-learn,
jax/flax, jupyter, etc.). Each chapter is available as a **GPU environment** (adds
the `gpu` feature: CUDA-enabled JAX, plus CUDA-enabled `torch` where relevant) and
as a matching **`-cpu` environment** that skips all CUDA/Nvidia binaries entirely —
useful for local runs on a machine without a GPU:

| Chapter                                                  | GPU environment | CPU environment    |
|-----------------------------------------------------------|-----------------|---------------------|
| Chapter 1 (Introduction)                                   | `default`       | `default`            |
| Chapter 2 (Learning the Language of Proteins)               | `proteins`      | `proteins-cpu`       |
| Chapter 3 (Learning the Logic of DNA)                       | `dna`           | `dna-cpu`            |
| Chapter 4 (Drug–Drug Interactions Using Graphs)              | `graphs`        | `graphs-cpu`         |
| Chapter 5 (Detecting Skin Cancer in Medical Images)          | `cancer`        | `cancer-cpu`         |
| Chapter 6 (Spatial Organization Patterns Within Cells)       | `localization`  | `localization-cpu`   |

`default` has no GPU dependencies to begin with, so there's no separate `default-cpu`
variant.

```bash
# Optional: preview the dependency resolution without installing packages
pixi update --dry-run

# Install the default environment (base packages only, CPU)
pixi install

# Install a chapter-specific GPU environment, e.g. proteins
pixi install -e proteins

# ...or its CPU-only counterpart (no CUDA/Nvidia binaries downloaded)
pixi install -e proteins-cpu

# Launch Jupyter inside a given environment
pixi run -e proteins-cpu jupyter lab
```

> [!NOTE]
> These environments currently target **Linux (64-bit)** only.
