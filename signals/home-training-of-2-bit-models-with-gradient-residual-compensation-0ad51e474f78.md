# Home-Training of 2-bit Models with Gradient Residual Compensation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `home-training-of-2-bit-models-with-gradient-residual-compensation-0ad51e474f78`
Run ID: `home-training-of-2-bit-models-with-gradient-residual-compensation-0ad51e474f78-20260629T193946198298+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d9402cc56d81

## What looked useful

Primary 5-seed run showed residual-compensated 2-bit updates at 0.8055 mean test accuracy versus 0.8209 for uncompensated 2-bit updates and 0.8166 for 2-bit-forward/full-update QAT. Deadzone sensitivity showed residuals can partially recover harsh update quantization loss, but the best gain was +0.0290, below the predeclared +0.05 useful threshold.

## Boundaries and scale limits

No transformer, token dataset, GPT-2-small-class model, long run, GPU kernel, or home-training wall-clock validation was performed. Results apply only to this small deterministic synthetic classification proxy.

## Claim scope

Bounded NumPy MLP proxy for 2-bit-forward training with 2-bit optimizer update compression. Residual compensation did not robustly improve accuracy over uncompensated 2-bit updates and did not beat the 2-bit-forward/full-update QAT control.

## Why it stopped

Proxy evidence did not meet the predeclared residual-compensation success threshold and is not direct/full validation of 2-bit home training.

## Recommended next action

Stop this run as a no-paper useful-signal result; if pursued, run a bounded tiny character-transformer or GPT-2-small-class proxy with matched 2-bit-forward/full-update and 2-bit-update controls before any larger scale work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny language-model test of residual-compensated 2-bit update training
- Success threshold: Residual-compensated 2-bit updates reduce validation perplexity by at least 5% versus uncompensated 2-bit updates and come within 3% of 2-bit-forward/full-update QAT across at least three seeds.
- Stop condition: Stop if residual compensation fails to beat uncompensated 2-bit updates by 5% perplexity or if it remains worse than the full-update QAT control after the bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/home-training-of-2-bit-models-with-gradient-residual-compensation-0ad51e474f78`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
