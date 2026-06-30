# Tiny contrastive critic for local pretraining data curation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-contrastive-critic-for-local-pretraining-data-curation-522d5c92e966`
Run ID: `tiny-contrastive-critic-for-local-pretraining-data-curation-522d5c92e966-20260528T080903376555+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1290e91868e3

## What looked useful

The critic beat random and keyword selection on eval NLL in 5/5 seeds. Mean NLL was 4.0322 for critic, 4.1086 for keyword, 4.1463 for random, and 3.9265 for oracle. Keyword selection was partly fooled by adversarial keyword-heavy documents; the contrastive critic reduced that failure enough to improve the downstream LM proxy metric.

## Boundaries and scale limits

Synthetic token-mixture corpus only; 1800 candidate documents per seed; 450-document selection budget; 160 target seed documents; tiny GRU LM; no real web corpus, transformer pretraining, deduplication stack, contamination analysis, or downstream transfer.

## Claim scope

In a controlled synthetic mixed-corpus proxy with target, off-domain, boilerplate, random, and adversarial keyword-heavy documents, a tiny contrastive seed-document critic selected data that improved a tiny GRU language model's held-out target-domain NLL versus random and naive keyword selection across 5 seeds.

## Why it stopped

No-paper closure: this run produced a useful synthetic proxy signal, but the evidence is not direct or broad enough for publication-grade validation.

## Recommended next action

Run a bounded real-corpus follow-up using a small local text corpus, a transformer LM baseline, and strong heuristic controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus contrastive critic curation with transformer LM validation
- Success threshold: Contrastive critic improves held-out target validation NLL by at least 0.05 versus the strongest non-oracle heuristic in at least 4/5 seeds at one budget, without relying on leaked validation documents.
- Stop condition: Stop as unsupported if the critic fails to beat the strongest cheap heuristic on mean target validation NLL at both tested budgets or if gains appear only from obvious leakage/duplication.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-contrastive-critic-for-local-pretraining-data-curation-522d5c92e966`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
