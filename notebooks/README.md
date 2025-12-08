# Semiotic Collapse Analysis Notebook

This directory contains the Jupyter notebook for generating the mechanistic analysis and visualizations featured in the blog post.

## 📓 Files

- `semiotic_collapse_analysis.ipynb` - Main analysis notebook with all experimental code
- `generate_visuals.py` - Standalone Python script version (for local execution)

## 🚀 Running on Google Colab

The easiest way to run this analysis is on Google Colab:

1. Upload `semiotic_collapse_analysis.ipynb` to Google Colab
2. Run **Cell 0** first - this installs dependencies
3. **Restart the runtime** when prompted (Runtime → Restart Session)
4. After restart, run **Cells 1-8** in sequence
5. The notebook will generate interactive Plotly visualizations

### Important Notes

- **Do NOT re-run Cell 0 after restarting** - it checks if packages are already installed
- The notebook uses GPT-2 Small (~500MB) which will download automatically
- GPU is not required but recommended for faster inference
- Expected runtime: 5-10 minutes on CPU, 2-3 minutes on GPU

## 📊 Outputs

The notebook generates:

1. **L1H0 Stability Plot** - Attention to previous token (Control vs Rot)
2. **Entropy Distribution** - Box plots comparing attention entropy
3. **Causal Patching Results** - Recovery probability when L1H0 is restored

## 🔧 Running Locally

If you want to run the script locally:

```bash
# Install dependencies
pip install torch numpy==1.26.4 pandas plotly transformer-lens kaleido pytz

# Run the visualization script
cd notebooks
python generate_visuals.py
```

The script will save HTML and PNG versions of all figures to `../assets/img/blog/`.

## 📁 Repository Structure

```
semiotic_collapse/
├── _posts/
│   └── 2025-12-08-semiotic-collapse.md   # Blog post
├── assets/
│   ├── bibliography/
│   │   └── 2025-12-08-semiotic-collapse.bib
│   └── img/blog/                         # Generated visualizations
│       ├── l1h0_stability.html
│       ├── causal_patching.html
│       └── entropy_distribution.html
└── notebooks/
    ├── README.md                          # This file
    ├── semiotic_collapse_analysis.ipynb   # Colab notebook
    └── generate_visuals.py                # Standalone script
```

## 🐛 Troubleshooting

### "NumPy version conflict"
- Make sure you restart the runtime after Cell 0
- Do not re-run Cell 0 after restarting

### "Model download failed"
- Check your internet connection
- GPT-2 Small requires ~500MB download

### "CUDA out of memory"
- Switch to CPU: The notebook will automatically use CPU if GPU is unavailable
- Reduce batch size if needed (though this notebook processes single sequences)

## 📚 Citation

If you use this code or analysis, please cite:

```bibtex
@article{semiotic_collapse_2025,
  title={The Semiotic Collapse: Bidirectional Mechanistic Interpretability of Agent Failure},
  author={Artifex Labs Team},
  year={2025},
  url={https://github.com/Tuesdaythe13th/semiotic_collapse}
}
```

## 📄 License

This analysis is part of an anonymous submission to the ICLR 2026 Blog Post Track.
