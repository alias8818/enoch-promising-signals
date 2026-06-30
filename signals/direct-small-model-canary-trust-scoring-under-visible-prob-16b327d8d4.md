# Direct small-model canary trust scoring under visible-probe contamination

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-small-model-canary-trust-scoring-under-visible-prob-16b327d8d4`
Run ID: `direct-small-model-canary-trust-scoring-under-visible-prob-16b327d8d4-20260610T025059535603+0000`

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

- Parent run decision: Held-out Canary Probe Trust Scoring: enoch://control-plane/projects/held-out-canary-probe-trust-scoring-8eb74a912e19/runs/held-out-canary-probe-trust-scoring-8eb74a912e19-20260609T174310610179+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e59032affdc1

## What looked useful

Clean hidden canary scoring achieved mean AUC 0.9921 against never-seen holdouts in the 3x contamination run, while probe-contaminated held-outs had 1.0000 false-positive rate at the clean memorized threshold. Equal-repeat contamination showed a smaller 0.1528 false-positive rate, and inference-visible-only prompting showed 0.0000 held-out false positives.

## Boundaries and scale limits

Three-seed local synthetic test only; no pretrained LLMs, natural canaries, web-scale mixtures, or production benchmark contamination were tested.

## Claim scope

In a synthetic small character-level causal transformer, canary trust scoring remains cleanly discriminative for memorized canaries versus never-seen held-outs, but repeated visible-probe training exposure can make held-out canaries exceed the memorized-canary trust threshold.

## Why it stopped

Tier 1 controlled small direct test completed with useful mechanism evidence, but evidence is synthetic and not publication-grade.

## Recommended next action

Run a bounded dose-response deepen test with contamination repeats swept across at least five levels and one pretrained small LM/tokenizer ablation; stop paper escalation until that confirms robustness outside the synthetic character model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Dose-response visible-probe canary contamination across tokenization and small pretrained models
- Success threshold: Contaminated held-out false-positive rate at the clean memorized threshold increases monotonically and reaches >= 0.50 in at least one non-character-model setting while never-seen holdout FPR stays <= 0.10.
- Stop condition: Stop if clean scoring AUC falls below 0.80, never-seen holdout FPR exceeds 0.10 before contamination is added, or contaminated false-positive rate remains below 0.25 at all exposure levels.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-model-canary-trust-scoring-under-visible-prob-16b327d8d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
