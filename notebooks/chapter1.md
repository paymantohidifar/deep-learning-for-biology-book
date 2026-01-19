# Chapter 1:Introduction

Learn about the promise and challenges of deep learning in biology. You will be walked through practical questions to consider before launching a new project—like what your model could replace, whether deep learning is even necessary, and how to structure your workflow. This chapter also includes a short technical introduction covering JAX/Flax, Python patterns common in machine learning, working environments, and prac‐
tical setup tips.

## Using Code Examples

Supplemental material (code examples, exercises, etc.) is available for download at https://github.com/deep-learning-for-biology.


## Deciding What Your Model Will Replace

This section from the introductory chapter focuses on the strategic framing of biological deep learning projects, arguing that defining the "real-world" target of a model is more critical than the initial choice of architecture.

### Key Summary Points

* **Avoid the "Tinker Trap":** Deep learning in biology is intellectually stimulating, which often leads researchers to spend excessive time on technical minutiae. To remain focused, one must identify the existing process the model is intended to replace or improve.
* **Domain-Specific Impact Areas:**
    * **Healthcare & Drug Discovery:** Models aim to replace slow or manual tasks such as dermatological diagnosis, culture-based pathogen detection, manual MRI tumor segmentation, and exhaustive wet-lab screening for drug-target interactions.
    * **Molecular Biology:** Computational tools like **AlphaFold** provide 3D protein structures that would otherwise require months of expensive X-ray crystallography or Cryo-EM. Other models act as digital alternatives to RNA-seq (gene expression) or manual variant interpretation.
    * **Ecology:** AI replaces labor-intensive field work, such as in-person biodiversity surveys (via acoustics) or manual crop scouting (via satellite/drone imagery), and offers non-invasive alternatives to physical animal tagging.
* **Quantifying Success:** Researchers should estimate the potential impact in terms of time, cost, or labor. For instance, if a manual process takes  and the model takes , the speedup  can be expressed as:
* **Innovation vs. Replacement:** Not all models replace old workflows. Some enable **entirely new capabilities**, such as generating *de novo* biological sequences or linking disparate data types that were previously incompatible. In these cases, success must be evaluated without established benchmarks.


## Determining Your Criteria for Success

**Main Concept:**
Define success metrics early to avoid endless, unfocused experimentation and wasted time in deep learning projects.

**Five Types of Success Criteria:**

1. **Performance Metrics**
   - Examples: accuracy, AUC, F1 score
   - Goals may include matching human expert performance, achieving experimental correlation, or maintaining low false-positive rates

2. **Interpretability Requirements**
   - Focus on explainability and transparency of model decisions
   - Important for domain expert trust, calibrated uncertainty estimates, and understandable feature attributions

3. **Model Size and Inference Efficiency**
   - Critical for resource-constrained environments (smartphones, embedded devices)
   - Metrics include inference time, memory usage, energy consumption, and performance per FLOP (floating point operation)
   - May prioritize efficiency over raw accuracy for real-time applications

4. **Training Efficiency**
   - Relevant when compute resources are limited or in educational settings
   - May focus on CPU-compatible models rather than GPU-dependent ones
   - Prioritizes fast training and minimal hardware requirements

5. **Generalizability**
   - Aims for models that work across multiple datasets or tasks
   - Relevant for foundational models designed for broad applicability
   - Values flexibility and reusability over single-task optimization

**Key Takeaway:**
Establishing clear success criteria upfront helps determine when a project is complete and ensures efforts remain focused and realistic while balancing multiple objectives.

## Invest Heavily in Evaluations

**Core Message:**
Evaluation strategy should be a top priority from the start, not an afterthought—it guides the entire project and determines whether your work produces meaningful results.

**What Strong Evaluation Involves:**
- Defining precise measurement methods and metrics
- Establishing validation procedures
- Selecting appropriate baselines for comparison
- Creating a well-designed evaluation strategy before building models

**Benefits of Strong Evaluations:**
- Measure progress accurately
- Detect bugs in models or pipelines
- Estimate task difficulty
- Build intuition about the problem
- Provide a known point of comparison to assess if the model is learning meaningfully

**Recommended Time Allocation:**
A rough guideline for successful machine learning projects:
- **50%** - Designing evaluation strategies and running baselines
- **25%** - Curating or processing data
- **25%** - Model architecture development

**Critical Warning:**
Without good evaluations, you operate blindly—unable to determine if your model is improving, understand trade-offs, or verify meaningful learning is occurring.

**Key Principle:**
Evaluation is not an end-stage activity. It should be designed at the beginning and used to guide decisions throughout the entire project lifecycle.

