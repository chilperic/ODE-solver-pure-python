# Getting Started with PyODESolve

## 🚀 Quick Setup (5 minutes)

### 1. Complete the Code

The solver classes need to be copied from the artifact:

1. Open the first PyODESolve artifact (the long one with all solver code)
2. Copy each class to its corresponding file:

**Core classes:**
- `BaseODESolver` → `pyodesolve/core/base.py`
- `ODEResult` → `pyodesolve/core/result.py`
- `SolverStatistics` → `pyodesolve/core/statistics.py`

**Solver classes:**
- `DormandPrince` → `pyodesolve/explicit/dormand_prince.py`
- `BDF` → `pyodesolve/implicit/bdf.py`
- `RadauIIA` → `pyodesolve/implicit/radau.py`

**Update imports** in each file to use relative imports:
```python
from ..core.base import BaseODESolver
from ..core.result import ODEResult
```

### 2. Install

```bash
cd pyodesolve_project
pip install -e .
```

### 3. Test

```bash
python examples/basic_usage.py
pytest tests/
```

### 4. Upload to GitHub

```bash
git init
git add .
git commit -m "Initial commit: PyODESolve v0.1.0"
git remote add origin https://github.com/YOUR_USERNAME/pyodesolve.git
git push -u origin main
```

## 📋 Before GitHub Upload

Update these files:
- `setup.py` - Change author name, email, URL
- `README.md` - Change contact email and repo URL
- `LICENSE` - Change copyright name

## ✅ Done!

Your ODE solver library is ready for the world! 🎉
