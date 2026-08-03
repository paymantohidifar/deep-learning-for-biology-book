# Deep Learning for Biology: Personal Study Notes & Reference

Welcome! This repository serves as a centralized hub for my personal study notes, architecture breakdowns, and implementations derived from *Deep Learning for Biology* by Christoff Ravarani and Natasha Latysheva.

## About This Repository

The purpose of this space is to provide a structured, easily accessible technical reference for AIxBio students and practitioners. It is designed to facilitate quick reviews of core concepts, algorithmic code snippets, and the deep learning models covered throughout the book.

* **Environment Orchestration:** A comprehensive, lean configuration guide to provision deterministic local runtime environments using `pixi`. For setup instructions, please refer to the [Environment Installation Guide](./INSTALL.md).
* **Cloud Runtimes:** All main notebooks include direct links to launch the execution context immediately on Google Colab.

> [!IMPORTANT]
> **Supplemental Learning Resource:** These notes and code summaries are designed to supplement your learning. They are **not** a substitute for the source material, assignments, and structural walk-throughs provided in the official publication. To fully grasp the underlying mathematics and engineering choices, I highly recommend purchasing the original book.

---

## Curriculum Breakdown

Click the links below to access the notebook for each book chapter.

1.  **[Chapter 1: Introduction](./notebooks/chapter1-intro.ipynb)**

2.  **[Chapter 2: Learning the Language of Proteins](./notebooks/chapter2-proteins.ipynb)**
    *Predict protein function from protein sequence using a linear classifier on transformer embeddings*

3.  **[Chapter 3: Learning the Logic of DNA](./notebooks/chapter3-dna.ipynb)**
    *Predict DNA-protein binding events from sequence using a convolutional neural network (CNN) and a transformer*

4.  **[Chapter 4: Understanding Drug–Drug Interactions Using Graphs](./notebooks/chapter4-graphs.ipynb)**
    *Predict whether a pair of drugs will interact using a graph neural network (GNN)*

5.  **[Chapter 5: Detecting Skin Cancer in Medical Images](./notebooks/chapter5-cancer.ipynb)**
    *Classify skin lesions using a convolutional neural network (CNN)*

6.  **[Chapter 6: Learning Spatial Organization Patterns Within Cells](./notebooks/chapter6-localization.ipynb)**
    *Predict protein subcellular localization using an autoencoder and a convolutional neural network (CNN)*

7.  **Chapter 7: Tips and Tricks for Deep Learning in Biology**

---

## Contribution & Feedback

If you spot a typographical error, discover an incorrect tensor operation, or have an improvement suggestion for the module implementations, contributions are welcome! Please feel free to open a descriptive GitHub issue or submit a structured pull request.

---

## Licensing

This project's notes and codebase additions are licensed under the [MIT License](./LICENSE).

---

## Acknowledgments & Citations

This repository is built while working through *Deep Learning for Biology* by Christoff Ravarani and Natasha Latysheva. All credit for the original concepts, datasets, and reference implementations belongs to the authors.

If you adapt these notes or implementations for your own research or projects, please cite the original textbook:

### APA Style

Ravarani, C., & Latysheva, N. (2025). *Deep learning for biology*. O'Reilly Media.

### BibTeX
```bibtex
@book{deep_learning_for_biology,
  title     = {Deep Learning for Biology},
  author    = {Ravarani, C. and Latysheva, N.},
  publisher = {O’Reilly Media},
  year      = {2025},
}
```
