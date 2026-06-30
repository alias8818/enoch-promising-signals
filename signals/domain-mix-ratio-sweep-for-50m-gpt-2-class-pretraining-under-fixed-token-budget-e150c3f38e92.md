# Domain-mix ratio sweep for 50M GPT-2-class pretraining under fixed token budget

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `domain-mix-ratio-sweep-for-50m-gpt-2-class-pretraining-under-fixed-token-budget-e150c3f38e92`
Run ID: `domain-mix-ratio-sweep-for-50m-gpt-2-class-pretraining-under-fixed-token-budget-e150c3f38e92-20260620T214603474197+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b2ebbeadc454

## What looked useful

A reproducible 11-ratio x 5-seed sweep found best target NLL at 0.5 domain-A ratio: 5.222957684681434 bits versus best edge-only target NLL 7.619261904196639 bits, a 2.396304219515205-bit gap. This supports the sweep mechanism and shows why edge-only mixes are poor under balanced evaluation, but it does not validate the original 50M GPT-2-class claim.

## Boundaries and scale limits

No neural Transformer was trained. No real text corpus, tokenizer, optimizer dynamics, 50M-parameter model, or GPT-2-class pretraining run was tested. The evidence is a CPU-bounded synthetic n-gram proxy only.

## Claim scope

Under a fixed token budget in a synthetic two-domain causal bigram language-model proxy, an equal-weighted validation objective selected an interior 0.5/0.5 training mix and strongly penalized single-domain edge mixes.

## Why it stopped

Closed as a proxy useful signal rather than full validation; the worker produced reproducible synthetic evidence but not direct GPT-2-class pretraining evidence.

## Recommended next action

Run a bounded neural follow-up: train a small causal Transformer on two real text domains with the same fixed-token ratio sweep, three seeds, and per-domain validation curves.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer fixed-token domain-mix sweep on real text domains
- Success threshold: An interior mix beats both edge-only mixes on the target-weighted validation objective by at least 0.05 bits/token mean across three seeds, without hiding a severe regression on either domain.
- Stop condition: Stop if the neural runs exceed the local compute budget, fail to beat edge-only controls, or show seed variance larger than the observed interior-vs-edge effect.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mix-ratio-sweep-for-50m-gpt-2-class-pretraining-under-fixed-token-budget-e150c3f38e92`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
