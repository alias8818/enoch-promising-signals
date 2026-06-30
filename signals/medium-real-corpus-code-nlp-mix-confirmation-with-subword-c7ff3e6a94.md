# Medium real-corpus code/NLP mix confirmation with subword GPT baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-real-corpus-code-nlp-mix-confirmation-with-subword-c7ff3e6a94`
Run ID: `medium-real-corpus-code-nlp-mix-confirmation-with-subword-c7ff3e6a94-20260612T075930600821+0000`

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

- Parent run decision: Code/NLP Mix Ratio Sweep for Tiny Mixed-Domain Pretraining: enoch://control-plane/projects/code-nlp-mix-ratio-sweep-for-tiny-mixed-domain-pretraining-1775cc36432f/runs/code-nlp-mix-ratio-sweep-for-tiny-mixed-domain-pretraining-1775cc36432f-20260611T214922817279+0000
- Parent run decision: Real-Corpus Tiny Code/NLP Mix Ratio Sweep: enoch://control-plane/projects/real-corpus-tiny-code-nlp-mix-ratio-sweep-96184152a4/runs/real-corpus-tiny-code-nlp-mix-ratio-sweep-96184152a4-20260612T074903961409+0000

## What looked useful

Correct domain tags produced small paired improvements over baseline on mixed loss (-0.0110 nats) and NLP loss (-0.0135 nats) across all seeds, and over random tags on mixed loss (-0.0071 nats) and NLP loss (-0.0145 nats), but code loss was not consistently improved and the margin is too small for a paper claim.

## Boundaries and scale limits

Not GPT-2-small-class; 6.26M parameters, 1500 steps, one Python code corpus, WikiText-2 NLP only, no downstream tasks, no long-run convergence, no larger-scale tokenizer/model robustness.

## Claim scope

On a small real WikiText-2 plus CodeSearchNet Python corpus with a 6.26M-parameter subword GPT trained for 1500 steps over seeds 11/22/33, correct domain prefix markers slightly reduce mixed and NLP validation loss versus a no-tag baseline and random-marker control when marker-token prediction is excluded.

## Why it stopped

Tier-2 medium real-corpus evidence found only a small mixed/NLP gain and mixed code-domain support; mechanism support is insufficient for publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should isolate prefix/length effects with constant-marker controls and text-token-only metrics before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prefix-control isolation for code/NLP domain markers in subword GPT
- Success threshold: Correct domain tags improve mixed validation loss by at least 0.015 nats versus every control, improve or tie both per-domain losses within 0.005 nats, and beat controls in at least 4 of 5 seeds.
- Stop condition: Stop if correct tags fail to beat constant/random/length controls on mixed loss, regress code loss by more than 0.005 nats, or effect remains below 0.015 nats after the predeclared seeds.

## Evidence references

- Artifact root: `<local-path>/projects/medium-real-corpus-code-nlp-mix-confirmation-with-subword-c7ff3e6a94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
