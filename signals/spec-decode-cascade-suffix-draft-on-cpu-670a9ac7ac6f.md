# Spec-Decode Cascade: Suffix Draft on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `spec-decode-cascade-suffix-draft-on-cpu-670a9ac7ac6f`
Run ID: `spec-decode-cascade-suffix-draft-on-cpu-670a9ac7ac6f-20260621T091512084710+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/92728ff62b1b

## What looked useful

High-reuse traces showed suffix-only acceptance 0.6693 and cascade wasted-draft reduction of 0.1324 tokens/output versus bigram-only, but cascade pass reduction was lower than bigram-only in high, medium, and low reuse scenarios.

## Boundaries and scale limits

No transformer verifier, no real tokenizer/LLM traces, no KV-cache or serving latency measurement, no CPU/GPU transfer effects, and no broad corpus validation. Calibrated run used 12 seeds, 20,000 tokens per seed/scenario, and 4,000 replay steps.

## Claim scope

CPU-only deterministic proxy over synthetic held-out token traces: suffix-table drafts are cleaner when suffix reuse is high and can reduce wasted draft tokens in a suffix-then-bigram cascade, but the cascade did not improve verifier-pass reduction over a bigram-only baseline.

## Why it stopped

Proxy evidence is useful but mixed: suffix drafting reduces wasted draft work on repeated traces, while the cascade fails to beat the bigram baseline on verifier-pass reduction.

## Recommended next action

Run a bounded direct-model follow-up on real tokenizer-level LLM traces with a small transformer verifier before considering any speedup or paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-level suffix draft replay with a small transformer verifier
- Success threshold: Cascade must match or exceed baseline verifier-pass reduction while reducing wasted draft tokens by at least 10% on reuse-heavy traces, with no regression larger than 2% on low-reuse traces.
- Stop condition: Stop if suffix reuse in real traces is too sparse to trigger on at least 10% of decode steps or if cascade pass reduction remains below baseline after threshold calibration.

## Evidence references

- Artifact root: `<local-path>/projects/spec-decode-cascade-suffix-draft-on-cpu-670a9ac7ac6f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
