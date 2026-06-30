# End-to-end GPT-2-small speculative verifier for trained EAGLE dynamic K selector

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `end-to-end-gpt-2-small-speculative-verifier-for-trained-ea-35c3aac999`
Run ID: `end-to-end-gpt-2-small-speculative-verifier-for-trained-ea-35c3aac999-20260520T014407413908+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-model dynamic vocabulary trace for EAGLE-like speculative heads: enoch://control-plane/projects/real-model-dynamic-vocabulary-trace-for-eagle-like-specula-1c3697bc69/runs/real-model-dynamic-vocabulary-trace-for-eagle-like-specula-1c3697bc69-20260520T003942830919+0000
- Parent run decision: Trained GPT-2-small EAGLE head with cheap K=256/K=512 dynamic selector: enoch://control-plane/projects/trained-gpt-2-small-eagle-head-with-cheap-k-256-k-512-dyna-ef4958c1fe/runs/trained-gpt-2-small-eagle-head-with-cheap-k-256-k-512-dyna-ef4958c1fe-20260520T012746767897+0000

## What looked useful

Exact verifier mechanics are reproducible and useful: all policies had zero mismatches against GPT-2-small greedy decoding while dynamic K reduced target calls by 61-70%. However, dynamic K versus best fixed K4 had ratios 1.017, 0.922, and 1.000, mean 0.980, so the selector advantage is unstable and not paper-positive.

## Boundaries and scale limits

No real EAGLE head was trained; distilgpt2 was used as the pretrained draft/proxy. Evaluation used a compact hand-written prompt corpus, 2,752 held-out generated tokens across three fixed seeds/splits, and a simple latency model plus wall throughput. This is not full-corpus or publication-grade EAGLE validation.

## Claim scope

In a bounded GPT-2-small target plus distilgpt2 draft setup, exact speculative verification with target correction preserved greedy GPT-2-small outputs and reduced target calls, but a trained linear dynamic-K selector did not robustly beat the best fixed-K control.

## Why it stopped

Bounded direct validation supported exact speculative verification but failed to show a robust trained dynamic-K advantage over fixed K4; the setup also used a distilgpt2 draft proxy rather than a trained EAGLE head.

## Recommended next action

Stop this follow-up as no-paper useful evidence; only reopen with a real trained EAGLE head and a larger held-out benchmark that can test dynamic K against fixed and oracle controls.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-gpt-2-small-speculative-verifier-for-trained-ea-35c3aac999`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
