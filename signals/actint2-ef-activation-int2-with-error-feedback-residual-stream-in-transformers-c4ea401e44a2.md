# ActINT2-EF: Activation INT2 with error-feedback residual stream in transformers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `actint2-ef-activation-int2-with-error-feedback-residual-stream-in-transformers-c4ea401e44a2`
Run ID: `actint2-ef-activation-int2-with-error-feedback-residual-stream-in-transformers-c4ea401e44a2-20260619T191623493939+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b31f7ad93d46

## What looked useful

At 300 steps, mean eval loss was fp 1.5429, naive INT2 2.7554, INT2+EF 2.3526. EF improved over naive INT2 by 0.4028 nats and reduced effective residual-stream quantization MSE to 0.338x naive. At 120 steps, EF improved over naive INT2 by 0.4955 nats and reduced MSE to 0.640x naive. EF remained worse than full precision.

## Boundaries and scale limits

No real C4/OpenWebText/TinyStories data, no GPT-2-small-class parameter scale, no pretrained checkpoint, no inference-only post-training quantization study, no optimized packed INT2 kernels, and no long-run robustness or architecture ablations.

## Claim scope

Small decoder-only transformer on a deterministic synthetic language-modeling held-out split: INT2 residual-stream activation quantization with layer-to-layer error feedback reduced effective residual-stream quantization MSE and improved eval loss versus naive INT2 across 3 seeds at 120 and 300 training steps.

## Why it stopped

No-paper useful-signal closure: the mechanism is supported only by small synthetic transformer evidence, not direct C4/GPT-2-small-class validation.

## Recommended next action

Run a bounded real-text GPT-2-small-class deepen test comparing fp, naive INT2 residual-stream activation quantization, and INT2+EF on held-out perplexity plus activation-error diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text GPT-2-small-class validation of INT2 residual-stream error feedback
- Success threshold: INT2+EF improves held-out perplexity or cross-entropy versus naive INT2 in at least 2 of 3 seeds while reducing residual-stream activation-error MSE by at least 25%, without claiming parity with full precision.
- Stop condition: Stop if INT2+EF fails to improve held-out loss versus naive INT2 in at least 2 of 3 seeds or if activation-error diagnostics do not show a consistent reduction.

## Evidence references

- Artifact root: `<local-path>/projects/actint2-ef-activation-int2-with-error-feedback-residual-stream-in-transformers-c4ea401e44a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
