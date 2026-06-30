# DistillAudit: Held-Out Sample Overlap as Cheating Resistance in Volunteer Distillation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `distillaudit-held-out-sample-overlap-as-cheating-resistance-in-volunteer-distillation-b24fc0ba14b4`
Run ID: `distillaudit-held-out-sample-overlap-as-cheating-resistance-in-volunteer-distillation-b24fc0ba14b4-20260610T021733761745+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7d69054757c

## What looked useful

Held-out overlap is useful as a cheap low-effort contamination screen, not as standalone cheating resistance. Exact and light contamination were flagged in 100% of tested submissions at 1%-5% contamination with 0/150 benign flags after strict-threshold calibration; heavy template rewrites were flagged 0% of the time.

## Boundaries and scale limits

No real LLM distillation, no real volunteer data, no downstream student training, no semantic paraphrase model, and no embedding/model-based detector. Main corrected run used 300 hidden examples, 300-row submissions, 150 benign calibration trials, and 60 trials per attack/rate.

## Claim scope

Synthetic volunteer distillation submissions with hidden held-out contamination, using token 4-shingle overlap calibrated on benign submissions. The audit reliably detects exact and light lexical held-out reuse but fails on heavy template rewrites.

## Why it stopped

Proxy evidence supports only a narrow low-effort duplicate-detection claim and early-falsifies the stronger standalone cheating-resistance claim under heavy rewrite contamination.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should add LLM-generated paraphrases plus semantic/embedding overlap baselines on the same calibrated benign-control protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semantic DistillAudit Against LLM-Paraphrased Held-Out Contamination
- Success threshold: At <=1% benign submission false-positive rate, semantic detector flags at least 80% of heavy-rewrite contaminated submissions at 2% contamination and outperforms token-shingle overlap by at least 30 percentage points.
- Stop condition: Stop if semantic detectors remain below 50% true-positive rate at 2% heavy-rewrite contamination or if benign false positives exceed the calibrated target after threshold correction.

## Evidence references

- Artifact root: `<local-path>/projects/distillaudit-held-out-sample-overlap-as-cheating-resistance-in-volunteer-distillation-b24fc0ba14`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
