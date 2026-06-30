# INT2 Adam optimizer state with residual compensation for home fine-tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-adam-optimizer-state-with-residual-compensation-for-home-fine-tuning-eb5cd492f72a`
Run ID: `int2-adam-optimizer-state-with-residual-compensation-for-home-fine-tuning-eb5cd492f72a-20260619T052931887633+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4434a2c467db

## What looked useful

Residual compensation is necessary for INT2 Adam state in this harness. fp32 residuals recover behavior but erase memory savings; fp16 residuals keep a meaningful memory saving but are learning-rate sensitive and unstable at the default LR.

## Boundaries and scale limits

Evidence is limited to deterministic synthetic MLP regression/classification proxies, 300-step runs, 5 seeds, simulated block quantization, and no packed kernel or real LLM/LoRA fine-tuning validation.

## Claim scope

Small CPU PyTorch proxy tests show that naive INT2 Adam moment state is unstable, while fp16 residual-compensated INT2 can be stable under lower learning rates with an estimated optimizer-state footprint of 4.5625 bytes/parameter, about 57% of full Adam state for block size 256.

## Why it stopped

Proxy evidence is mixed and not paper-ready: it falsifies naive INT2 Adam state and identifies a narrower fp16-residual regime, but direct real fine-tuning evidence is still missing.

## Recommended next action

Run a bounded direct LoRA or GPT-2-small-class fine-tuning follow-up with packed INT2+fp16-residual optimizer state, tuned LR grid, validation loss, memory accounting, and late-training stability checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LoRA fine-tuning validation for INT2 Adam state with fp16 residuals
- Success threshold: INT2+fp16 residual reaches validation loss within 5% of tuned full Adam on at least 3 seeds while using at least 35% less optimizer-state memory and without divergence.
- Stop condition: Stop if all stable LR settings are more than 10% worse than full Adam validation loss, diverge in more than one seed, or measured memory savings fall below 25%.

## Evidence references

- Artifact root: `<local-path>/projects/int2-adam-optimizer-state-with-residual-compensation-for-home-fine-tuning-eb5cd492f72a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
